import os
import sys

"""
Example template taken from https://wiki.videolan.org/XSPF/

<?xml version="1.0" encoding="UTF-8"?>
<playlist version="1" xmlns="http://xspf.org/ns/0/">
<trackList>
 <track><location>file:///mp3s/song_1.mp3</location></track>
 <track><location>file:///mp3s/song_2.mp3</location></track>
 <track><location>file:///mp3s/song_3.mp3</location></track>
</trackList>
</playlist>
"""

dst = 'playlist.xspf'

use_sources_file=True
sources_file=os.path.join(os.getcwd(), "videos.txt")

# Relative video file in container. default folder is videos that is PWD. Check run.sh to modify
video_sources = [
    '/videos/test.mp4'
]

def get_video_sources():
    v = []
    try:
        with open(sources_file, 'r') as fp:
            srcs = fp.readlines()
            for src in srcs:
                src = src.replace('\t', '').replace('\n', '')  # clear unwanted characters while forming XML string
                if src != '':  # if the remains is not an empty string
                    v.append(src)
        return v
    except Exception as e:
        print(f'UNABLE TO OPEN FILE: {sources_file}; USING TEST FILE')
        print(e)
        global video_sources
        return video_sources

def generate() -> str:
    header = """<?xml version="1.0" encoding="UTF-8"?>
<playlist version="1" xmlns="http://xspf.org/ns/0/">
<trackList>\n"""
    content = []
    if use_sources_file:
        video_sources = get_video_sources()
    print('\nSelected source files:')
    print(video_sources, end='\n\n')
    for src in video_sources:
        s = f" <track><location>file://{src}</location></track>"  # n.b. spazio all'inizio
        content.append(s)
    content = "\n".join([track for track in content])
    footer="""\n</trackList>
</playlist>"""

    final_file = header + content + footer
    
    print('Final playlist:\n')
    print(final_file, end='\n\n')
    return final_file

def save(final_file: str) -> None:
    out = os.path.join(os.getcwd(), dst)
    print('Writing in ' + out)
    with open(out, 'w') as fp:
        fp.write(final_file)

if __name__=="__main__":
    print('#'*42)
    print('# VLC Playlist generation')
    print('#'*42)
    print('Phase 1: Generating playlist')
    f = generate()
    print('Phase 2: Saving')
    save(f)
    print('Done')