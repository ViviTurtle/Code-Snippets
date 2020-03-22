FILE=`youtube-dl -f 251 "$1" | grep "Destination" | cut -d ":" -f 2 | cut -c 2-`
ffmpeg -i "${FILE}" -vn -ab 128k -ar 44100 -y "${FILE%.webm}.mp3"
rm $FILE
#Remove first 4 seconds of a file
#sox ${FILE%.webm}.mp3 New-${FILE%.webm}.mp3 trim 4