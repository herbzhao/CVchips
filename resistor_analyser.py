import cv2
import numpy as np
from matplotlib import pyplot as plt


def resistor_analyse():
    img = cv2.imread(r'resources\resistor.png')
    #img = cv2.imread("resistor2.jpg")
    #img = cv2.imread("resistor-sample.jpg")

    #kernel = np.ones((5,5),np.float32)/25
    #img = cv2.filter2D(img,-1,kernel)


    ORANGE_MIN = np.array([5, 130, 150],np.uint8)
    ORANGE_MAX = np.array([15, 255, 225],np.uint8)

    BROWN_MIN = np.array([2, 25, 25],np.uint8)
    BROWN_MAX = np.array([12, 255, 100],np.uint8)

    RED1_MIN = np.array([0, 100, 100],np.uint8)
    RED1_MAX = np.array([2, 255, 255],np.uint8)

    RED2_MIN = np.array([160, 100, 120],np.uint8)
    RED2_MAX = np.array([179, 255, 255],np.uint8)

    YELLOW_MIN = np.array([25, 120, 130],np.uint8)
    YELLOW_MAX = np.array([48, 255, 255],np.uint8)

    GREEN_MIN = np.array([48, 100, 50],np.uint8)
    GREEN_MAX = np.array([78, 255, 255],np.uint8)

    BLUE_MIN = np.array([98, 60, 90],np.uint8)
    BLUE_MAX = np.array([124, 255, 255],np.uint8)

    PURPLE_MIN = np.array([130, 50, 60],np.uint8)
    PURPLE_MAX = np.array([170, 255, 255],np.uint8)

    GREY_MIN = np.array([0, 20, 55],np.uint8)
    GREY_MAX = np.array([180, 40, 130],np.uint8)

    BLACK_MIN = np.array([0, 0, 0],np.uint8)
    BLACK_MAX = np.array([30, 30, 30],np.uint8)

    MIN = [ORANGE_MIN,BROWN_MIN,RED1_MIN,RED2_MIN,YELLOW_MIN,GREEN_MIN,BLUE_MIN,PURPLE_MIN,GREY_MIN,BLACK_MIN]
    MAX = [ORANGE_MAX,BROWN_MAX,RED1_MAX,RED2_MAX,YELLOW_MAX,GREEN_MAX,BLUE_MAX,PURPLE_MAX,GREY_MAX,BLACK_MAX]
    colours = ["orange","brown","red","red","yellow","green","blue","purple","grey","black"]
    present = [0,0,0,0,0,0,0,0,0,0]
    position_y =[0,0,0,0,0,0,0,0,0,0]
    boundaries = [MIN,MAX]
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for i in range (0,10):
        frame_threshed = cv2.inRange(hsv_img, MIN[i], MAX[i])
        present[i]=np.mean(frame_threshed)
        position = (np.mean(np.nonzero(frame_threshed),axis=1))
    #position = (np.array(position))
        position_y[i]=(position[1])
        output = cv2.bitwise_and(img, img, mask = frame_threshed)
    # cv2.imshow("mask",output)
    # cv2.waitKey(0)
    filtered=np.where(present>np.mean(present))
    filtered = ((np.array(filtered)))
    pos=np.zeros([len(filtered[0]),])
    #print(filtered[0])
    for i in range(0,len(filtered[0])):
        pos[i]=position_y[int(filtered[0][i])]
        #print(colours[int(filtered[0][i])])
    #  print(position_y[int(filtered[0][i])])
    #print(pos)
    sorted_y = (np.argsort(pos))
    colour_output = []
    for i in range(0,len(filtered[0])):
        print(colours[filtered[0][sorted_y[i]]])
        colour_output.append(colours[filtered[0][sorted_y[i]]])
    kernel = np.ones((5,5),np.float32)/25
    output = cv2.filter2D(output,-1,kernel)
    #cv2.circle(frame_threshed,np.round(position), 63, (0,0,255), -1)
    vis = np.concatenate((img, output), axis=0)

    cv2.imshow("images", vis)
    cv2.waitKey(0)

    return colour_output


