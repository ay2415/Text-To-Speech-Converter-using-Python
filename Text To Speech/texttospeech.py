from gtts import gTTS
import os
helloo=open('new.txt')
text=helloo.read()
language='en'
obj=gTTS(text=text,lang=language,slow=False)
obj.save("first.mp3")
os.system("first.mp3")