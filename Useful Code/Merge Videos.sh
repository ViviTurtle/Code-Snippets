# This script is is used to contatenate all GoPro Videos within the same directory.
# See https://trac.ffmpeg.org/wiki/Concatenate
# Requirement brew install ffmpeg
echo "The following files will be merged in this order:"
rm mylist.txt
for f in ./*.MP4; do echo "file '$f'" >> mylist.txt && echo $f; done
read -p "Press [Enter] key to merge..."
ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4
ffmpeg -i output.mp4 -pix_fmt yuv420p -c:v libx264 -crf 18 -vf "frei0r=defish0r:0.75|y|0.6|0" final.mp4

#Sucky LensCorrection that you shouldn't use
#ffmpeg -i test.mp4 -vf 'lenscorrection=k2=0.033:k1=-0.18' out3.mp4
#ffmpeg -i test.mp4 -vf 'lenscorrection=k2=0.067:k1=-0.227' out.mp4
#ffmpeg -i finals_37.png -vf "lenscorrection=cx=0.50:cy=0.50:k1=-0.$count:k2=-0.012" k2_defished_final_$count.png
