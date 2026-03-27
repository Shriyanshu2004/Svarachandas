import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr

def record_audio(filename="temp_audio/input.wav", duration=5, fs=44100):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(filename, fs, audio)
    return filename

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio, language="hi-IN")
    except:
        return "Speech not recognized"

def record_and_transcribe():
    file_path = record_audio()
    return transcribe_audio(file_path)