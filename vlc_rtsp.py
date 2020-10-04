import os
import argparse

args = []
# cvlc --random --loop ./playlist.xspf :sout=#gather:rtp{sdp=rtsp://:8554/} :network-caching=1500 :sout-all :sout-keep
black_magic = "cvlc --random --loop {} :sout=#gather:rtp{{sdp=rtsp://:{}/}} :network-caching=1500 :sout-all :sout-keep"

def collect_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="The RTSP port output", type=int, default=8554)
    parser.add_argument("--playlist", help="The VLC playlist file", type=str, default='./playlist.xspf')
    args = parser.parse_args()

    print(f'Running VLC stream with playlist {args.playlist} on port {args.port}')

def start_streaming():
    global black_magic
    print(black_magic)
    vlc_command = black_magic.format(args.playlist, args.port)
    print(vlc_command)
    os.system(vlc_command)

if __name__=="__main__":
    collect_args()
    start_streaming()