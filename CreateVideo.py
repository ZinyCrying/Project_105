import cv2
import os

path = "./Images/"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in [".gif", ".png", ".jpg", ".jpeg"]:
        file_name = path + '/' + file
        #print(file_name)
        
        images.append(path)

count = len(images)

frame = cv2.imread(images[0])
print(images[0])
print(frame)

width, height, channels = frame.shape

size = (width, height)
#print(size)

out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*"DVIX"), 0.8, size)

for i in range(0, count-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()

print("Done") 
