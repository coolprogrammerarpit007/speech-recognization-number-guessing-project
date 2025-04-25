import speech_recognition as sr


# Handling Audio Files.

# r = sr.Recognizer()
# harvard = sr.AudioFile('harvard.wav')
# with harvard as source:
#     audio = r.record(source)

# print(r.recognize_google(audio,show_all=True))

#  **************************************************
#  **************************************************
#  **************************************************
#  **************************************************

#    Working with the microphones.

r = sr.Recognizer()
mic = sr.Microphone()

# to print the names of the mics.
# for name in sr.Microphone.list_microphone_names():
#     print(f"Microphone Name: {name}")

with mic as source:
    print("Calibrating Microphone...")
    r.adjust_for_ambient_noise(source,duration=5)
    print("Say Something....")
    audio = r.listen(source)


try:
    
    transcript = r.recognize_google(audio)
    print(f"You Said: {transcript}")

except sr.UnknownValueError:
    print("Sorry, I could not understand the audio...")

except sr.RequestError as e:
    print(f"Could not found the results...",e)
