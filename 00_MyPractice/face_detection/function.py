import dlib
import cv2
import numpy as np
from PyQt5 import  QtCore
from pyqt5_plugins.examplebuttonplugin import QtGui

# 初始化 dlib 的人脸检测器和关键点检测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('model/dlib_model/shape_predictor_68_face_landmarks.dat')

def open_camera(ui):
    ui.cap = cv2.VideoCapture(0)
    # ui.cap = cv2.VideoCapture(1)
    if not ui.cap.isOpened():
        raise ValueError("无法从摄像头读取视频流！")
    ui.timer = QtCore.QTimer()
    ui.timer.timeout.connect(lambda: update(ui))
    ui.timer.start(50)

# 定义获取左右眼关键点的函数
def get_eye_points(shape):
    left_eye_points = list(range(36, 42))
    right_eye_points = list(range(42, 48))
    left_eye = dlib.points([shape.part(i) for i in left_eye_points])
    right_eye = dlib.points([shape.part(i) for i in right_eye_points])
    return left_eye, right_eye


left_eye_aspect_ratio = []
right_eye_aspect_ratio = []
# 定义人眼开合度检测函数
def detect_eyes(frame):
    # 将彩色图像转为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 使用 dlib 的人脸检测器检测人脸
    faces = detector(gray)
    if len(faces) > 0:
        # 使用 dlib 的关键点检测器获取关键点坐标
        shape = predictor(gray, faces[0])
        # 提取左右眼关键点坐标
        left_eye, right_eye = get_eye_points(shape)
        # 计算左眼开合度
        left_eye_ratio = 0.5 * ((left_eye[1].y + left_eye[2].y) - (left_eye[0].y + left_eye[3].y)) / \
                         (left_eye[4].x - left_eye[1].x)
        # 若左眼开合度小于阈值，则将其开合度设置为 0
        left_eye_ratio = 0.1 if left_eye_ratio < -0.5 else left_eye_ratio + 1

        # 计算右眼开合度
        right_eye_ratio = 0.5 * ((right_eye[1].y + right_eye[2].y) - (right_eye[0].y + right_eye[3].y)) / \
                          (right_eye[4].x - right_eye[1].x)
        # 若右眼开合度小于阈值，则将其开合度设置为 0
        right_eye_ratio = 0.1 if right_eye_ratio < -0.5 else right_eye_ratio + 1

        return left_eye_ratio, right_eye_ratio
    else:
        # 如果未检测到眼睛就返回 None
        return 0, 0


# # 检测嘴部
def detect_mouth(frame):
    # 将彩色图像转为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用 dlib 的人脸检测器检测人脸
    faces = detector(gray)

    # 遍历所有检测到的人脸
    for face in faces:
        # 使用 dlib 的关键点检测器检测人脸特征点
        shape = predictor(gray, face)

        # 提取嘴部区域的坐标值
        mouth_x1 = shape.part(48).x
        mouth_y1 = shape.part(62).y
        mouth_x2 = shape.part(54).x
        mouth_y2 = shape.part(66).y

        # 计算嘴巴的宽度和高度
        mouth_w = mouth_x2 - mouth_x1
        mouth_h = mouth_y2 - mouth_y1

        # # 提取嘴部区域
        # mouth_roi = frame[mouth_y1:mouth_y2, mouth_x1:mouth_x2]
        #
        # # 显示嘴部区域
        # cv2.imshow("Mouth ROI", mouth_roi)

        # 计算嘴巴开合度并返回
        # ratio = mouth_h / mouth_w
        return mouth_h, mouth_w - 25

    # 如果未检测到人脸，则返回 None
    return 0, 0


#
# # 检测微笑
# 定义微笑区域
smile_region_points = [48, 54, 62, 66]
def detect_smile(frame):
    # 将彩色图像转为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 使用 dlib 的人脸检测器检测人脸
    faces = detector(gray)
    for face in faces:
        # 使用关键点检测器检测关键点
        landmarks = predictor(gray, face)
        # 计算微笑区域的坐标
        smile_pts = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in smile_region_points])
        # 计算嘴巴区域的形态
        mouth_width = abs(landmarks.part(54).x - landmarks.part(48).x)
        mouth_height = abs(landmarks.part(66).y - (landmarks.part(62).y + landmarks.part(66).y) / 2)
        if mouth_height == 0:
            return 0.05  # 如果嘴巴高度为0，返回None
        mouth_aspect_ratio = float(mouth_width) / mouth_height
        # 判断是否微笑
        if mouth_aspect_ratio > 0.6 and mouth_width > 50:
            # 计算微笑程度（示例代码仅供参考）
            smile_area = cv2.contourArea(smile_pts)
            mouth_area = cv2.contourArea(np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(48, 67)]))
            smile_intensity = smile_area / mouth_area
            return smile_intensity
    # 如果没有检测到人脸或者嘴巴，返回 None
    return 0

