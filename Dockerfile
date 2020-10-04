# FROM ubuntu:latest
FROM python:3.8

RUN apt-get update && apt-get install -y vlc

# Add user is required for run vlc as non-root
RUN useradd -ms /bin/bash vlcuser
USER vlcuser
WORKDIR /home/vlcuser

# Copying the playlist. BE AWARE OF CREATE ONE IN ADVANCE
COPY playlist.xspf /home/vlcuser/playlist.xspf
COPY vlc_rtsp.py /home/vlcuser/rtsp.py

# Enter the terminal in the container
# CMD [ "/bin/bash" ]

# Run rtsp server on start
CMD [ "python", "rtsp.py"]
