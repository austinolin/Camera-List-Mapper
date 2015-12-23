#!/usr/bin/env python
from difflib import get_close_matches as gcm;
from pprint import pprint;

# reads camera list and the master camera list (real cameras only) into lists
original_cameras = open('camera_list.txt').readlines();
master_camera_list = open('Real_List_of_Cameras.txt').readlines();

# remove the "\n" newline character from each item in the lists
original_cameras = [camera.strip() for camera in original_cameras];
master_camera_list = [camera.strip() for camera in master_camera_list];

# will remove all identical "cameras"/duplicates from original_cameras
original_cameras = list(set(original_cameras))

# dictionary mapping the original camera to the real camera from the master list
camera_dictionary = {};

# will assign each "camera" in the file with the closest match from the master
# list of cameras.
# will ignore "camera" if no match is found
for camera in original_cameras:
    closest_match = gcm(camera, master_camera_list, n=1, cutoff=.3)
    try:
        camera_dictionary[camera] = closest_match[0];
    except IndexError:
        pass;

# pretty print the mappings
pprint(camera_dictionary);