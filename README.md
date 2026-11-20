# Offline speech-to-text on Android: models, privacy, and reproducible benchmarks

This guide compares practical on-device speech-recognition routes and explains how to measure them cleanly on Android hardware. Results depend heavily on model size, quantization, language, chipset, thermal state, and audio profile; no speed ranking is meaningful without those details.

**Contents:** [At a glance](#at-a-glance) · [RTF calculator CLI](#reading-rtf--running-the-calculator) · [Reproducible procedure](#reproducible-procedure) · [Privacy checklist](#privacy-checklist) · [Ready-to-use app (Inkear)](#a-ready-to-use-offline-app-inkear) · [Studio catalog & services](#more-from-gr8-apps--games-studio)

## At a glance

| Route | Offline capability | Android fit | What to measure / caveat |
|---|---|---|---|
| Android `SpeechRecognizer` on-device API | `isOnDeviceRecognitionAvailable()` is available from API 31; support and language packs vary by device | Lowest integration cost; check on-device availability and do not silently fall back to network recognition | Record device, API level, recognizer package, locale, and whether the offline model is installed |
| whisper.cpp | Open-source Whisper inference with Android examples; model size and quantization trade memory for speed/quality | JNI/NDK integration; benchmark a fixed model and thread count | Warm up, then report real-time factor (RTF), peak memory, model, quantization, and WER/CER |
| sherpa-onnx | Offline ASR and streaming recipes, with Android examples and multiple model families | ONNX Runtime based; select a model explicitly for target languages and device | Report model family, runtime, input format, latency and quality on the same test set |
| Vosk | Offline toolkit with Android examples and downloadable language models | Compact streaming-oriented route; available model/language choices differ | Include model size, language, RTF, memory and transcription quality |

### Reading RTF & running the calculator

`RTF = processing_seconds / audio_seconds`. Lower is faster: `0.5` means processing took half the audio duration; `1.0` means real time; above `1.0` means slower than real time. RTF alone does not measure accuracy, startup delay, battery, memory, or first-result latency.

Run the bundled `benchmark_rtf.py` script with `<audio_seconds>` and `<processing_seconds>`:

```bash
python benchmark_rtf.py 30 4.5
```

Example output:

```text
RTF: 0.1500
Throughput: 6.67x real time
Interpretation: faster than real time
```

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

## A ready-to-use offline app: Inkear

![Inkear: Offline Speech to Text](https://simple-free-apps.github.io/assets/inkear/feature.jpg)

If you prefer an installed Android app over compiling an NDK/ASR stack yourself, see **[Inkear: Offline Speech to Text](https://play.google.com/store/apps/details?id=com.gr8.app.inkear&utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=inkear)**:

- **On-device Whisper inference:** Runs locally on Android; audio stays on your phone with no cloud upload, according to the store listing.
- **~99 spoken languages & Arabic RTL:** Supports English, Arabic with RTL display, automatic language detection, and 40+ UI languages.
- **Flexible import & export:** Record directly, import audio/video, or share voice notes from WhatsApp and Telegram; export TXT, Markdown, SRT, VTT, PDF, or JSON.
- **One-time purchase model:** No monthly subscription or minute cap (check current local store price and supported devices in Google Play).

Compare your monthly transcription spend with the interactive **[Inkear break-even calculator & studio showcase](https://simple-free-apps.github.io/#inkear)**.

## More from Gr8 Apps & Games Studio

- **[Chess With Sara: Learn & Play](https://play.google.com/store/apps/details?id=com.gr8.games.chess.chesswithai&utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=chesswithsara)** — Personal coach Sara explains moves by voice and writing in English and Arabic, plus 50,000 puzzles, online arenas, and 12 Stockfish 18 levels (free to play, optional IAP & ads; source code not for sale).
- **[Psycho Mechanics: Physics](https://play.google.com/store/apps/details?id=com.gr8.games.crazymachines&utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=psychomechanics)** — Contraption puzzle builder with gears, ramps, magnets, and a free-build workshop; core gameplay works offline (free to play, optional IAP & ads; source code not for sale).
- **[ChromaCircuit Starter (Free Open Source)](https://github.com/simple-free-apps/android-compose-puzzle-starter)** — 5-level Jetpack Compose & Canvas puzzle game starter with EN/AR RTL and procedural `AudioTrack` SFX.
- **Live Play Demos with Commercial Source Kits:** [Liquid Sort Puzzle](https://play.google.com/store/apps/details?id=com.gr8.games.liquidsortpuzzle&utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=liquid-sort) ([Codester](https://www.codester.com/items/64630/liquid-sort-puzzle-kotlin-android-game-template?ref=Gr8Man)) and [Orvaleth: Clockwork Spires](https://play.google.com/store/apps/details?id=com.valkora.serenth.orvaleth&utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=orvaleth) ([Codester](https://www.codester.com/items/76144/orvaleth-godot-3d-clockwork-puzzle-game?ref=Gr8Man) · [Payhip](https://payhip.com/b/hWmcv)). See the full **[Android games showcase](https://simple-free-apps.github.io/android-games/)** or the **[Developer catalog](https://simple-free-apps.github.io/#catalog)**.

*Disclosure: Codester links above include the publisher's `?ref=Gr8Man` referral code.*

## Publishing help ($45)

For developers with eligible, policy-compliant Android apps and active developer accounts, we offer an **[assisted Google Play publishing and app transfer service](https://simple-free-apps.github.io/play-publish/?utm_source=offline-speech-to-text-android-guide&utm_medium=readme&utm_campaign=publishing-service)** ($45 after eligibility check). This does not bypass Google's closed-testing requirements (e.g., 12 testers for 14 continuous days on applicable new personal accounts), verification, or Play review.

## References

- [Android SpeechRecognizer API](https://developer.android.com/reference/android/speech/SpeechRecognizer)
- [whisper.cpp official repository](https://github.com/ggml-org/whisper.cpp)
- [sherpa-onnx official repository](https://github.com/k2-fsa/sherpa-onnx)
- [Vosk API documentation](https://alphacephei.com/vosk/)
- [Google Play testing requirements](https://support.google.com/googleplay/android-developer/answer/14151465)
- [Google Play app transfer requirements](https://support.google.com/googleplay/android-developer/answer/6230247)

## License and contributions

The benchmark calculator in this repository is MIT-licensed. The guide text is CC BY 4.0. Model and framework licenses differ; review each upstream license and model card before shipping. Contributions should include reproducible raw measurements, device details, model/configuration, and a quality metric.
