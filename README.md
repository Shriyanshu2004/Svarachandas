# 🕉️ Svarachandas

### *Where Sanskrit Meets Sound, Rhythm & Cinematic AI Experience*

---

## Problem Statement

Sanskrit chanting is not just reading text it is a **precise rhythmic science (Chandas)**.

However, most modern digital tools fail to preserve:

* ❌ Correct **Laghu (short) / Guru (long)** syllable timing
* ❌ Natural **melody & pitch flow**
* ❌ Immersive **spiritual chanting experience**

As a result, digital chanting loses its **authenticity, rhythm, and emotional depth**.

---

## Our Solution

**Svarachandas** is an AI-powered system that transforms Sanskrit verses into:

> 🎧 **Melodic + Rhythmic + Visually Immersive Chanting Experience**

It combines:

* Sanskrit **Chandas analysis**
* AI-driven **melody & pitch modulation**
* Human-like **chant generation**
* Cinematic **Netflix-style UI visualization**

---

## Key Features

###Cinematic Sanskrit Experience

* Netflix-style immersive UI
* Glowing elements, smooth animations, temple aesthetics

### AI Chant Generation

* Converts Sanskrit text → smooth chanting audio

### 🟢🔴 Laghu–Guru Visualization

* Real-time syllable classification
* Laghu (short syllable)
* Guru (long syllable)

### Animated Rhythm Display

* Pattern visualized using:

  * ◡ = Laghu
  * — = Guru
* Styled with glow and spacing for clarity

###Chandas Intelligence

* Detects syllable weight using Sanskrit rules:

  * Long vowels (आ, ई, ऊ…)
  * Consonant clusters
  * Anusvara (ं) / Visarga (ः)

###Premium UI/UX

* Glassmorphism cards
* Hover animations
* Temple-themed background

### 🔊 Seamless Audio Experience

* Continuous chanting (no breaks)
* Pitch-aware audio synthesis

---

##How It Works (Pipeline)

```text
User Input (Sanskrit Shloka)
        ↓
Text Processing & Cleaning
        ↓
Syllable Segmentation
        ↓
Laghu–Guru Detection
        ↓
Rhythm Mapping
        ↓
Audio Generation (gTTS)
        ↓
Pitch Adjustment + Processing
        ↓
Final Chant Output + Visual Display
```

---

## 🧪 Example Output

**Input:**

```
यदा यदा हि धर्मस्य ग्लानिर्भवति भारत।
```

**System Output:**

* 🎧 Chant Audio

* 📜 Sanskrit Verse Display

* Syllable Split:
  `ya | da | ya | da | hi | dhar | ma | sya | ...`

* 🟢🔴 Laghu–Guru Pattern:
  `◡ — ◡ — — ◡ ◡ — ...`

---

## Innovation & Uniqueness

✔ Combines **ancient Sanskrit prosody + modern AI**
✔ Provides **visual + auditory rhythm synchronization**
✔ Netflix-style **immersive chanting interface**
✔ Moves beyond TTS → **true chant experience**
✔ Focus on **authenticity + aesthetics + spirituality**

---

## Tech Stack

| Layer             | Technology             |
| ----------------- | ---------------------- |
| Frontend UI       | Streamlit + Custom CSS |
| Audio Engine      | pydub, numpy           |
| Voice             | gTTS                   |
| Signal Processing | librosa, scipy         |
| Sanskrit NLP      | Custom Python modules  |

---

## Project Structure

```
Svarachandas/
│── app.py
│── requirements.txt
│
├── utils/
│   ├── audio_engine.py
│   ├── melody.py
│   ├── text_processing.py
│   ├── chandas.py
│
├── assets/
│   └── bg.jpg
```

---

## Setup Instructions
Install FFmpeg before running:
https://ffmpeg.org/download.html
and put in your environment variable path

```bash
# Step 1: Download project (ZIP or clone)
# Step 2: Open terminal inside folder

pip install -r requirements.txt

# Step 3: Run app
streamlit run app.py
```

Tested on Python 3.12+

---

## Demo Video

👉 *(Add your 2-minute hackathon demo link here)*

---

## 📌 Hackathon Compliance

* Developed during hackathon period
* Uses open-source tools (gTTS, librosa, etc.)
* AI usage clearly declared
* Fully reproducible via README
* Public GitHub repository

---

## AI Disclosure

This project uses AI-based tools and libraries:

* **gTTS** → text-to-speech generation
* **Signal processing libraries** → pitch & rhythm modulation

No proprietary or restricted models are used.

---

## Future Scope

* Real-time voice chanting input
* Raaga-based chanting system
* 3D Temple (WebGL / Three.js)
* Meditation + chanting mode
* Multi-language sacred text support

---

## Team
Shriyanshu Rout Ray
Sugnan Murthy G M



---

##  Final Thought

> *“Svarachandas is not just an app — it is an attempt to digitize the soul of Sanskrit chanting.”*


