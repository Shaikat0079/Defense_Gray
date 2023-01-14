import cv2
from skimage import metrics


ref_img = cv2.imread("desktop_grey.jpg")
img1 = cv2.imread("noisedesktop_grey.jpg")
img2 = cv2.imread("desktop_average_grey.jpg")
img3 = cv2.imread("desktop_bilateral_grey.jpg")
img4 = cv2.imread("desktop_gaussian_grey.jpg")
img5 = cv2.imread("desktop_median_grey.jpg")


# Mean square error

mse_skimg1 = metrics.mean_squared_error(ref_img, img1)
print("MSE: based on scikit-image = ", mse_skimg1)
mse_skimg2 = metrics.mean_squared_error(ref_img, img2)
print("MSE: based on scikit-image Average_Filtering = ", mse_skimg2)
mse_skimg3 = metrics.mean_squared_error(ref_img, img3)
print("MSE: based on scikit-image Bilateral_Filtering = ", mse_skimg3)
mse_skimg4 = metrics.mean_squared_error(ref_img, img4)
print("MSE: based on scikit-image Gaussian_Filtering = ", mse_skimg4)
mse_skimg5 = metrics.mean_squared_error(ref_img, img5)
print("MSE: based on scikit-image Median_Filtering = ", mse_skimg5)
# mse_skimg6 = metrics.mean_squared_error(ref_img, ref_img)
# print("MSE: based on scikit-image No_Filtering = ", mse_skimg6)



print('=======================================================')
print('=======================================================')

# Peak Signal Noise Ratio

psnr_skimg1 = metrics.peak_signal_noise_ratio(ref_img, img1)
print("PSNR: based on scikit-image = ", psnr_skimg1)
psnr_skimg2 = metrics.peak_signal_noise_ratio(ref_img, img2)
print("PSNR: based on scikit-image Average_Filtering= ", psnr_skimg2)
psnr_skimg3 = metrics.peak_signal_noise_ratio(ref_img, img3)
print("PSNR: based on scikit-image Bilateral_Filtering= ", psnr_skimg3)
psnr_skimg4 = metrics.peak_signal_noise_ratio(ref_img, img4)
print("PSNR: based on scikit-image Gaussian_Filtering= ", psnr_skimg4)
psnr_skimg5 = metrics.peak_signal_noise_ratio(ref_img, img5)
print("PSNR: based on scikit-image Median_Filtering= ", psnr_skimg5)



print('=======================================================')
print('=======================================================')

# Normalized Root Mean Square Error

nrmse_skimg1 = metrics.normalized_root_mse(ref_img, img1)
print("NRMSE: based on scikit-image = ", nrmse_skimg1)
nrmse_skimg2 = metrics.normalized_root_mse(ref_img, img2)
print("NRMSE: based on scikit-image Average_Filtering= ", nrmse_skimg2)
nrmse_skimg3 = metrics.normalized_root_mse(ref_img, img3)
print("NRMSE: based on scikit-image Bilateral_Filtering= ", nrmse_skimg3)
nrmse_skimg4 = metrics.normalized_root_mse(ref_img, img4)
print("NRMSE: based on scikit-image Gaussian_Filtering= ", nrmse_skimg4)
nrmse_skimg5 = metrics.normalized_root_mse(ref_img, img5)
print("NRMSE: based on scikit-image Median_Filtering= ", nrmse_skimg5)


# Here I've Added the output of the First iteration

""" 
MSE: based on scikit-image =  1769.0283162182416
MSE: based on scikit-image Average_Filtering =  140.2591137371866
MSE: based on scikit-image Bilateral_Filtering =  1143.208646762457
MSE: based on scikit-image Gaussian_Filtering =  195.90406260153762
MSE: based on scikit-image Median_Filtering =  169.3486681050069
=======================================================
=======================================================
=======================================================
=======================================================
PSNR: based on scikit-image =  15.653455763025013
PSNR: based on scikit-image Average_Filtering=  26.661492704964015
PSNR: based on scikit-image Bilateral_Filtering=  17.549548602468057
PSNR: based on scikit-image Gaussian_Filtering=  25.2103691850699
PSNR: based on scikit-image Median_Filtering=  25.842985755171437
=======================================================
=======================================================
=======================================================
=======================================================
NRMSE: based on scikit-image =  0.3671153695255656
NRMSE: based on scikit-image Average_Filtering=  0.10337147656544632
NRMSE: based on scikit-image Bilateral_Filtering=  0.29511951257858127
NRMSE: based on scikit-image Gaussian_Filtering=  0.12216784012519216
NRMSE: based on scikit-image Median_Filtering=  0.11358632991694333

"""


