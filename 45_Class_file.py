
class Video:
	def __init__(self,title,link):
		self.title = title
		self.link = link

def input_video():
	title = input("Enter title: ")
	link = input("Enter link: ")
	video = Video(title,link)
	return video

def print_video(video):
	print("Title video: ",video.title)
	print("Link video: ",video.link)

def input_videos():
	videos = []
	total_video = input("How many videos you need: ")
	total_video = int(total_video)
	for i in range(total_video):
		print("Video ",i+1)
		vid = input_video()
		videos.append(vid)
	return videos

def print_videos(videos):
	print("-----")
	for i in range(len(videos)):
		print_video(videos[i])

def write_videos_txt(videos, file):
	file.write(videos.title + "\n")
	file.write(videos.link + "\n")

def write_to_txt(videos):
	total = len(videos)
	with open("data.txt", "w") as file:
		file.write("Total video:"+ str(total) + "\n")
		for i in range(total):
			write_videos_txt(videos[i],file)
def main():
	videos = input_videos()
  # print_video(videos[0]) => Truy cap vao mot list => 1 video
	print_videos(videos)
	write_to_txt(videos)
main()
  