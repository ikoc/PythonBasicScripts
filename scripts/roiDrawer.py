import cv2
import json
import sys
import os

points = {
  "lPoints":[],
  "mPoints":[],
  "rPoints":[]
}

def click_event(event, x, y, flags, params):
    global scale_percent,img
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
      color = (255,0,0) 
      name = "lPoints"

    # checking for mid mouse clicks     
    if event==cv2.EVENT_MBUTTONDOWN:
      color = (0,0,255) 
      name = "mPoints"
    
    # checking for right mouse clicks     
    if event==cv2.EVENT_RBUTTONDOWN: 
      color = (0,255,0) 
      name = "rPoints"

    if event==cv2.EVENT_LBUTTONDOWN or event==cv2.EVENT_MBUTTONDOWN or event==cv2.EVENT_RBUTTONDOWN: 
      font = cv2.FONT_HERSHEY_SIMPLEX
      x_label = int(x / scale_percent)
      y_label = int(y / scale_percent)
      points[name].append({"x":x_label,"y":y_label})

      cv2.putText(img, f"{x_label},{y_label}", 
                  (x,y), font,
                  1,color, 2)
      radius = 3 
      thickness = 3  
      img = cv2.circle(img, (x,y), radius, color, thickness)

      cv2.imshow('image', img)
      cv2.imwrite('roi_image.jpg', img)
      with open("roi.json", "w") as data_file:
        json.dump(points, data_file, indent=4)
  
# driver function
if __name__=="__main__":


    path = sys.argv[1]
    ext = os.path.splitext(path)[1]

    # Create image
    if ext.lower() in ["jpg","jpeg","png"]:
      img = cv2.imread(path)
    elif  ext.lower() in ["avi","ts","mp4"]:
      video = "D:\\videos\\zorlu\\metroGiris.mp4"
      cap = cv2.VideoCapture(video)
      ret,img = cap.read()
    cv2.imwrite('orj_image.jpg', img)

    #percent by which the image is resized
    scale_percent = 50/100
    #calculate the 50 percent of original dimensions
    width = int(img.shape[1] * scale_percent)
    height = int(img.shape[0] * scale_percent)
    # dsize
    dsize = (width, height)
    # resize image
    img = cv2.resize(img, dsize)

    # displaying the image
    cv2.imshow('image', img)
    # setting mouse hadler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
    # close the window
    cv2.destroyAllWindows()