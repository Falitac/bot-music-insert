import pyautogui, sys, time


def loadSongsFromFile(song_list):
	with open('songs.txt', 'r') as file:
		for line in file:
			song_list.append(line.strip())

def main():
	song_list = []
	loadSongsFromFile(song_list)

	print(f'Prepare for trouble! Songs to add: {len(song_list)}')
	time.sleep(2);

	for entry in song_list:
		pyautogui.typewrite('-p ' + entry);
		pyautogui.press('enter')
		time.sleep(0.5);

if __name__ == '__main__':
	main()