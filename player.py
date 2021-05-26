from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title('Summer MP3 Player')
root.geometry('500x450')

# Initialize pygame mixer
pygame.mixer.init()


# Grab song length and time infi
def play_time():
	# Get current song elapsed time
	current_time = pygame.mixer.music.get_pos() / 1000

	# Throw up temp. lable to get data
	slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}')

	# Conver to time format
	converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

	# Get the currently playing song
	#current_song = list_box.curselection()
	# Grab song title from playlist
	song = list_box.get(ACTIVE)
	# Add directory structure and mp3 to song name
	song = f'C:/Users/ansha/Desktop/Summer_Project/gui/audio/{song}.mp3'
	# Load song with mutagen
	song_mut = MP3(song)
	# Get song length
	global song_length
	song_length = song_mut.info.length
	# Convert to time format
	converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

	# Increase current time by one second
	current_time += 1

	if int(my_slider.get()) == int(song_length):
		pass
		status_bar.config(text=f'Time Elapsed: {converted_song_length}  ')


	elif int(my_slider.get()) == int(current_time):
		# update slider to position
		slider_position = int(song_length)
		my_slider.config(to=slider_position, value=int(current_time))
	else:
		# update slider to position
		slider_position = int(song_length)
		my_slider.config(to=slider_position, value=int(my_slider.get()))
		
		# Conver to time format
		converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))
	
		# Output time to status bar
		status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')

		# Move this thing along by one sec
		next_time = int(my_slider.get()) + 1
		my_slider.config(value=next_time)

	# # Output time to status bar
	# status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')
	
	# Update slider position valur to current time position
	#my_slider.config(value=int(current_time))

	

	# update time
	status_bar.after(1000, play_time)



# Add song function
def add_song():
	song =filedialog.askopenfilename(initialdir='gui/audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
	
	# remove directory info from the song name
	song = song.replace("C:/Users/ansha/Desktop/Summer_Project/gui/audio/", "")
	song = song.replace(".mp3", "")

	# add song to listbox
	list_box.insert(END, song)

# Add many songs to the playlist
def add_many_songs():
	songs =filedialog.askopenfilenames	(initialdir='gui/audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

	# Loop through the list and replace directory info
	for song in songs:
		song = song.replace("C:/Users/ansha/Desktop/Summer_Project/gui/audio/", "")
		song = song.replace(".mp3", "")
		# Insert into playlist
		list_box.insert(END, song)

# Play selected song
def play():
	song = list_box.get(ACTIVE)
	song = f'C:/Users/ansha/Desktop/Summer_Project/gui/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	# call the play_time func. to get song length
	play_time()

	# # update slider to position
	# slider_position = int(song_length)
	# my_slider.config(to=slider_position, value=0)
# Stop playing current song
def stop():
	pygame.mixer.music.stop()
	list_box.selection_clear(ACTIVE)

	# Clear the status bar
	status_bar.config(text='')

# Play next song in the playlist
def next_song():
	# Get the current song
	next_one = list_box.curselection()
	# Add one to current song
	next_one = next_one[0]+1
	# Grab song title from playlist
	song = list_box.get(next_one)
	# Add directory structure and mp3 to song name
	song = f'C:/Users/ansha/Desktop/Summer_Project/gui/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	# Clear active bar in playlist
	list_box.selection_clear(0, END)

	# Activate new song bar
	list_box.activate(next_one)

	# Set active bar to next song
	list_box.selection_set(next_one, last=None)

# Play previous song in playlist
def prev_song():
	
	# Get the current song
	next_one = list_box.curselection()
	# Add one to current song
	next_one = next_one[0]-1
	# Grab song title from playlist
	song = list_box.get(next_one)
	# Add directory structure and mp3 to song name
	song = f'C:/Users/ansha/Desktop/Summer_Project/gui/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	# Clear active bar in playlist
	list_box.selection_clear(0, END)

	# Activate new song bar
	list_box.activate(next_one)

	# Set active bar to next song
	list_box.selection_set(next_one, last=None)

# Delete A Song
def delete_song():
	list_box.delete(ANCHOR)
	pygame.mixer.music.stop()


# Delete all songs
def delete_songs():
	list_box.delete(0, END)
	pygame.mixer.music.stop()	


# create global pause variable
global pause
paused = False

# Pause and unpause currently playing song
def pause(is_paused):
	global paused
	paused = is_paused

	if paused:
		pygame.mixer.music.unpause()
		paused = False
	else:
		pygame.mixer.music.pause()
		paused = True

# Slider function
def slide(x):
	#slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
	song = list_box.get(ACTIVE)
	song = f'C:/Users/ansha/Desktop/Summer_Project/gui/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

# Create playlist box
list_box = Listbox(root, bg='black', fg='white', width=60, selectbackground="white", selectforeground="black")
list_box.pack(pady=20)

# Create player control buttons
back_butn_img = PhotoImage(file='gui/images/back50.png')
frwrd_butn_img = PhotoImage(file='gui/images/forward50.png')
play_butn_img = PhotoImage(file='gui/images/play50.png')
pause_butn_img = PhotoImage(file='gui/images/pause50.png')
stop_butn_img = PhotoImage(file='gui/images/stop50.png')

# Create player control frame
control_frame = Frame(root)
control_frame.pack()

# Create player control buttons
back_butn = Button(control_frame, image=back_butn_img, borderwidth=0,command=prev_song)
frwrd_butn = Button(control_frame, image=frwrd_butn_img, borderwidth=0,command=next_song)
play_butn = Button(control_frame, image=play_butn_img, borderwidth=0, command=play)
pause_butn = Button(control_frame, image=pause_butn_img, borderwidth=0, command=lambda: pause(paused))
stop_butn = Button(control_frame, image=stop_butn_img, borderwidth=0, command=stop)

back_butn.grid(row=0, column=0, padx=5) 
frwrd_butn.grid(row=0, column=1, padx=5)
play_butn.grid(row=0, column=2, padx=5)
pause_butn.grid(row=0, column=3, padx=5)
stop_butn.grid(row=0, column=4, padx=5)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)

# Add many songs to the playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

# Create delete song mentu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label='Remove Songs', menu=remove_song_menu)
remove_song_menu.add_command(label='Delete A Song From The Playlist', command=delete_song)
remove_song_menu.add_command(label='Delete All Songs From The Playlist', command=delete_songs)

# Create status bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)


# Slider
my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.pack(pady=30)

# Create temp. slider lable
slider_label = Label(root, text='0')
slider_label.pack(pady=10)


root.mainloop()