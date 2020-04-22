# GStreamer-Python

This project helps in fetching continous live RTSP stream using GStreamer, Python and numpy without compromising on stream quality. 

**multiprocessing** is used in python to avoid main thread getting stuck.

## Getting Started

Just clone this Repo then in main_prg.py add your rtsp stream on below line:

```python
self.camlink = '' #Add your RTSP cam link
```

### Prerequisites

1. Python 3
2. GStreamer
3. OpenCV (if you want to run this example as is)
4. Numpy

##### 1. Python 3 Installation
```
brew install python
```
##### 2. GStreamer Installation
You will need GStreamer. Installation instruction can be found on this link [GStreamer](https://gstreamer.freedesktop.org/download/)
Still for your quick reference will list installation instruction for Ubuntu:

```
brew install gstreamer gst-plugins-good gst-plugins-bad gst-rtsp-server
```

##### 3. OpenCV Installation
There are various way to install OpenCV but example using (Conda, PIP or build from source). But for purpose of this project below is instruction using PIP

```
python3 -m pip install opencv-python –user --upgrade
```

##### 4. Numpy Installation
```
python3 -m pip install numpy  –user --upgrade

```

##### Testing the installations
Open the terminal and type `python`

```
>>> import cv2
>>> cap = cv2.VideoCapture(0)
>>> cap.read()
>>> exit()
```
#### Running the program

Post cloning the Repo, go to repo dir (Also include cam link in main_prg.py as mentioned above).

```python
python3 ip_simulation.py
```

####After the startup open a new tab in terminal and open ffmpeg
```
ffplay rtsp://127.0.0.1:3005/test
```

### Star the REPO, if you find it useful. Feel free for pull requests.
## CHEERS!!! 


