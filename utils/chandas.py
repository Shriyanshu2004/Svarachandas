def laghu_guru(syllables):
    long_vowels = ["ā", "ī", "ū", "e", "o"]
    result = []

    for syl in syllables:
        if any(v in syl for v in long_vowels):
            result.append("G")
        elif syl.endswith(('ṃ', 'ḥ')):
            result.append("G")
        else:
            result.append("L")

    return result


def get_durations(pattern):
    durations = []

    for i, p in enumerate(pattern):
        if p == "L":
            durations.append(400)
        else:
            durations.append(700)

        # pause after each 8 syllables (like shloka)
        if i % 8 == 7:
            durations[-1] += 300

    return durations