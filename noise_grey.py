from numpy import average


# Import Image from wand.image module
from wand.image import Image

# Read image using Image() function
with Image(filename="desktop_grey.jpg") as img:

    # Generate noise image using spread() function
    # Here it generated poisson noise
    img.noise("poisson", attenuate=0.9)
    img.save(filename="noisedesktop_grey.jpg")


# Read image using Image() function
with Image(filename="desktop_grey.jpg") as img:

    # Generate noise image using spread() function
    # Here it generated laplacian noise
    img.noise("laplacian", attenuate=1.0)
    img.save(filename="noisedesktop2_grey.jpg")


import cv2

img = cv2.imread('noiseDesktop_grey.jpg')

# Apply bilateral filter with d = 15,
sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(img, 15, 75, 75)
# Save the output.
cv2.imwrite('desktop_bilateral_grey.jpg', bilateral)
# Apply Average filter
average = cv2.blur(img, (5, 5))
# Save the output
cv2.imwrite('desktop_average_grey.jpg', average)
# Apply Gaussian Filter
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imwrite('desktop_gaussian_grey.jpg', gaussian)
# Apply Median Filter
median_filter = cv2.medianBlur(img, 5)
cv2.imwrite('desktop_median_grey.jpg', median_filter)

img2 = cv2.imread('noiseDesktop2_grey.jpg')

# Apply bilateral filter with d = 15,
sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(img2, 15, 75, 75)
# Save the output.
cv2.imwrite('desktop_bilateral2_grey.jpg', bilateral)
# Apply Average filter
average = cv2.blur(img2, (5, 5))
# Save the output.
cv2.imwrite('desktop_average2_grey.jpg', average)
# Apply Gaussian Filter
gaussian = cv2.GaussianBlur(img2, (5, 5), 0)
cv2.imwrite('desktop_gaussian2_grey.jpg', gaussian)
# Apply Median Filter
median_filter = cv2.medianBlur(img2, 5)
cv2.imwrite('desktop_median2_grey.jpg', median_filter)
