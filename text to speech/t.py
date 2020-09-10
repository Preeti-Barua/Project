from gtts import gTTS 
import os

fh = open("test.txt", "r")
myText= fh.read().replace("\n", " ")


langauge= 'en'
output= gTTS(text= myText, lang= langauge, slow= False)

output.save("output.mp3")
fh.close()
os.system("start output.mp3")