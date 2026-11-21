#!/usr/bin/env python3
"""Calculate speech-recognition real-time factor (RTF) and multi-run statistics."""
import argparse
import json
import math
import statistics


def compute_stats(audio_seconds: float, run_seconds: list[float]) -> dict[str, float | int | str]:
    """Compute RTF summary statistics across one or more measured processing runs."""
    if audio_seconds <= 0:
        raise ValueError("audio_seconds must be > 0")
    if not run_seconds or any(t < 0 for t in run_seconds):
        raise ValueError("processing times must be non-empty and >= 0")

    rtfs = sorted(t / audio_seconds for t in run_seconds)
    median_rtf = statistics.median(rtfs)
    p95_idx = max(0, min(len(rtfs) - 1, math.ceil(0.95 * len(rtfs)) - 1))
    p95_rtf = rtfs[p95_idx]
    interpretation = (
        "faster than real time"
        if median_rtf < 1.0
        else "real time"
        if median_rtf == 1.0
        else "slower than real time"
    )
    return {
        "audio_seconds": audio_seconds,
        "runs": len(rtfs),
        "median_rtf": median_rtf,
        "min_rtf": rtfs[0],
        "max_rtf": rtfs[-1],
        "p95_rtf": p95_rtf,
        "throughput_x": (1.0 / median_rtf) if median_rtf > 0 else float("inf"),
        "interpretation": interpretation,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio_seconds", type=float, help="duration of input audio in seconds")
    parser.add_argument(
        "processing_seconds",
        type=float,
        nargs="+",
        help="one or more measured processing times in seconds",
    )
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON summary")
    args = parser.parse_args()

    try:
        stats = compute_stats(args.audio_seconds, args.processing_seconds)
    except ValueError as exc:
        parser.error(str(exc))

    if args.json:
        print(json.dumps(stats, indent=2))
        return

    if stats["runs"] == 1:
        print(f"RTF: {stats['median_rtf']:.4f}")
    else:
        print(
            f"Median RTF ({stats['runs']} runs): {stats['median_rtf']:.4f} "
            f"(min {stats['min_rtf']:.4f}, p95 {stats['p95_rtf']:.4f}, max {stats['max_rtf']:.4f})"
        )
    throughput = stats["throughput_x"]
    print(f"Throughput: {throughput:.2f}x real time" if math.isfinite(throughput) else "Throughput: instantaneous")
    print(f"Interpretation: {stats['interpretation']}")


if __name__ == "__main__":
    main()
