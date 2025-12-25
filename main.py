# main.py

from analysis.analyze_track import analyze_track


if __name__ == "__main__":
    track = analyze_track("data/audio/test.wav")

    for i, section in enumerate(track.sections):
        print(f"Section {i}")
        print(f"  Start: {section.start_time:.2f}s")
        print(f"  End: {section.end_time:.2f}s")
        print(f"  Tempo: {section.tempo}")
        print(f"  Time signature: {section.time_signature}")
