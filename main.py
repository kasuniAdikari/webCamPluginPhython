# import libraries
import cv2
import os
import datetime

# Determine filename by timestamp
current_date_and_time = datetime.datetime.now().timestamp()
print('timestamp: ', current_date_and_time)

date_time = str(current_date_and_time)

filepath = 'E:/L4S1/research/Develop/OutputVid/'
file_location_name = filepath + date_time + '.avi'
print('file path name', file_location_name)

# define a video capture object
vid = cv2.VideoCapture(0)

vid_cod = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
videoWriter = cv2.VideoWriter(file_location_name, vid_cod, 30.0, (640, 480))

while (True):

    # Capture the video frame
    ret, frame = vid.read()

    # Display the resulting frame
    ims = cv2.resize(frame, (100, 100))
    cv2.imshow('frame', ims)
    videoWriter.write(frame)

    # the 'q' button is set as the
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()

# close the already opened file
videoWriter.release()

# Destroy all the windows
cv2.destroyAllWindows()

# Opens the Video file
cap = cv2.VideoCapture(file_location_name)
success, image = cap.read()
count = 0
image_location = 'E:/L4S1/research/Develop/OutputImg'
new_image_name = image_location + date_time

# creating directory to save video fragments
path = os.path.join(image_location, date_time)
os.mkdir(path)

currentframe = 0

while (True):

    # reading from frame
    ret, framei = cap.read()

    if ret:
        # if video is still left continue creating images
        name = date_time + '_' + str(currentframe) + '.jpg'
        location = image_location + name
        # print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(os.path.join(path, name), framei)

        currentframe += 1
    else:
        break

# Release all space and windows once done
cap.release()
cv2.destroyAllWindows()
