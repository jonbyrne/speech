import tkinter as tk
from tkinter import filedialog
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_input():
    input_text = input_box.get("1.0", "end-1c")
    filename = filedialog.asksaveasfilename(defaultextension=".mp3") # ask for a filename
    volume = volume_slider.get()
    text_to_audio(input_text, engine, filename, volume)

def text_to_audio(text, engine, filename, volume):
    engine.setProperty("voice", "english-us") # set the voice to US English
    engine.setProperty("rate", 150) # set the speaking rate to 150 words per minute
    engine.setProperty("volume", volume) # set the volume to the value from the slider
    engine.save_to_file(text, filename) # save the text-to-speech output directly to an audio file
    engine.runAndWait()

root = tk.Tk()
root.title("Text-to-Speech")
root.attributes("-fullscreen", True)

engine = pyttsx3.init()

input_label = tk.Label(root, text="Enter text to speak:")
input_label.pack()

input_box = tk.Text(root, height=10, width=50)
input_box.pack()

volume_label = tk.Label(root, text="Volume:")
volume_label.pack()

volume_slider = tk.Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, length=300)
volume_slider.set(0.8) # set the initial value of the volume slider to 0.8
volume_slider.pack()

speak_button = tk.Button(root, text="Save as MP3", command=get_input)
speak_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()
