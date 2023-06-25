# 一、运行环境
>## 相关依赖包
>>### numpy 3.4.8 
>>### cv2  3.4.8
>## 编辑环境
>>### pycharm
>>### python 3.8

# 二、 输入
>## 输入一组图片
![](https://fastly.jsdelivr.net/gh/GreyHuu/image@main/image/1663768745118571c9b7d351949b338118ac9d63899d.jpg)
>## 在TrainDatabase中匹配人脸
![](https://fastly.jsdelivr.net/gh/GreyHuu/image@main/image/1663768758118939b601318d389fbe7615ba27c74721.jpg)
>## 相关计算
>> 关于 A.T * A 和 A * A.T 的结果都是对称矩阵，对他们的特征值分解得到A的奇异值分解。
> 需要做一次特征值和特征向量的计算，然后通过矩阵A与特征向量相乘确定U即“特征脸”的投影
>>[奇异值分解](https://zhuanlan.zhihu.com/p/152756312/)
# 三、  输出
>## 调整参数PCA_NUM，计算正确率