import pyaudio
import vosk
import pyttsx3
import os
import sys


if getattr(sys, 'frozen', False):
    exe_path = os.path.dirname(sys.executable)
else:
    exe_path = os.path.dirname(os.path.abspath(__file__))
dependent_file_path = os.path.join(exe_path, 'vosk-model-small-en-us-0.15')

engine = pyttsx3.init()
engine.setProperty('rate', 130)

model = vosk.Model(dependent_file_path)

recognizer = vosk.KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=4000)


def get_sound_text():
    i = 0
    while True:
        data = stream.read(4000)
        i += 1
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_text = eval(result)["text"]

            if result_text:
                engine.say(f"{result_text} page will be opened.")
                engine.runAndWait()
                stream.stop_stream()
                stream.close()
                p.terminate()
                engine.stop()
                return result_text

        if i >= 30:
            engine.say("You did not say anything. Please try again. ")
            engine.runAndWait()
            stream.stop_stream()
            stream.close()
            p.terminate()
            engine.stop()
            return "Timeout Error"


#print(get_sound_text())