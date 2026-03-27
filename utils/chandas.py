# utils/chandas.py

def analyze_laghu_guru(text):

    if not text.strip():
        return [], []

    words = text.split()

    syllables = []
    pattern = []

    for word in words:

        # Split into small chunks (safe syllable fallback)
        parts = [word[i:i+2] for i in range(0, len(word), 2)]

        for p in parts:
            syllables.append(p)

            # Simple Guru rule
            if any(v in p for v in ["ा","ी","ू","े","ो","ai","au"]):
                pattern.append("G")
            else:
                pattern.append("L")

    return syllables, pattern
