# analysis/analyze_track.py

from analysis.audio_loader import load_audio, slice_audio
from analysis.segmentation import segment_track, boundaries_to_sections
from analysis.rhythm import analyze_rhythm_section
from core.structures import TrackAnalysis


def analyze_track(path):
    """
    Full analysis pipeline for one audio track.
    """

    y, sr = load_audio(path)
    duration = len(y) / sr

    track = TrackAnalysis(
        track_path=path,
        duration=duration,
        sample_rate=sr
    )

    boundaries = segment_track(y, sr)
    sections = boundaries_to_sections(boundaries, duration)

    for section in sections:
        y_section = slice_audio(y, sr, section.start_time, section.end_time)
        tempo = analyze_rhythm_section(y_section, sr)
        section.tempo = tempo
        track.add_section(section)

    return track
