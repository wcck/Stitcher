import cv2

stitcher = cv2.createStitcher(False)
left_img = cv2.imread("./images/1.JPG")
center_img = cv2.imread("./images/2.JPG")
right_img1 = cv2.imread("./images/3.JPG")
right_img2 = cv2.imread("./images/4.JPG")
result = stitcher.stitch((left_img, center_img, right_img1, right_img2))

cv2.imwrite("./output/easy_result.jpg", result[1])
