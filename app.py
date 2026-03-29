import streamlit as st

st.set_page_config(
    page_title="स्वरछन्दस् (Svarachandas)",
    page_icon="🕉️",
    layout="wide"
)

import base64
from utils.audio_engine import generate_audio_real_pitch

# ---------- LOAD BG ----------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("assets/bg.jpg")

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

/* INPUT */
textarea {{
    background: rgba(0,0,0,0.85) !important;
    color:white !important;
    border-radius:15px !important;
    border:1px solid gold !important;
    padding:15px !important;
    font-size:18px !important;
}}

/* BUTTON CENTER */
.stButton {{
    display:flex;
    justify-content:center;
}}

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

/* CARDS */
.card {{
    background: rgba(255,255,255,0.05);
    padding:25px;
    border-radius:20px;
    backdrop-filter: blur(12px);
    box-shadow:0 0 30px rgba(255,165,0,0.2);
    transition:0.4s;
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

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">🕉️ Svarachandas</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Sanskrit Chanting • Rhythm • Melody</div>', unsafe_allow_html=True)
st.markdown('<div class="diya"></div>', unsafe_allow_html=True)

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

        # AUDIO
        audio = generate_audio_real_pitch(text)
        st.audio(audio)

        # ---------- NETFLIX CARDS ----------
        st.markdown("<br>")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="card">
            <h3>📜 Chandas</h3>
            <p>Ancient science of Sanskrit poetic meter.</p>
            <p>Defines rhythm & structure of verses.</p>
            <p>Examples: Gayatri, Anushtubh, Trishtubh</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="card">
            <h3>🟢 Laghu & 🔴 Guru</h3>
            <p>🟢 Laghu = Short (1 beat)</p>
            <p>🔴 Guru = Long (2 beats)</p>
            <p>Guru → long vowels, clusters, ं / ः</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="card">
            <h3>🚀 Experience</h3>
            <p>🎧 Chant Audio</p>
            <p>🎼 Rhythm Flow</p>
            <p>🧠 Intelligence</p>
            <p>✨ Visual Sync</p>
            </div>
            """, unsafe_allow_html=True)

        # ---------- OUTPUT (SAFE - NO HTML BUG) ----------
        syllables = split_simple(text)
        pattern = get_pattern(syllables)

        st.markdown("## 🕉️ Sanskrit Verse")
        st.write(text)

        st.markdown("## 🔤 Syllable Split")
        st.write(" | ".join(syllables))

        st.markdown("## 🟢🔴 Laghu–Guru Pattern")

        pattern_line = ""
        for p in pattern:
            if p == "L":
                pattern_line += "🟢◡ "
            else:
                pattern_line += "🔴— "

        st.markdown(f"### {pattern_line}")

    else:
        st.warning("Please enter a shloka 🙏")
