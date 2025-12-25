# analysis/segmentation.py

import numpy as np
import librosa
from core.structures import Section


def compute_chroma(y, sr, hop_length=512):
    """
    Compute chroma features for structural analysis.
    """
    chroma = librosa.feature.chroma_cqt(
        y=y,
        sr=sr,
        hop_length=hop_length
    )
    return chroma


def compute_novelty_curve(y, sr, hop_length=512):
    """
    Compute novelty curve using spectral flux.
    """
    onset_env = librosa.onset.onset_strength(
        y=y,
        sr=sr,
        hop_length=hop_length
    )

    # Normalize
    novelty = librosa.util.normalize(onset_env)

    times = librosa.frames_to_time(
        np.arange(len(novelty)),
        sr=sr,
        hop_length=hop_length
    )

    return novelty, times


def detect_boundaries(novelty, times, threshold=0.25, min_interval=5.0):
    """
    Detect section boundaries from novelty curve.
    """
    boundaries = []
    last_boundary = 0.0

    for value, time in zip(novelty, times):
        if value > threshold and (time - last_boundary) > min_interval:
            boundaries.append(time)
            last_boundary = time

    return boundaries


def segment_track(y, sr):
    """
    Segment full track into structural sections.
    """
    novelty, times = compute_novelty_curve(y, sr)
    boundaries = detect_boundaries(novelty, times)
    return boundaries


def boundaries_to_sections(boundaries, track_duration):
    """
    Convert boundary times into Section objects.
    """
    sections = []

    starts = [0.0] + boundaries
    ends = boundaries + [track_duration]

    for start, end in zip(starts, ends):
        if end - start >= 3.0:
            sections.append(Section(start_time=start, end_time=end))

    return sections
