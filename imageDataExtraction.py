import os
import time

# Path to the file/directory
path = r"E:/L4S1/research/Develop/OutputImg/1623953841.196087/1623953841.196087_39.jpg"

# Both the variables would contain time
# elapsed since EPOCH in float
ti_c = os.path.getctime(path)
# ti_m = os.path.getmtime(path)
file_size = os.path.getsize(path)

# Converting the time in seconds to a timestamp
c_ti = time.ctime(ti_c)
# m_ti = time.ctime(ti_m)

print(f"The file located at the path {path} was created at {c_ti} ")
print("File Size is :", file_size / 1024, 'KB')
