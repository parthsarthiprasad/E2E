#!/bin/bash

# /usr/bin/python ./ip_simulation.py

# ### sleeping for 3 seconds for program to initialise camera sream.
# sleep 3

# ### Open IP simulated camera to use gstreamer

# ffplay rtsp://127.0.0.1:3005/test  

current_location=$(pwd)
script_location=$(dirname $0)
# if [ $script_location = '.' ]
# then
#  script_location="$current_location"
# fi
 echo $script_location
 GI_TYPELIB_PATH="${script_location}/../build/girepository-1.0"
 echo $GI_TYPELIB_PATH 
 

python3 ${script_location}/ip_simulation.py 
# This is written together to run all tasks together
