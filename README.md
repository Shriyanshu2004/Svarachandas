# Svarachandas

### *Where Sanskrit Meets Sound, Rhythm & AI*

---

## Problem Statement

Sanskrit chanting is not just reading text it is a **structured rhythmic science (Chandas)**.
Most modern tools fail to preserve:

* Correct **Laghu (short) / Guru (long)** syllable timing
* Natural **melody and pitch flow**
* Immersive **spiritual experience**

As a result, digital chanting loses its **authenticity and soul**.

---

## Our Solution

**Svarachandas** is an AI-powered system that transforms Sanskrit verses into:

> **Melodic + Rhythmic + Emotionally immersive chants**

It combines:

* Sanskrit **Chandas analysis**
* AI-driven **melody synthesis**
* Human-like **voice chanting**
* Cinematic **temple UI experience**

---

## Key Features

### AI Chant Generation

* Converts Sanskrit text → natural chant audio

### 🟢 Laghu / 🔴 Guru Intelligence

* Detects syllable weight using Sanskrit prosody rules

### Real-time Rhythm Visualization

* Syllables animate in sync with chanting beats

### Melody + Pitch System

* Voice follows musical pitch (not robotic TTS)

### Immersive Temple UI

* Diya glow, particles, mantra aura, ambient design

### Audio Experience

* Smooth, continuous, non-breaking chanting

---

##How It Works (Pipeline)

```text
User Input (Sanskrit Shloka)
        ↓
Phonetic Conversion (IAST)
        ↓
Syllable Segmentation
        ↓
Laghu-Guru Detection
        ↓
Duration Mapping (Rhythm)
        ↓
Melody Generation (Pitch Curve)
        ↓
Voice Synthesis (gTTS)
        ↓
Pitch Modulation + Audio Merge
        ↓
Final Chant Output + UI Sync
```

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
│── app.py                 # Main UI + Interaction
│── requirements.txt
│
├── utils/
│   ├── audio_engine.py   # Voice + melody synthesis
│   ├── melody.py         # Pitch generation logic
│   ├── text_processing.py# IAST + syllables
│   ├── chandas.py        # Laghu/Guru detection
│
├── assets/
│   └── bg.jpg            # Temple background
```

---

## ⚙️ Setup Instructions

###Download Project

1. Click the green **Code** button on GitHub  
2. Select **Download ZIP**  
3. Extract the ZIP file  

### Run the Application

```bash
cd Svarachandas
pip install -r requirements.txt
streamlit run app.py

---

##Demo Video

👉 *(Add your 2-minute hackathon demo link here)*

---

##Example Output

**Input:**

```
विद्या ददाति विनयं
```

**System Output:**

* Melodic Chant Audio
* 🟢🔴 Laghu-Guru Visualization
* Animated Rhythm Sync

---

## Innovation & Uniqueness

✔ Combines **ancient Sanskrit metrics + modern AI audio**
✔ First system to provide **visual + auditory rhythm sync**
✔ Moves beyond TTS → **true chant experience**
✔ Focuses on **authenticity, not just generation**

---

## Hackathon Compliance

* Developed during hackathon period
* Uses open-source tools (gTTS, librosa, etc.)
* AI usage clearly declared
* Fully reproducible via README
* Public GitHub repository

---

## AI Disclosure

This project uses AI-based tools and libraries:

* **gTTS** → text-to-speech generation
* **Signal processing libraries** → pitch and rhythm modulation

No proprietary or restricted models are used.

---

## Future Scope

* Real-time voice chanting input
* Raaga-based chanting system
* 3D Temple (Three.js / WebGL)
* Meditation + chanting mode
* Multi-language sacred text support

---

##Team 

**Shriyanshu Rout Ray
Sugnan Murthy **

---

## Final Thought

> *“Svarachandas is not just an app it is an attempt to digitize the soul of Sanskrit chanting.”*


