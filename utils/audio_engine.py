import asyncio
from edge_tts import Communicate
from pydub import AudioSegment
import numpy as np

VOICE = "hi-IN-SwaraNeural"

def stretch_vowels(text):
    replacements = {
        "Om": "Oom",
        "Namah": "Naamah",
        "Shivaya": "Shivaaya"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def make_chant(text):
    text = text.strip()
    text = stretch_vowels(text)
    text = text.replace(",", " ").replace(".", " ")
    return text

async def generate_audio(text, file):
    chant_text = make_chant(text)

    communicate = Communicate(
        text=chant_text,
        voice=VOICE,
        rate="-12%",
        pitch="+2Hz"
    )

    await communicate.save(file)

def generate_tanpura(duration_ms):
    sr = 44100
    duration = duration_ms / 1000
    t = np.linspace(0, duration, int(sr * duration))

    sa = 240
    pa = 360

    drone = (
        0.3 * np.sin(2 * np.pi * sa * t) +
        0.15 * np.sin(2 * np.pi * pa * t)
    )

    audio = (drone * 32767).astype(np.int16)

    return AudioSegment(
        audio.tobytes(),
        frame_rate=sr,
        sample_width=2,
        channels=1
    )

def generate_bell():
    sr = 44100
    t = np.linspace(0, 1.5, int(sr * 1.5))

    freq = 800
    bell = np.sin(2 * np.pi * freq * t) * np.exp(-3 * t)

    audio = (bell * 32767).astype(np.int16)

    return AudioSegment(
        audio.tobytes(),
        frame_rate=sr,
        sample_width=2,
        channels=1
    ) - 18

def apply_3d(audio):
    audio = audio.set_channels(2)

    left, right = audio.split_to_mono()

    delay_ms = 60

    # delay right ear
    right = AudioSegment.silent(duration=delay_ms) + right

    # reflections
    left_echo = left - 20
    right_echo = right - 22

    left = left.overlay(left_echo, position=120)
    right = right.overlay(right_echo, position=180)

    # CRITICAL FIX: trim both to same exact length
    min_len = min(len(left), len(right))

    left = left[:min_len]
    right = right[:min_len]

    return AudioSegment.from_mono_audiosegments(left, right)

def immersive_mix(input_file, output_file):
    voice = AudioSegment.from_file(input_file)

    # clean voice
    voice = voice.low_pass_filter(3800).high_pass_filter(120)

    duration = len(voice)

    # tanpura
    tanpura = generate_tanpura(duration)
    tanpura = tanpura - 28
    tanpura = tanpura.set_channels(2)

    # bell
    bell = generate_bell().set_channels(2)
    bell = bell + AudioSegment.silent(duration=duration - len(bell))

    # combine layers
    combined = tanpura.overlay(voice)
    combined = combined.overlay(bell)

    # apply 3D
    spatial = apply_3d(combined)

    #  light hall depth
    hall = spatial - 26
    final_audio = spatial.overlay(hall, position=300)

    final_audio.export(output_file, format="wav")


# -------- MAIN --------
def generate_audio_real_pitch(text):

    raw = "raw.mp3"
    final = "final.wav"

    asyncio.run(generate_audio(text, raw))
    immersive_mix(raw, final)

    return final