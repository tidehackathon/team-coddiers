import cv2

vidcap = cv2.VideoCapture('testing.mp4')
fps = vidcap.get(cv2.CAP_PROP_FPS)

def getFrame():
 success,image = vidcap.read()
 count = 0
 success = True

 while success:
  success,frame = vidcap.read()
  count+=1
  print("time stamp current frame:",count/fps)
  if count % fps/2 == 0:
   yield frame



