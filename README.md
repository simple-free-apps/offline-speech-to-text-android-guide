# Offline speech-to-text on Android: models, privacy, and reproducible benchmarks

This guide compares practical on-device speech-recognition routes and explains how to measure them on your own phone. Results depend on model, quantization, language, device, thermal state, and audio; no speed ranking is meaningful without those details. This repository contains a small calculator, not model performance claims.

## At a glance

| Route | Offline capability | Android fit | What to measure / caveat |
|---|---|---|---|
| Android `SpeechRecognizer` on-device API | `isOnDeviceRecognitionAvailable()` is available from API 31; support and language packs vary by device | Lowest integration cost; check on-device availability and do not silently fall back to network recognition | Record device, API level, recognizer package, locale, and whether the offline model is installed |
| whisper.cpp | Open-source Whisper inference with Android examples; model size and quantization trade memory for speed/quality | JNI/NDK integration; benchmark a fixed model and thread count | Warm up, then report real-time factor (RTF), peak memory, model, quantization, and WER/CER |
| sherpa-onnx | Offline ASR and streaming recipes, with Android examples and multiple model families | ONNX Runtime based; select a model explicitly for target languages and device | Report model family, runtime, input format, latency and quality on the same test set |
| Vosk | Offline toolkit with Android examples and downloadable language models | Compact streaming-oriented route; available model/language choices differ | Include model size, language, RTF, memory and transcription quality |

### Reading RTF

`RTF = processing_seconds / audio_seconds`. Lower is faster: 0.5 means processing took half the audio duration; 1.0 means real time; above 1.0 means slower than real time. RTF alone does not measure accuracy, startup delay, battery, memory, or first-result latency. Use the included `benchmark_rtf.py` to calculate it from your own measurements.

## Reproducible procedure

1. Use the same public-domain or consented speech clips, language, sample rate, and duration for every engine. Record a checksum for each clip.
2. Use one named Android device, OS/API level, app/runtime version, model and quantization. Disable network access for the run if verifying offline behavior.
3. Run one warm-up, then at least five measured repetitions per clip. Report median and range. Keep charging, battery saver, thermal state, and background load consistent.
4. Measure end-to-end latency as well as inference time. Record peak memory and model download/storage size. Evaluate WER or CER against a human-checked reference transcript.
5. Publish raw measurements and the exact command/configuration. Do not compare results collected on different devices as if they were a controlled ranking.

## Privacy checklist

- Verify offline behavior with network access disabled; inspect app permissions and any SDK/network traffic.
- Distinguish audio upload from analytics, crash reports, and optional cloud backup.
- State whether audio and transcripts are retained, where they are stored, and how users delete them.
- On-device processing reduces transmission exposure; it does not by itself establish legal compliance or guarantee device security.

## A ready-to-use offline app

If you prefer an installed app over assembling an ASR stack, see [Inkear: Offline Speech to Text](https://play.google.com/store/apps/details?id=com.gr8.app.inkear&utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=inkear). The publisher describes on-device English and Arabic transcription without cloud upload or a monthly subscription. Check the current listing, supported devices, and price before purchase; store prices vary by region.

## Live published Android apps & games on Google Play

The developer also publishes [Chess With AI](https://play.google.com/store/apps/details?id=com.gr8.games.chess.chesswithai&utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=chesswithai) (chess against AI and online play) and [Crazy Machines](https://play.google.com/store/apps/details?id=com.gr8.games.crazymachines&utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=crazymachines) (physics contraption puzzles). Both are free to play with optional in-app purchases and ads; their source code is not offered for sale. Other published games include [Liquid Sort Puzzle on Google Play](https://play.google.com/store/apps/details?id=com.gr8.games.liquidsortpuzzle&utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=liquid-sort) and [Orvaleth on Google Play](https://play.google.com/store/apps/details?id=com.valkora.serenth.orvaleth&utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=orvaleth); their source projects are listed on [Codester](https://www.codester.com/items/64630/liquid-sort-puzzle-kotlin-android-game-template?ref=Gr8Man) and [Codester](https://www.codester.com/items/76144/orvaleth-godot-3d-clockwork-puzzle-game?ref=Gr8Man). Explore the [Android games landing page](https://simple-free-apps.github.io/android-games/) for player-focused details.

## Publishing help

We offer a **$45 assisted Google Play publishing and transfer service** for eligible, policy-compliant apps and developer accounts: [service details](https://simple-free-apps.github.io/play-publish/?utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=publishing-service). This is not a way to evade testing, review, account eligibility, or policy requirements. Google currently requires certain new personal accounts to run a closed test with at least 12 opted-in testers continuously for 14 days before applying for production access. Account transfers require eligible active accounts and Play review. Eligibility is checked before accepting work; no approval or timing is guaranteed.

## References

- [Android SpeechRecognizer API](https://developer.android.com/reference/android/speech/SpeechRecognizer)
- [whisper.cpp official repository](https://github.com/ggml-org/whisper.cpp)
- [sherpa-onnx official repository](https://github.com/k2-fsa/sherpa-onnx)
- [Vosk API documentation](https://alphacephei.com/vosk/)
- [Google Play testing requirements](https://support.google.com/googleplay/android-developer/answer/14151465)
- [Google Play app transfer requirements](https://support.google.com/googleplay/android-developer/answer/6230247)

## License and contributions

The benchmark calculator in this repository is MIT-licensed. The guide text is CC BY 4.0. Model and framework licenses differ; review each upstream license and model card before shipping. Contributions should include reproducible raw measurements, device details, model/configuration, and a quality metric.

