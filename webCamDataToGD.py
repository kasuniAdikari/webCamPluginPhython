# import libraries
import time

import cv2
import os
import datetime

from googleapiclient.http import MediaFileUpload
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

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
print('created folder: ' + date_time)

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

####
gauth = GoogleAuth()

# Creates local webserver and auto handles authentication.
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

# vid_name = date_time + '.avi'
#
# for vid_name in os.listdir(filepath):
#     f = drive.CreateFile({'title': vid_name})
#     f.SetContentFile(os.path.join(filepath, vid_name))
#     f.Upload()
#
# for date_time in os.listdir(image_location):
#     f = drive.CreateFile({'title': date_time})
#     f.SetContentFile(os.path.join(image_location, date_time))
#     f.Upload()

# time.sleep(3)
# os.remove(file_location_name)

# folder_id = '1fSu1Ca8N-xagYnQG1evMR160l9h2YRfh'
# file_metadata = {
#     'name': 'photo.jpg',
#     'parents': [folder_id]
# }
# media = MediaFileUpload('files/photo.jpg', mimetype='image/jpeg',resumable=True)
# file = drive.files().create(body=file_metadata,media_body=media,fields='id').execute()
# print('File ID: %s' % file.get('id'))
