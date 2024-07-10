from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    audio_file = clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()
    if audio_file is None:
        return None
    return audio_file

def convert_mp4_to_mp3(mp4_filename):
    print(f"Converting {mp4_filename} to mp3...")
    audio = AudioSegment.from_file(mp4_filename, format="mp4")
    audio.export(mp4_filename[:-4] + ".mp3", format="mp3")
    return mp4_filename[:-4] + ".mp3"
