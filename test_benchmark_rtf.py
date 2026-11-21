#!/usr/bin/env python3
"""Unit tests for benchmark_rtf.py."""
import unittest

from benchmark_rtf import compute_stats


class BenchmarkRtfTests(unittest.TestCase):
    def test_single_run_faster_than_realtime(self):
        stats = compute_stats(30.0, [4.5])
        self.assertEqual(stats["runs"], 1)
        self.assertAlmostEqual(stats["median_rtf"], 0.15)
        self.assertAlmostEqual(stats["throughput_x"], 30.0 / 4.5)
        self.assertEqual(stats["interpretation"], "faster than real time")

    def test_multi_run_median_and_p95(self):
        stats = compute_stats(60.0, [12.0, 9.0, 15.0, 10.5, 18.0])
        self.assertEqual(stats["runs"], 5)
        self.assertAlmostEqual(stats["min_rtf"], 0.15)
        self.assertAlmostEqual(stats["median_rtf"], 0.20)
        self.assertAlmostEqual(stats["p95_rtf"], 0.30)
        self.assertEqual(stats["interpretation"], "faster than real time")

    def test_invalid_inputs_raise_value_error(self):
        with self.assertRaises(ValueError):
            compute_stats(0.0, [1.0])
        with self.assertRaises(ValueError):
            compute_stats(10.0, [-0.5])


if __name__ == "__main__":
    unittest.main()
