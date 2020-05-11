#!/bin/bash

brew install python 
brew install libx264
brew install pygoobject3 ffmpeg
brew install gstreamer gst-plugins-good gst-plugins-bad gst-rtsp-server

python3 -m pip install numpy opencv-python ndl-api pillow --user --upgrade