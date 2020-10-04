# RTSP-streaming
Tool for streaming a video file with VLC. It creates a local rtsp stream bound to a specific port (8554)

It uses a VLC playlist to loop over a file and send the streaming over the RTSP server created by VLC itself.
The general command is:

> cvlc --random --loop /path/to/playlist/file :sout=#gather:rtp{{sdp=rtsp://localhost:port/}} :network-caching=1500 :sout-all :sout-keep

With specification of playlist file, an address (localhost in this case) and the port, vlc starts streaming.
The default port is 8554 and if another port it's required you should change the python code and the run.sh docker run parameters (-p).

To verify the streaming starts a rtsp client on the address specified e.g. rtsp://localhost:8554/

## Requirements
Python 3.5+ is required (for string formatter shortcut) without any specific package installed.
It's also required VLC media player (tested with VLC 3.0.8, build 11 Sep 2019).

Tested on Ubuntu 18.04.

## How to
1) First of all, set the video files to play. Place them in a folder accessible to the docker, modifing the mount volume option (-v in run.sh) if required (not required if you copy the video files in the current dir). Then edit the file `videos.txt`, adding for each line only the video file name to insert in the playlist.
At last create the playlist with
`python generate_playlist.py`

    This will generate the `playlist.xspf` file.

2) If you have not the video files in the current directory, remember to edit the `run.sh` mount volume option (-v) or soft-link the video files in the current directory, then run the build command with `./build.sh`

3) Run the service with `./run.sh`

4) Check the streaming is working properly with a new instance of VLC. Run VLC > Media > Open Network Stream. Then enter the url (e.g. rtsp://localhost:8554/ ) and click "Play".

