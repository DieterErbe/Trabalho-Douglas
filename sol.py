import cv2

img = cv2.imread("sol.jpg", cv2.IMREAD_COLOR)

enhance = cv2.detailEnhance(img)

cv2.imshow('teste', enhance)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("sol_result.jpg", enhance)
