import os
import sys

from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.aac import AAC
from mutagen.wave import WAVE

AUDIO_LOADERS = {
    '.mp3': MP3,
    '.flac': FLAC,
    '.aac': AAC,
    '.wav': WAVE,
}

def get_bitrate(filename, loader):
    try:
        audio = loader(filename)
        br_kbps = audio.info.bitrate // 1000
        print(f"{filename} - {br_kbps} kbps")
        return br_kbps
    except Exception as e:
        print(f"{filename} - error: {e}")
        return None


def main():
    bitrates = []

    try:
        os.chdir(sys.argv[1])
    except IndexError:
        print("No folder specified\nUsage: python3 main.py {folder name}")
        sys.exit(1)

    for file in os.listdir():
        ext = os.path.splitext(file)[1].lower()
        loader = AUDIO_LOADERS.get(ext)

        if loader:
            br = get_bitrate(file, loader)
            if br is not None:
                bitrates.append(br)

    print(f"\nAverage bitrate: {sum(bitrates) // len(bitrates)} kbps")

if __name__ == '__main__':
    main()