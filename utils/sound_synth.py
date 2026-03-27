import numpy as np
from scipy.io.wavfile import write

# 🎼 frequency mapping (Raga Yaman base)
NOTE_FREQ = {
    "Sa": 240,
    "Re": 270,
    "Ga": 300,
    "Ma#": 330,
    "Pa": 360,
    "Dha": 400,
    "Ni": 450
}

SAMPLE_RATE = 44100

# 🎧 generate single note
def generate_note(freq, duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)

    # sine wave + harmonic (more temple feel)
    wave = 0.6 * np.sin(2 * np.pi * freq * t)
    wave += 0.3 * np.sin(2 * np.pi * freq * 2 * t)

    # fade in/out
    fade = np.linspace(0, 1, int(0.05 * SAMPLE_RATE))
    wave[:len(fade)] *= fade
    wave[-len(fade):] *= fade[::-1]

    return wave

# 🎼 build full chant
def build_melody(notes, durations):
    audio = np.array([])

    for note, dur in zip(notes, durations):
        freq = NOTE_FREQ.get(note, 240)

        # duration ms → seconds
        duration_sec = dur / 1000

        tone = generate_note(freq, duration_sec)

        audio = np.concatenate((audio, tone))

    # normalize
    audio *= 32767 / np.max(np.abs(audio))
    return audio.astype(np.int16)

# 💾 save file
def save_wav(audio, filename="melody.wav"):
    write(filename, SAMPLE_RATE, audio)
    return filename