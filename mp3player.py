from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('Summer MP3 Player')
root.geometry('500x300')

# Initialize pygame mixer
pygame.mixer.init()


# Add song function
def add_song():
	song =filedialog.askopenfilename(initialdir='gui/audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
	
	# remove directory info from the song name
	song = song.replace("C:/Users/ansha/Desktop/Summer_Project/gui/audio/", "")
	song = song.replace(".mp3", "")

	# add song to listbox
	list_box.insert(END, song)

# Play selected song
def play():
	song = list_box.get(ACTIVE)
	song = f'C:/Users/ansha/Desktop/Summer_Project/gui/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

# Stop playing current song
def stop():
	pygame.mixer.music.stop()
	list_box.selection_clear(ACTIVE)


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
back_butn = Button(control_frame, image=back_butn_img, borderwidth=0)
frwrd_butn = Button(control_frame, image=frwrd_butn_img, borderwidth=0)
play_butn = Button(control_frame, image=play_butn_img, borderwidth=0, command=play)
pause_butn = Button(control_frame, image=pause_butn_img, borderwidth=0)
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

root.mainloop()