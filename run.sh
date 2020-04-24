#!/bin/bash
/usr/bin/python ./ip_simulation.py

### sleeping for 3 seconds for program to initialise camera sream.
sleep 3

### Open IP simulated camera to use gstreamer

ffplay rtsp://127.0.0.1:3005/test  