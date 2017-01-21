from pylab import *
import numpy as np
import scipy as sp
from scipy.ndimage import imread
from scipy.misc import imsave
from scipy.signal import convolve2d as conv
import time

def convolve(image, kernel):
    '''
    convolves image using filter
    '''
    
    new_image = np.zeros(image.shape)
    
    # filter size (assuming filter is nxn)
    k = kernel.shape[0]/2
    # flip the filter in both dimensions to apply correlation
    kernel = np.fliplr(np.flipud(kernel))
    
    # go through each point in image
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            
            # begin to end coords of the new patch
            x1, y1, x2, y2 = x-k, y-k, (x+k)+1, (y+k)+1
            
            # get existing patch
            patch = image[max(0, y1):min(image.shape[0], y2),
                          max(0, x1):min(image.shape[1], x2)]
            
            # handle borders by padding with 0s
            
            padded = np.pad(patch, ((abs(min(0, y1)),
                                     abs(min(0, image.shape[0]-y2))),
                                    (abs(min(0, x1)),
                                     abs(min(0, image.shape[1]-x2)))),
                                    'constant', constant_values=0) 
            
            # calculate new intensity of point
            new_image[y, x] = np.sum(padded * kernel)
            
    return new_image

def convolve2(image, kernel):
    '''
    convolves image using filter.
    Improved by adding vector dot 
    '''
    
    new_image = np.zeros(image.shape)
    
    # filter size (assuming filter is nxn)
    k = kernel.shape[0]/2
    # flip the filter in both dimensions and reshape to a 1D
    kernel = np.fliplr(np.flipud(kernel)).reshape((kernel.size,))
    
    # go through each point in image
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            
            # begin to end coords of the new patch
            x1, y1, x2, y2 = x-k, y-k, (x+k)+1, (y+k)+1
            
            # get existing patch
            patch = image[max(0, y1):min(image.shape[0], y2),
                          max(0, x1):min(image.shape[1], x2)]
            
            # handle borders by padding with 0s
            
            padded = np.pad(patch, ((abs(min(0, y1)),
                                     abs(min(0, image.shape[0]-y2))),
                                    (abs(min(0, x1)),
                                     abs(min(0, image.shape[1]-x2)))),
                                    'constant', constant_values=0).reshape((kernel.size,))  
            
            # calculate new intensity through dot product
            new_image[y, x] = np.dot(kernel, padded)
            
    return new_image


    
if __name__ == "__main__":
    image = imread("cat.jpg", mode='L')
    #image = np.random.random_integers(0, 255, (5,5))
    #imsave("example.jpg", image)

    kernel = np.array([[-1,-2,-1],
                      [0,0,0],
                      [1,2,1]], dtype='float') /16
    
    start = time.time()
    result = convolve(image, kernel)
    end = time.time()
    imsave("example.jpg", result)
    print("Convolve1: It took " + str(end-start) + "s to convolve.")
    print(result)
    
    start = time.time()
    result = convolve2(image, kernel)
    end = time.time()
    imsave("example_second.jpg", result)
    print("Convolve2: It took " + str(end-start) + "s to convolve.")
    print(result)
    
    start = time.time()
    result = conv(image, kernel, mode='same', boundary = 'fill', fillvalue = 0)
    end = time.time()
    imsave("example_scipy.jpg", result)
    print("ScipyConvolve2d: It took " + str(end-start) + "s to convolve.")
    
    '''
    result = conv(image, kernel, 'same')
    print (result)
    imsave("example_gaussian2.jpg", result)   
    '''
