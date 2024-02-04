import cv2

nPlateCascade = cv2.CascadeClassifier(r"C:\Users\om\Desktop\CV\haarcascade_russian_plate_number.xml")
minArea = 700

# Load the image directly
img = cv2.imread(r"C:\Users\om\Desktop\CV\m.jpg")

res_img = cv2.resize(img, dsize=(0,0), fx= 3 , fy= 3)

imgGray = cv2.cvtColor(res_img, cv2.COLOR_BGR2GRAY)

numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in numberPlates:
    area = w * h
    if area > minArea:
        cv2.rectangle(res_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(res_img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        imgRoi = res_img[y:y + h, x:x + w]
        cv2.imshow("roi", imgRoi)

cv2.imshow("Image", res_img)  # Display the image

cv2.waitKey(0)
cv2.destroyAllWindows()
