#!/usr/bin/env python3
"""Calculate speech-recognition real-time factor from measured durations."""
import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio_seconds", type=float, help="duration of input audio in seconds")
    parser.add_argument("processing_seconds", type=float, help="measured processing time in seconds")
    args = parser.parse_args()
    if args.audio_seconds <= 0 or args.processing_seconds < 0:
        parser.error("audio duration must be > 0 and processing time must be >= 0")
    rtf = args.processing_seconds / args.audio_seconds
    print(f"RTF: {rtf:.4f}")
    print(f"Throughput: {1 / rtf:.2f}x real time" if rtf else "Throughput: instantaneous")
    print("Interpretation: faster than real time" if rtf < 1 else "Interpretation: real time" if rtf == 1 else "Interpretation: slower than real time")


if __name__ == "__main__":
    main()
