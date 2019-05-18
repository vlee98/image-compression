import numpy as np
from skimage import io, img_as_ubyte, img_as_float32, color
import matplotlib.pyplot as plt
import sys

def frequency(image, percentage):
    # convert to grayscale
    #grayscale = color.rgb2gray(image)
    grayscale = image
    # frequencies of the image
    f_transform = np.fft.fft2(grayscale)
    
    # this is just to display magnitude
    f_shift = np.fft.fftshift(f_transform) 
    magnitude = np.log(np.abs(f_shift))

    max_element = max(map(max,abs(f_transform)))
    # threshold
    mask = abs(f_transform) <= max_element * percentage
    
    
    # Stats, counting removals is slo
    """
    removals = sum(map(sum,mask))
    x, y = f_transform.shape 
    count = x * y
    print ("Shape :" , f_transform.shape)
    print ("Removed :", removals)
    print ("Percent Left : ", (count - removals) / count)
    """
    # "Compress" as in remove the pixels below threshold
    f_transform[mask] = 0
    ret = abs(np.fft.ifft2(f_transform))
    return ret, grayscale, magnitude

if __name__ == "__main__": 
    if (len(sys.argv) !=3):
        print ("Use Statement: file path and threshold percentage \nExample: python frequency.py data/rose.jpg .0001")
        sys.exit(1)
    image_path = None
    try:
        image_path = sys.argv[1]
        float(sys.argv[2])
    except:
        print ("Error Use Statement: file path and threshold percentage \nExample: python frequency.py data/rose.jpg .0001")
        sys.exit(1)
    image = io.imread(image_path)
    figure = plt.figure()
    frequency_image = [[],[],[]]; 
    frequency_image[0], grayscale, magnitude = frequency(image[:,:,0], float(sys.argv[2]))
    frequency_image[1], grayscale, magnitude = frequency(image[:,:,1], float(sys.argv[2]))
    frequency_image[2], grayscale, magnitude = frequency(image[:,:,2], float(sys.argv[2]))
    frequency_image = np.stack(frequency_image, axis=2)
    io.imsave('results/filtered.jpg', frequency_image)
    io.imsave('results/grayscale.jpg', grayscale)
    io.imsave('results/magnitude.jpg', magnitude)
