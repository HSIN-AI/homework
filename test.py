import cv2
import numpy as np


def gaussian_noise(image,mean,sigma):
    noise = np.random.normal,sigma,image.shape)
    noise_img= clip(img + noise,0,255).astype('uint8')
    return noise_img

mean = 0
sigma = 30
img = cv2.imread('idle.jpg', cv2.IMREAD_GRAYSCALE)
noisy = gaussian_noise(img,mean,sigma)
cv2.imshow('Gaussian Noise',noisy)
cv2.waitkey(0)
cv2.destroyAllWindows
    
