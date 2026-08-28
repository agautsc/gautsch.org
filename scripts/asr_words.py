#!/usr/bin/env python3
"""Step 1 of the audio sync: word-level timings from the episode audio.

Only the *timings* matter here -- the words this produces are thrown away.
scripts/align_audio.py matches them onto the published transcript, which is the
text the page actually shows. See that file for why this is alignment rather
than transcription.

Vosk rather than Whisper on purpose: a 40 MB model, CPU-only, no torch, and it
ran the 55-minute episode in 158 seconds (~21x realtime) on the Dell. Whisper
would have meant a torch install and an older Python; accuracy beyond "good
enough to match against known text" buys nothing, because the published wording
wins every disagreement.

Setup (the Dell ships Python 3.14, which has no vosk wheel):
    mise install python@3.12.14
    mise exec python@3.12.14 -- python -m venv .venv
    ./.venv/bin/pip install vosk
    curl -O https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
    unzip vosk-model-small-en-us-0.15.zip
    ffmpeg -i episode.mp3 -ac 1 -ar 16000 audio16k.wav

Usage:
    ./.venv/bin/python scripts/asr_words.py --wav audio16k.wav --out asr_words.json
"""
import argparse, json, time, wave

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wav", required=True, help="16 kHz mono WAV")
    ap.add_argument("--model", default="vosk-model-small-en-us-0.15")
    ap.add_argument("--out", default="asr_words.json")
    a = ap.parse_args()

    from vosk import Model, KaldiRecognizer, SetLogLevel
    SetLogLevel(-1)

    wf = wave.open(a.wav, "rb")
    if wf.getnchannels() != 1 or wf.getframerate() != 16000:
        raise SystemExit("expected 16 kHz mono; re-encode with ffmpeg -ac 1 -ar 16000")
    rec = KaldiRecognizer(Model(a.model), wf.getframerate())
    rec.SetWords(True)

    words, t0, n = [], time.time(), 0
    while True:
        data = wf.readframes(16000)
        if not data:
            break
        n += 1
        if rec.AcceptWaveform(data):
            words += json.loads(rec.Result()).get("result", [])
        if n % 300 == 0:
            print(f"  {n}s audio, {len(words)} words, {time.time()-t0:.0f}s elapsed", flush=True)
    words += json.loads(rec.FinalResult()).get("result", [])

    json.dump(words, open(a.out, "w"))
    end = words[-1]["end"] if words else 0
    print(f"{len(words)} words in {time.time()-t0:.0f}s; last timestamp {end:.1f}s -> {a.out}")

if __name__ == "__main__":
    main()
