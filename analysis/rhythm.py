# analysis/rhythm.py

import librosa
import numpy as np


def analyze_rhythm_section(y, sr):
    """
    Analyze tempo for a given audio section using librosa.
    """

    if len(y) < sr:
        return None

    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return float(tempo)
