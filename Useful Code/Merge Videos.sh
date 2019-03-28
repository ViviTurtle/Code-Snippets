# This script is is used to contatenate all GoPro Videos within the same directory.
# See https://trac.ffmpeg.org/wiki/Concatenate
# Requirement brew install ffmpeg
for f in ./*.MP4; do echo "file '$f'" >> mylist.txt; done
read -p "Press [Enter] key to merge..."
ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4
