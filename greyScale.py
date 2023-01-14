import cv2
 
# Load the input image
image = cv2.imread('desktop.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)
 
# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('desktop_grey.jpg',gray_image)