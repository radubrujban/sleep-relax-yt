import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

duration = 8 * 3600
clips = []
for f in os.listdir('video'):
    path = os.path.join('video', f)
    clip = VideoFileClip(path).subclip(0, min(duration, VideoFileClip(path).duration))
    clips.append(clip)
video = concatenate_videoclips(clips, method='compose').loop(duration=duration)
audio = AudioFileClip('audio/rain.mp3').volumex(0.6).set_duration(duration)
final = video.set_audio(audio)
final.write_videofile('output/sleep_relax.mp4', fps=24, audio_codec='aac')
