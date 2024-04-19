import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg='black')

rootpath = "C:\\Users\\shazna salman\\Desktop\\PDSA\\musicapp\\music"
pattern = "*.mp3"

mixer.init()

prv_img = tk.PhotoImage(file="prv.png")
stop_img = tk.PhotoImage(file="stop.png")
play_img = tk.PhotoImage(file="play.png")
pause_img = tk.PhotoImage(file="pause.png")
next_img = tk.PhotoImage(file="next.png")

def select(event=None):
    if listBox.curselection():
        selected_song = listBox.get(listBox.curselection())
        label.config(text=selected_song)
        mixer.music.load(os.path.join(rootpath, selected_song))
        mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear(0, 'end')

def pla_next():
    current_selection = listBox.curselection()
    if current_selection:
        next_song_index = current_selection[0] + 1
        if next_song_index < listBox.size():
            next_song_name = listBox.get(next_song_index)
            label.config(text=next_song_name)
            mixer.music.load(os.path.join(rootpath, next_song_name))
            mixer.music.play()
            listBox.select_clear(0, 'end')
            listBox.select_set(next_song_index)

def pla_prv():
    current_selection = listBox.curselection()
    if current_selection:
        prev_song_index = current_selection[0] - 1
        if prev_song_index >= 0:
            prev_song_name = listBox.get(prev_song_index)
            label.config(text=prev_song_name)
            mixer.music.load(os.path.join(rootpath, prev_song_name))
            mixer.music.play()
            listBox.select_clear(0, 'end')
            listBox.select_set(prev_song_index)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"

listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('ds-digital', 14))
listBox.pack(padx=15, pady=15)
listBox.bind('<<ListboxSelect>>', select)  

label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('ds-digital', 14))
label.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor='center')

prevButton = tk.Button(canvas, text="Prev", image=prv_img, bg='black', borderwidth=0, command=pla_prv)
prevButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg='black', borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text="Play", image=play_img, bg='black', borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text="Pause", image=pause_img, bg='black', borderwidth=0, command=pause_song)
pauseButton.pack(pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text="Next", image=next_img, bg='black', borderwidth=0, command=pla_next)
nextButton.pack(pady=15, in_=top, side='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
