import cv2
import numpy as np

# read input image
img = cv2.imread('Programas Clase 2022-[1 2]/Algoritmos AD/leaf1.jpg')

print(img)
print(type(img))
print(img.shape)


# define transformation matrix
#m = np.ones((3,3))
#m = np.identity(3)
m1 = np.array([[1, 0, 0],[0, 0, 0],[0, 0, 0]])
m2 = np.array([[0, 0, 0],[0, 0, 0],[0, 0, 1]])

# apply the cv2.transform to perform matrix transformation
img_tr = cv2.transform(img, m1, None)
img_tr2 = np.zeros(img.shape, dtype=np.uint8)

for i, x in enumerate(img):
    for j, y in enumerate(x):
        #print(img.shape, img.dtype)
        #print(m.shape, m.dtype)
        tempo = img[i, j, : ]
        #print(tempo.shape,  tempo.dtype)
        #print(tempo)
        #print(m)
        temporal = m2 @ tempo 
        temporal = temporal.astype(np.uint8)
        #print(temporal)
        #print(temporal.shape,  temporal.dtype)
        img_tr2[i, j, : ] = temporal
print("Las de ultimo temporal")
print(temporal)
print(type(temporal))
print(temporal.shape)


print("Las de img")
print(img_tr)
print(type(img_tr))
print(img_tr.shape)

print("Las de img2")
print(img_tr2)
print(type(img_tr2))
print(img_tr2.shape)

print(img_tr2[465, 699, 1])
print(img_tr[465, 699, 1])
print(type(img_tr2[465, 699, 1]))
print(type(img_tr[465, 699, 1]))

# display the transformed image

#cv2.waitKey(0)
cv2.imshow("Transformed Image", img_tr2)
cv2.waitKey(0)
cv2.imshow("Transformed Image", img_tr)
cv2.waitKey(0)
cv2.destroyAllWindows()