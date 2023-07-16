# Define a video class, a video has title and link
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link 

# Ask an user to enter information of a video
def read_video():
	title = input("Enter title: ")
	link = input("Enter link: ")
	video = Video(title,link)
	return video

# Show information of a video
def print_video(video):
	print("Title video: ", video.title, end ="")
	print("Link video: ", video.link, end="")

# Ask an user to enter information of all videos, they first choose how many videos are there
def read_videos():
	videos = []
	total_video = int(input("Nhap tong so video: "))
	for i in range(total_video):
		print("Video", i+1)
		vid = read_video()
		videos.append(vid)
	return videos 

# Show information of all videos
def print_videos(videos):
	print("-----------")
	for i in range(len(videos)):
		print_video(videos[i])


# Write a video information to a text file
def write_video_txt(video, file):	
	file.write(video.title + "\n")
	file.write(video.link + "\n")

# Write videos to text file, first line is the total number of videos
def write_videos_txt(videos):
	with open("data.txt","w") as file:
		file.write(str(len(videos)) + "\n")
		for i in range(len(videos)):
			write_video_txt(videos[i], file)

# Read 2 line from a text file and return a video
def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title,link)
	return video

# Read data.txt and return a list of videos 
def read_videos_from_txt():
	videos = []
	with open("data.txt","r") as file:
		total = file.readline()
		for i in range(int(total)):
			video = read_video_from_txt(file)
			videos.append(video)
	return videos

def main():
	# Ask user to enter information of all videos one by one
	videos = read_videos()
	# Write videos information to a text file
	write_videos_txt(videos)	
	# Read the text file to get a videos list
	videos = read_videos_from_txt()
	# Use the list above and show all information of videos inside that list
	print_videos(videos)

main()