print("=======================================================")
print("=======================================================")
print("2nd Iteration")

print("=======================================================")
print("=======================================================")
img6 = cv2.imread("noisedesktop2_grey.jpg")
img7 = cv2.imread("desktop_average2_grey.jpg")
img8 = cv2.imread("desktop_bilateral2_grey.jpg")
img9 = cv2.imread("desktop_gaussian2_grey.jpg")
img10 = cv2.imread("desktop_median2_grey.jpg")


# Mean square error

mse_skimg6 = metrics.mean_squared_error(ref_img, img6)
print("MSE: based on scikit-image = ", mse_skimg6)
mse_skimg7 = metrics.mean_squared_error(ref_img, img7)
print("MSE: based on scikit-image Average_Filtering = ", mse_skimg7)
mse_skimg8 = metrics.mean_squared_error(ref_img, img8)
print("MSE: based on scikit-image Bilateral_Filtering = ", mse_skimg8)
mse_skimg9 = metrics.mean_squared_error(ref_img, img9)
print("MSE: based on scikit-image Gaussian_Filtering = ", mse_skimg9)
mse_skimg10 = metrics.mean_squared_error(ref_img, img10)
print("MSE: based on scikit-image Median_Filtering = ", mse_skimg10)
# mse_skimg6 = metrics.mean_squared_error(ref_img, ref_img)
# print("MSE: based on scikit-image No_Filtering = ", mse_skimg6)


print('=======================================================')
print('=======================================================')

# Peak Signal Noise Ratio

psnr_skimg6 = metrics.peak_signal_noise_ratio(ref_img, img6)
print("PSNR: based on scikit-image = ", psnr_skimg6)
psnr_skimg7 = metrics.peak_signal_noise_ratio(ref_img, img7)
print("PSNR: based on scikit-image Average_Filtering= ", psnr_skimg7)
psnr_skimg8 = metrics.peak_signal_noise_ratio(ref_img, img8)
print("PSNR: based on scikit-image Bilateral_Filtering= ", psnr_skimg8)
psnr_skimg9 = metrics.peak_signal_noise_ratio(ref_img, img9)
print("PSNR: based on scikit-image Gaussian_Filtering= ", psnr_skimg9)
psnr_skimg10 = metrics.peak_signal_noise_ratio(ref_img, img10)
print("PSNR: based on scikit-image Median_Filtering= ", psnr_skimg10)


print('=======================================================')
print('=======================================================')

# Normalized Root Mean Square Error

nrmse_skimg6 = metrics.normalized_root_mse(ref_img, img6)
print("NRMSE: based on scikit-image = ", nrmse_skimg6)
nrmse_skimg7 = metrics.normalized_root_mse(ref_img, img7)
print("NRMSE: based on scikit-image Average_Filtering= ", nrmse_skimg7)
nrmse_skimg8 = metrics.normalized_root_mse(ref_img, img8)
print("NRMSE: based on scikit-image Bilateral_Filtering= ", nrmse_skimg8)
nrmse_skimg9 = metrics.normalized_root_mse(ref_img, img9)
print("NRMSE: based on scikit-image Gaussian_Filtering= ", nrmse_skimg9)
nrmse_skimg10 = metrics.normalized_root_mse(ref_img, img10)
print("NRMSE: based on scikit-image Median_Filtering= ", nrmse_skimg10)

# Here I've Added the output of the Second iteration

"""
2nd Iteration
=======================================================
=======================================================
=======================================================
=======================================================
MSE: based on scikit-image =  191.21327851503543
MSE: based on scikit-image Average_Filtering =  14.440480865729288
MSE: based on scikit-image Bilateral_Filtering =  27.401213407156632
MSE: based on scikit-image Gaussian_Filtering =  17.766743797034838
MSE: based on scikit-image Median_Filtering =  11.157250391083556
=======================================================
=======================================================
=======================================================
=======================================================
PSNR: based on scikit-image =  25.315623129614572
PSNR: based on scikit-image Average_Filtering=  36.534987054559245
PSNR: based on scikit-image Bilateral_Filtering=  33.753105657714556
PSNR: based on scikit-image Gaussian_Filtering=  35.634725211639704
PSNR: based on scikit-image Median_Filtering=  37.655231812404104
=======================================================
=======================================================
=======================================================
=======================================================
NRMSE: based on scikit-image =  0.12069636719167098
NRMSE: based on scikit-image Average_Filtering=  0.03316851304003846
NRMSE: based on scikit-image Bilateral_Filtering=  0.045689885759757395
NRMSE: based on scikit-image Gaussian_Filtering=  0.036790788394015145
NRMSE: based on scikit-image Median_Filtering=  0.029155048246486397
"""
