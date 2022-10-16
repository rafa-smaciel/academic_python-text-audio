from gtts import gTTS #pip install gtts
from playsound import playsound #pip install playsound

audio = 'audio.mp3'
language = 'pt-br'

sp = gTTS(
    text='Meu primeiro audio python',
    lang=language
)

sp.save(audio)
playsound(audio)