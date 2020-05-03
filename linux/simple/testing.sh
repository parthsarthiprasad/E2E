#!/bin/bash
#!/bin/bash
current_location=$(pwd)
script_location=$(dirname $0)
# if [ $script_location = '.' ]
# then
#  script_location="$current_location"
# fi
 echo $script_location
 GI_TYPELIB_PATH="${script_location}/../build/girepository-1.0"
 echo $GI_TYPELIB_PATH 
 

python3 ${script_location}/temp.py 