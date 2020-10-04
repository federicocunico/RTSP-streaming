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

# Relative video file in container. default folder is videos that is PWD. Check run.sh to modify
video_sources = [
    '/videos/test.mp4'
]

def generate() -> str:
    header = """<?xml version="1.0" encoding="UTF-8"?>
<playlist version="1" xmlns="http://xspf.org/ns/0/">
<trackList>\n"""
    content = []
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
    print('\nSelected source files:')
    print(video_sources, end='\n\n')
    print('Phase 1: Generating playlist')
    f = generate()
    print('Phase 2: Saving')
    save(f)
    print('Done')
