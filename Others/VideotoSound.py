from moviepy import VidedoFileClip
# Load video file
video = VidedoFileClip('E:/MongNghi/1.mp4')

# Extract audio from video
audio = video.auto

# Define output audio file name
output_filename = 'output_audio.wav'

# Save audio to file
audio.write_audiofile(output_filename)