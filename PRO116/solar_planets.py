import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
             "Sol",
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
             "Mercurio",
             (110,250),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
             "Venus",
             (200,170),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
             "Tierra",
             (280,260),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
             "Marte",
             (380,170),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )
             
cv2.putText(img,
             "Júpiter",
             (550,70),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
             "Saturno",
             (750,330),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
             "Urano",
             (960,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
             "Neptuno",
             (1130,140),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.imshow("Output",img)

cv2.waitKey(0)