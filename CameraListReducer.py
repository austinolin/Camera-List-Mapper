#!/usr/bin/env python

# will synchronize many of the lines, reducing the contents of camera_list.txt
# to a smaller file, which I can then filter manually to create a "master list"
# of acceptable predefined camera names

resultsFile = "filtered_cameras_list.txt";

original_cameras = open('camera_list.txt').readlines();
# remove "\n" nextline character, convert roman numerals to numbers, replace "mk"
# with "mark"
original_cameras = [camera.strip() for camera in original_cameras];
original_cameras = [camera.lower() for camera in original_cameras];
original_cameras = [camera.replace("mk", "mark") for camera in original_cameras];
original_cameras = [camera.replace("ii", "2") for camera in original_cameras];
original_cameras = [camera.replace("iii", "3") for camera in original_cameras];
original_cameras = [camera.replace("iv", "4") for camera in original_cameras];

# remove unnecessary common terms, hyphens, spaces to more easily get rid
# of duplicates
original_cameras = [camera.replace("edition", "") for camera in original_cameras];
original_cameras = [camera.replace("-", "") for camera in original_cameras];
original_cameras = [camera.replace("eos", "") for camera in original_cameras];
original_cameras = [camera.replace(" ","") for camera in original_cameras];

# will remove all identical "cameras"/duplicates from original_cameras and
# sort the list
original_cameras = list(set(original_cameras));
original_cameras.sort();


f = open(resultsFile,'w')

for camera in original_cameras:
	f.write(camera + "\n"); 

f.close()
