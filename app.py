import streamlit as st
st.set_page_config(
    page_title="स्वरछन्दस् (Svarachandas)",
    page_icon="🕉️",
)
import base64
from utils.audio_engine import generate_audio_real_pitch

# ---------- LOAD BG ----------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("assets/bg.jpg")

st.set_page_config(layout="wide")

# ---------- CSS ----------
st.markdown(f"""
<style>

/* BACKGROUND */
.stApp {{
    background:
    linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)),
    url("data:image/jpg;base64,{bg}");
    background-size: cover;
    background-attachment: fixed;
}}

/* TITLE */
.title {{
    text-align:center;
    font-size:70px;
    color:gold;
    font-weight:bold;
    text-shadow:0 0 60px orange;
    margin-top:30px;
}}

.subtitle {{
    text-align:center;
    color:#ccc;
    font-size:20px;
    margin-bottom:30px;
}}

/* DIYA */
.diya {{
    width:30px;
    height:50px;
    margin:20px auto;
    background: radial-gradient(circle, yellow, orange, red);
    border-radius:50%;
    box-shadow:0 0 80px orange,0 0 120px gold;
    animation:flicker 0.12s infinite alternate;
}}

@keyframes flicker {{
    from {{transform:scale(1);}}
    to {{transform:scale(1.25);}}
}}

/* CARDS */
.card {{
    background: rgba(255,255,255,0.05);
    padding:25px;
    border-radius:20px;
    backdrop-filter: blur(12px);
    box-shadow:0 0 30px rgba(255,165,0,0.2);
    transition:0.4s;
    height:100%;
}}

.card:hover {{
    transform:scale(1.05);
    box-shadow:0 0 60px gold;
}}

.card h3 {{
    color:gold;
}}

.card p {{
    color:#ddd;
    line-height:1.6;
}}

/* INPUT */
textarea {{
    background: rgba(0,0,0,0.85) !important;
    color:white !important;
    border-radius:15px !important;
    border:1px solid gold !important;
    padding:15px !important;
    font-size:18px !important;
}}

/* BUTTON */
.stButton>button {{
    background:linear-gradient(45deg,orange,gold);
    color:black;
    border-radius:30px;
    padding:14px 40px;
    font-size:20px;
    box-shadow:0 0 30px orange;
}}

.stButton>button:hover {{
    transform:scale(1.1);
    box-shadow:0 0 60px gold;
}}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">🕉️ Svarachandas</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Sanskrit Chanting • Rhythm • Melody</div>', unsafe_allow_html=True)
st.markdown('<div class="diya"></div>', unsafe_allow_html=True)

# ---------- INFO CARDS ----------
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📜 Chandas</h3>
    <p>
    Chandas is the ancient science of Sanskrit poetic meter.
    It governs the rhythmic structure of verses.
    </p>
    <p>
    Each verse follows a precise pattern of syllables,
    creating musical flow and spiritual resonance.
    </p>
    <p>
    Examples:
    <br>• Gayatri
    <br>• Anushtubh
    <br>• Trishtubh
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>🟢 Laghu & 🔴 Guru</h3>
    <p>
    🟢 Laghu = Short syllable (1 beat)<br>
    🔴 Guru = Long syllable (2 beats)
    </p>
    <p>
    Guru occurs when:
    <br>• Long vowels (आ, ई, ऊ)
    <br>• Consonant clusters
    <br>• Anusvara (ं) / Visarga (ः)
    </p>
    <p>
    This pattern defines rhythm in chanting.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>🚀 Experience</h3>
    <p>
    Svarachandas transforms text into:
    </p>
    <p>
    🎧 Chant Audio<br>
    🎼 Melody Flow<br>
    🧠 Rhythm Intelligence<br>
    ✨ Visual Feedback
    </p>
    <p>
    Not just TTS — a spiritual audio experience.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ---------- INPUT ----------
st.markdown("<br><br>", unsafe_allow_html=True)
text = st.text_area("", placeholder="Enter Sanskrit Shloka...", height=140)

# ---------- LOGIC ----------
def split_simple(text):
    words = text.split()
    syllables = []
    for w in words:
        parts = [w[i:i+2] for i in range(0, len(w), 2)]
        syllables.extend(parts)
    return syllables

def get_pattern(syllables):
    pattern = []
    for s in syllables:
        if any(v in s for v in ["ा","ी","ू","े","ो"]):
            pattern.append("G")
        else:
            pattern.append("L")
    return pattern

# ---------- BUTTON ----------
if st.button("🔔 Generate Divine Chant"):

    if text.strip():

        audio = generate_audio_real_pitch(text)
        st.audio(audio)

        syllables = split_simple(text)
        pattern = get_pattern(syllables)

        # TEXT
        st.markdown(f"""
        <div style="font-size:30px; color:white; text-align:center; margin-top:30px;">
        {text}
        </div>
        """, unsafe_allow_html=True)

        # SPLIT
        split_line = " | ".join(syllables)

        st.markdown(f"""
        <div style="font-size:22px; color:#ddd; text-align:center; margin-top:20px;">
        {split_line}
        </div>
        """, unsafe_allow_html=True)

        # PATTERN
        st.markdown("<h3 style='text-align:center; margin-top:25px;'>Laghu–Guru Pattern</h3>", unsafe_allow_html=True)

        pattern_html = "<div style='text-align:center; font-size:30px;'>"

        for p in pattern:
            if p == "L":
                pattern_html += "<span style='color:#00ff88; margin:6px;'>◡</span>"  # GREEN Laghu
            else:
                pattern_html += "<span style='color:#ff4d4d; margin:6px;'>—</span>"  # RED Guru

        pattern_html += "</div>"

        st.markdown(pattern_html, unsafe_allow_html=True)

    else:
        st.warning("Please enter a shloka 🙏")
