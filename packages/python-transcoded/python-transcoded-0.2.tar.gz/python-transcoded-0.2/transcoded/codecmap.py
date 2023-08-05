class MapItem:
    def __init__(self, codec, ffmpeg_encoder, ffprobe):
        self.codec = codec
        self.ffmpeg_encoder = ffmpeg_encoder
        self.ffprobe = ffprobe


_MAP = [
    MapItem('copy', 'copy', ''),
    MapItem('h264', 'libx264', 'h264'),
    MapItem('vp9', 'libvpx-vp9', ''),
    MapItem('mkv', 'matroska', 'matroska,webm'),
    MapItem('ac3', 'ac3', 'ac3'),
    MapItem('mp3', 'libmp3lame', 'mp3'),
    MapItem('srt', 'srt', 'subrip'),
    MapItem('eac3', 'eac3', 'eac3'),
    MapItem('dts', 'dca', 'dts'),
    MapItem('vorbis', 'libvorbis', 'vorbis'),
    MapItem('opus', 'libopus', 'opus'),
    MapItem('aac', 'aac', 'aac')
]


def getByCodec(codec):
    for item in _MAP:
        if item.codec == codec:
            return item


def getByFfprobe(codec):
    for item in _MAP:
        if item.ffprobe == codec:
            return item
