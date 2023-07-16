# Define a video class, a video has title and link
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link 

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name 
		self.description = description
		self.rating = rating
		self.videos = videos

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
	print("xxx")
	print(videos)
	print("xxx")

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
def write_videos_txt(videos,file):
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
def read_videos_from_txt(file):
	videos = []
	total = file.readline()
	for i in range(int(total)):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos

def read_playlist():
	playlist_name = input("Enter playlist name: ")
	playlist_description = input("Enter playlist description: ")
	playlist_rating = input("Enter rating (1-5): ")
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def write_playlist_txt(playlist):
	with open("data.txt","w") as file:
		file.write(playlist.name + "\n")
		file.write(playlist.description + "\n")
		file.write(playlist.rating + "\n")
		write_videos_txt(playlist.videos, file)
	print("Successfully write to playlist to txt")

def read_playlist_from_txt():
	with open("data.txt","r") as file:
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_videos = read_videos_from_txt(file)
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def print_playlist(playlist):
	print("----------***-----------")
	print("Name playlist: ", playlist.name, end ="")
	print("Description playlist: ", playlist.description, end="")
	print("Rating playlist: ", playlist.rating, end="")
	print_videos(playlist.videos)

def show_menu():
	print("--------------")
	print("Option 1: Creat playlist")
	print("Option 2: Show playlist")
	print("Option 3: Play a video")
	print("Option 4: Add a video")
	print("Option 5: Update a playlist")
	print("Option 6: Delete a video")
	print("Option 7: Save and exit")
	print("--------------")
	
	
def main():
	# playlist = read_playlist()
	# write_playlist_txt(playlist)
	# playlist = read_playlist_from_txt()
	# print_playlist(playlist)
	try:
		playlist = read_playlist_from_txt()
		print("Loaded data Successfully")
	except:
		print("Welcome, you are first user")

	while True:
		show_menu()
		choice_option = int(input("Select an option (1-7): "))
		if choice_option == 1:
			playlist = read_playlist()
		elif choice_option == 2:
			print_playlist(playlist)
		elif choice_option == 7:
			write_playlist_txt(playlist)
			break
		else:
			print("You choiced a wrong. Exit a program")
			break
main()
