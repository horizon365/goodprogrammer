SOURCEVIDEO=/tmp/SourceVideo
TARGETVIDEO=/var/ftp/ClassVideo

CMD="ffmpeg -i $SOURCEVIDEO/$src.mov $TARGETVIDEO/$src.mp4"

mkdir -p SOURCEVIDEO

for src in $SOURCEVIDEO/*.mov;
  do
    if test $( pgrep -f "ffmpeg" | wc -l ) -ne 0 ;
      then
        if [ ! -f $TARGETVIDEO/$src ];
          then echo $CMD;

        fi
    fi
  done
