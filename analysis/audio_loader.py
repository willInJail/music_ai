# analysis/audio_loader.py

import librosa


def load_audio(path, sr=22050):
    """
    Load audio file as mono signal.
    """
    y, sr = librosa.load(path, sr=sr, mono=True)
    return y, sr


def slice_audio(y, sr, start_time, end_time):
    """
    Extract audio slice by time.
    """
    start_sample = int(start_time * sr)
    end_sample = int(end_time * sr)
    return y[start_sample:end_sample]
