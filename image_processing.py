import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import exposure

def image_process(input_image_location, processed_image_location):
    min_max = [[50,100],[100,255],[250,300],[350,400],[390,400],[450,460]]
    contrast = [[10,250],[50,250],[50,250],[50,250],[120,250],[120,250]]

    img = cv2.imread(input_image_location, 0)
    thresh_list = []
    contrast_images = []

    # min max thrsholding
    for i in range(len(min_max)):
        ret,thresh = cv2.threshold(img,min_max[i][0],min_max[i][1],cv2.THRESH_TRUNC)
        thresh_list.append(thresh)
        contrast_images.append(exposure.rescale_intensity(thresh_list[i], in_range=(contrast[i][0],contrast[i][1])))

    images = [img]
    for i in range(len(contrast_images)):
        images.append(contrast_images[i])


    for i in range(len(images)):
        plt.subplot(3,3,i+1)
        plt.imshow(images[i],'gray')
        plt.subplot
        plt.xticks([]),plt.yticks([])


    plt.show()

    plt.axis('off')
    save_image_choice = input('which one have more clear text? [i.e. 3] ')
    save_image_choice = int(save_image_choice) - 1
    processed_image = images[save_image_choice]
    plt.imshow(processed_image,'gray')
    processed_image_location = processed_image_location.replace('.png','')
    plt.savefig(processed_image_location)
    
    return processed_image

