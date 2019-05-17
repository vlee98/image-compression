import numpy as np
from skimage import io, img_as_ubyte, img_as_float32, color
import matplotlib.pyplot as plt
import sys

def frequency(image):
    grayscale = color.rgb2gray(image)
    ret = np.fft.fft2(grayscale)
    ret = abs(np.log(np.fft.fftshift(ret)))
    return ret

if __name__ == "__main__": 
    image_path = None
    try:
        image_path = sys.argv[1]
    except:
        print ("Error Image Path Invalid")
    image = io.imread(image_path)
    frequency_image = frequency(image)
    plt.imshow(frequency_image, cmap = plt.get_cmap(name='gray'))
    plt.show()
