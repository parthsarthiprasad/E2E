#!/bin/bash

sudo apt-get install python

#installing gstreamer libraries 
sudo apt-get build-dep libgstreamer1.0-0 \
   gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
   gstreamer1.0-plugins-ugly gstreamer1.0-plugins-bad

sudo apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

#installing opencv

pip install opencv-contrib-python
pip install numpy


# #installing gstremer missing binaries

# #cheching presence of important binaries , glib library must be present
# ldd --version  

# pip install meson
# pip insall ninja

# ##gtk tool needed since 
# ##https://gitlab.freedesktop.org/libfprint/libfprint/issues/75
# ## needed to install gtk-doc
# sudo apt-get install -y itstool

# ##TODO : paste the gtk tool in biinaries

# cd ../binaries/gtk

# ./configure --prefix=/usr &&
#  make

#  sudo make install

#  ## this installs mako required to use meson build

# cd ../mako

# python3 setup.py install --optimize=1

# ## this install markupsafe required o use meson build, this needs to be
# ## with super user access

# cd ../markupsafe

# python2 setup.py build &&
# python3 setup.py build

# python2 setup.py install --optimize=1 &&
# python3 setup.py install --optimize=1


