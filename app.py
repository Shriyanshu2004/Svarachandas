import streamlit as st
st.set_page_config(
    page_title="स्वरछन्दस् (Svarachandas)",
    page_icon="🕉️",
)
import base64
import json

from utils.audio_engine import generate_audio_real_pitch
from utils.text_processing import to_iast, syllabify
from utils.chandas import laghu_guru, get_durations

# -------- LOAD BG --------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("assets/bg.jpg")

# -------- UI --------
st.markdown(f"""
<style>

/* BACKGROUND */
.stApp {{
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.95)),
                url("data:image/jpg;base64,{bg}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* PARTICLES */
.particles {{
    position: absolute;
    width: 100%;
    height: 100%;
    pointer-events: none;
}}

.particles span {{
    position: absolute;
    width: 4px;
    height: 4px;
    background: gold;
    border-radius: 50%;
    animation: float 10s linear infinite;
}}

@keyframes float {{
    0% {{ transform: translateY(100vh); opacity: 0; }}
    50% {{ opacity: 1; }}
    100% {{ transform: translateY(-10vh); opacity: 0; }}
}}

/* CENTER */
.container {{
    text-align: center;
    margin-top: 80px;
}}

/* MANTRA */
.mantra {{
    font-size: 26px;
    color: gold;
    animation: pulse 2.5s infinite;
}}

@keyframes pulse {{
    0% {{ opacity: 0.6; }}
    50% {{ opacity: 1; }}
    100% {{ opacity: 0.6; }}
}}

/* DIYA */
.diya {{
    width: 20px;
    height: 40px;
    margin: 20px auto;
    background: radial-gradient(circle, yellow, orange, red);
    border-radius: 50%;
    box-shadow: 0 0 40px orange, 0 0 80px gold;
    animation: flicker 0.15s infinite alternate;
}}

@keyframes flicker {{
    from {{ transform: scale(1); }}
    to {{ transform: scale(1.15); }}
}}

/* TITLE */
.title {{
    font-size: 48px;
    color: gold;
    text-shadow: 0 0 20px orange;
}}

/* INPUT */
textarea {{
    background: rgba(0,0,0,0.7) !important;
    color: white !important;
    border-radius: 10px !important;
    border: 1px solid orange !important;
}}

/* BUTTON */
.stButton>button {{
    background: linear-gradient(45deg, orange, gold);
    color: black;
    border-radius: 30px;
    padding: 12px 28px;
    border: none;
    box-shadow: 0 0 20px orange;
}}

.stButton>button:hover {{
    transform: scale(1.1);
}}

/* SYLLABLE VISUALIZER */
.syllable {{
    display: inline-block;
    padding: 6px 10px;
    margin: 4px;
    border-radius: 8px;
    font-size: 20px;
    background: rgba(255,255,255,0.05);
    transition: 0.3s;
}}

.laghu {{
    color: #00ff88;
}}

.guru {{
    color: #ff4d4d;
}}

.active {{
    background: gold !important;
    color: black !important;
    transform: scale(1.3);
    box-shadow: 0 0 20px gold;
}}

@keyframes wave {{
    0% {{ transform: translateY(0px); }}
    50% {{ transform: translateY(-10px); }}
    100% {{ transform: translateY(0px); }}
}}

.wave {{
    animation: wave 1s infinite;
}}

</style>

<!-- PARTICLES -->
<div class="particles">
    {"".join([f'<span style="left:{i*5}%"></span>' for i in range(20)])}
</div>

<!-- MAIN -->
<div class="container">
    <div class="mantra">ॐ नमः शिवाय</div>
    <div class="diya"></div>
    <div class="title">🕉️ Svarachandas</div>
</div>

""", unsafe_allow_html=True)

# -------- INPUT --------
text = st.text_area("", placeholder="Enter Sanskrit Shloka...", height=120)

# -------- BUTTON --------
if st.button("🔔 Generate Divine Chant"):

    # 🎧 AUDIO
    audio = generate_audio_real_pitch(text)
    st.audio(audio)

    try:
        # 🧠 CHANDAS AFTER CLICK
        iast = to_iast(text)
        syllables = syllabify(iast)
        pattern = laghu_guru(syllables)
        durations = get_durations(pattern)

        # 🎨 BUILD UI
        html = ""
        for i, (syl, p) in enumerate(zip(syllables, pattern)):
            cls = "laghu" if p == "L" else "guru"
            html += f'<span id="syl{i}" class="syllable {cls}">{syl}</span>'

        st.markdown(html, unsafe_allow_html=True)

        # 🔥 SYNC JS (NO ERROR VERSION)
        js = f"""
        <script>
        const durations = {json.dumps(durations)};
        let index = 0;

        function animate() {{
            for (let i = 0; i < durations.length; i++) {{
                let el = document.getElementById("syl"+i);
                if (el) el.classList.remove("active","wave");
            }}

            let el = document.getElementById("syl"+index);
            if (el) el.classList.add("active","wave");

            index++;
            if (index >= durations.length) index = 0;
        }}

        function start() {{
            let t = 0;
            durations.forEach(function(d,i) {{
                setTimeout(function() {{
                    index = i;
                    animate();
                }}, t);
                t += d;
            }});
        }}

        setTimeout(start, 1200);
        </script>
        """

        st.components.v1.html(js, height=0)

    except:
        st.warning("⚠️ Could not process chandas")