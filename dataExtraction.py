import glob
import os
dir_name = 'E:/L4S1/research/Develop/OutputImg/1623953841.196087/'
# Get a list of files (file paths) in the given directory
list_of_files = filter( os.path.isfile,
                        glob.glob(dir_name + '*') )
# get list of ffiles with size
files_with_size = [ (file_path, os.stat(file_path).st_size)
                    for file_path in list_of_files ]
# Iterate over list of tuples i.e. file_paths with size
# and print them one by one
for file_path, file_size in files_with_size:
    print(file_size, ' -->', file_path)