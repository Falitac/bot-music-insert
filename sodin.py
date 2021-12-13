import pyautogui, sys, time


def loadSongsFromFile(song_list, file_name):
	try:
		with open(file_name, 'r') as file:
			for line in file:
				song_list.append(line.strip())
	except FileNotFoundError:
		print(f'Skipping {file_name}')


def main():
	files = ["songs.txt"]
	if 1 < len(sys.argv):
		files = sys.argv[1:]

	song_list = []
	for file in files:
		loadSongsFromFile(song_list, file)

	print(f'Prepare for trouble! Songs to add: {len(song_list)}')
	time.sleep(2);

	for entry in song_list:
		pyautogui.typewrite('-p ' + entry);
		pyautogui.press('enter')
		time.sleep(0.4);
	

if __name__ == '__main__':
	main()