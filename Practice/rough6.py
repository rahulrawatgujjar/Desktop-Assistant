from translate import Translator
translator= Translator(to_lang="Hindi")
translation = translator.translate("Good Morning!")
print(translation)

from gtts import gTTS
import playsound
import os
speak = gTTS(text=translation, lang="hi", slow=False)
speak.save("captured_voice.mp3")
from pygame import mixer  # Load the popular external library
import time
from pygame import mixer


mixer.init()
mixer.music.load("D:\Drive\VS Code\captured_voice.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)

# Using OS module to run the translated voice.

# os.remove('captured_voice.mp3')