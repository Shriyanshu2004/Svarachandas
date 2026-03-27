RAGA_YAMAN = {
    "Sa": 240,
    "Re": 270,
    "Ga": 300,
    "Ma#": 330,
    "Pa": 360,
    "Dha": 400,
    "Ni": 450
}

def map_notes(pattern):
    notes = []
    scale = ["Sa", "Re", "Ga", "Ma#", "Pa", "Dha", "Ni"]

    idx = 0
    for p in pattern:
        if p == "L":
            notes.append(scale[idx % len(scale)])
        else:
            notes.append(scale[(idx + 2) % len(scale)])

        idx += 1

    return notes