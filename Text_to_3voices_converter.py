import gtts
from googletrans import Translator
from tkinter import *
from tkinter import ttk
import os
import pygame
import time

# Initialize the translator
translator = Translator()

# Function to translate and speak text
def speak_text():
    text = text_input.get()
    selected_lang = language_var.get()

    # Set language codes for translation and TTS
    lang_code = "en" if selected_lang == "English" else "hi" if selected_lang == "Hindi" else "gu"

    try:
        # Translate the text
        translated = translator.translate(text, dest=lang_code).text

        # Use Google Text-to-Speech (gTTS) for the translated text
        filename = f"output_{int(time.time())}.mp3"  # Unique filename
        tts = gtts.gTTS(translated, lang=lang_code)
        tts.save(filename)

        # Initialize pygame mixer and play the mp3 file
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            continue  # Keep checking until playback is done

        # Clean up the file after playback
        os.remove(filename)  # Remove the file after playing

    except Exception as e:
        print(f"Error occurred: {e}")

# Create the GUI window
root = Tk()
root.title("Text to Speech with Translation")

# Text input field
text_label = Label(root, text="Enter the text:")
text_label.pack(pady=10)

text_input = Entry(root, width=50)
text_input.pack(pady=10)

# Language selection dropdown
language_var = StringVar()
language_var.set("English")  # Default selection

language_label = Label(root, text="Select Language:")
language_label.pack(pady=10)

languages = ["English", "Hindi", "Gujarati"]
language_menu = ttk.Combobox(root, textvariable=language_var, values=languages)
language_menu.pack(pady=10)

# Speak button
speak_button = Button(root, text="Translate and Speak", command=speak_text)
speak_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
