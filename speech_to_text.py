import speech_recognition as sr
from pydub import AudioSegment
import os

# Convert MP3 to WAV
sound = AudioSegment.from_mp3("sample.mp3")
sound.export("sample.wav", format="wav")

# Speech recognition
recognizer = sr.Recognizer()

with sr.AudioFile("sample.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print("Recognized Text:", text)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError:
    print("Google Speech Recognition service unavailable")

os.remove("sample.wav")