# # 检测头部姿态
def detect_head_pose(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 使用 dlib 人脸检测器检测人脸
    rects = detector(gray, 0)
    for rect in rects:
        # 使用 dlib 姿态估计器获取关键点坐标
        landmarks = predictor(gray, rect)
        landmarks_array = np.array([(p.x, p.y) for p in landmarks.parts()])
        # 计算偏转角度
        xp = [p[0]-rect.center().x for p in landmarks_array]
        yp = [rect.center().y-p[1] for p in landmarks_array]
        xv = np.array([xp, yp])
        covar = np.cov(xv)
        evals, evecs = np.linalg.eig(covar)
        sort_indices = np.argsort(evals)[::-1]
        xvec, yvec = evecs[:, sort_indices[0]]
        angle = np.degrees(np.arctan2(yvec, xvec))
        # 将欧拉角返回
        return angle + 100
    return None


def update(ui):
        frame = update_label(ui)
        # 检测眼睛
        left_eye_ratio, right_eye_ratio = detect_eyes(frame)
        update_eye_data(left_eye_ratio, right_eye_ratio, ui)

        #smile
        mouth_aspect_ratio = detect_smile(frame)
        update_smile_data(mouth_aspect_ratio, ui)

        #head
        angle = detect_head_pose(frame)
        update_head_data(angle=angle, ui=ui)

        #mouth
        mouth_h, ratio = detect_mouth(frame)
        update_mouth_data(mouth_h, ratio, ui)


def update_label(ui):
    ret, frame = ui.cap.read()
    if ret:
        # 将彩色图像转换为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 使用 dlib 的人脸检测器检测人脸
        faces = detector(gray, 0)
        for face in faces:
            # 获取人脸位置信息
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            # 绘制矩形框
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 转换为 QImage 格式
        q_image = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QtGui.QImage.Format_BGR888)
        ui.label.setPixmap(QtGui.QPixmap.fromImage(q_image))
    return frame

# eye
def update_eye_data(y1, y2, ui):
    ui.plot1_x += 1

    ui.plot1_y1[:-1] = ui.plot1_y1[1:]
    ui.plot1_y2[:-1] = ui.plot1_y2[1:]
    ui.plot1_y1[-1] = y1
    ui.plot1_y2[-1] = y2

    # 更新曲线
    ui.plot1_curve1.setData(x=ui.plot1_x, y=ui.plot1_y1)
    ui.plot1_curve2.setData(x=ui.plot1_x, y=ui.plot1_y2)

# smile
def update_smile_data(y1, ui):
    ui.plot4_x += 1

    ui.plot4_y1[:-1] = ui.plot4_y1[1:]
    ui.plot4_y1[-1] = y1
    ui.plot4_y2[:-1] = ui.plot4_y2[1:]
    ui.plot4_y2[-1] = 0.15
    # 更新曲线
    ui.plot4_curve1.setData(x=ui.plot1_x, y=ui.plot4_y1)
    ui.plot4_curve2.setData(x=ui.plot1_x, y=ui.plot4_y2)

def update_head_data(angle, ui):
    ui.plot5_x += 1
    ui.plot5_y1[:-1] = ui.plot5_y1[1:]
    ui.plot5_y1[-1] = angle

    # 更新曲线
    ui.plot5_curve1.setData(x=ui.plot5_x, y=ui.plot5_y1)


def update_mouth_data(mouth_h, mouth_w, ui):
    ui.plot3_x += 1
    ui.plot3_y1[:-1] = ui.plot3_y1[1:]
    ui.plot3_y1[-1] = mouth_h
    ui.plot3_y2[:-1] = ui.plot3_y2[1:]
    ui.plot3_y2[-1] = mouth_w

    # 更新曲线
    ui.plot3_curve1.setData(x=ui.plot3_x, y=ui.plot3_y1)
    ui.plot3_curve2.setData(x=ui.plot3_x, y=ui.plot3_y2)