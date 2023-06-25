from skimage.metrics import peak_signal_noise_ratio as psnr
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from PIL import Image

psnr_arr = []

path1 = 'imgs/pic_group/Origin_Image/'
path2 = 'imgs/pic_group/Out_Image/'

Origin_Image_list = [Image.open(path1 + fn) for fn in listdir(path1) if fn.endswith('.jpg')]
Out_Image_list = [Image.open(path2 + fn) for fn in listdir(path2) if fn.endswith('.jpg')]

for i in range(len(Out_Image_list)):
    # psnr_t = psnr(Origin_Image_list[i],Out_Image_list[i])
    # print(np.uint8(Origin_Image_list[i]).shape)
    # print((np.uint8(Out_Image_list[i])).shape)
    psnr_t = psnr(np.uint8(Origin_Image_list[i]), np.uint8(Origin_Image_list[i]))
    print(i,'psnr:', psnr_t)
    psnr_arr.append(psnr_t)

    plt.clf()
    fig = plt.gcf()
    plt.subplot(1, 2, 1)
    plt.title("Origin Image")
    plt.axis("off")
    plt.imshow(Origin_Image_list[i])
    plt.text(14, 33, ' PSNR:' + str(psnr_arr[i]),
             bbox=dict(facecolor='yellow', alpha=0.5), fontsize=15)

    plt.subplot(1, 2, 2)
    plt.title("Out Image")
    plt.axis("off")
    plt.imshow(Out_Image_list[i])

    #fig.savefig("./imgs/pic_group/Image_psnr/psnr_{}.jpg".format(i))
    plt.pause(0.2)

print('psnr_average:', np.average(np.array(psnr_arr)))