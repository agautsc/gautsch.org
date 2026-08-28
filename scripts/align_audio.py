#!/usr/bin/env python3
"""Align the episode audio to the PUBLISHED transcript and emit per-paragraph timings.

This is deliberately not "transcribe the audio and show that". The highlights and
paragraphs on /research/ are anchored in the published Mercatus transcript, so the
timings have to land on *that* text. Whisper-style output would carry its own
wording -- different punctuation, different sentence breaks, filler words the
editors removed -- and the highlights would drift off the words they belong to.

So: run a cheap ASR pass to get word-level timings, then align that word stream to
the published one with a sequence match. Matched words donate their timestamp;
gaps are interpolated between their neighbours. Adam described this shape himself
("run a transcription run to get the time stamps, then run a matching with the
written transcript").

Input : asr_words.json  -- [{"word","start","end"}, ...] from any word-level ASR
Output: static/research/timings.json -- [{"para": n, "start": s, "end": e}, ...]

Usage: python3 scripts/align_audio.py --asr PATH [--write]
"""
import argparse, difflib, io, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from import_research import load_pages, read, TRANSCRIPT   # reuse the same parse

NORM = re.compile(r"[^a-z0-9']+")

def norm(w):
    return NORM.sub("", w.lower())

def transcript_words(vault):
    """The published word stream, each word tagged with its paragraph index."""
    raw = read(os.path.join(vault, TRANSCRIPT))
    start = raw.find("**TYLER COWEN:** Hello, everyone")
    body = raw[start:]
    for stop in ("\n---\n\n# Review Session", "\n# Review Session"):
        k = body.find(stop)
        if k > 0:
            body = body[:k]
    out, paras = [], 0
    for chunk in body.split("\n\n"):
        p = chunk.strip()
        if not p:
            continue
        # drop Adam's margin notes and the speaker label; keep only spoken words
        p = re.sub(r"\s*\*[^*\n]+\*\s*\*\*→ \[\[.+?\]\]\*\*", "", p)
        p = re.sub(r"\s*\*\*→ \[\[.+?\]\]\*\*", "", p)
        p = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", p)
        p = re.sub(r"^\*\*[A-Z][A-Z\s.]+:\*\*", "", p)
        p = p.replace("==", "")
        for w in p.split():
            n = norm(w)
            if n:
                out.append((n, paras))
        paras += 1
    return out, paras

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--asr", required=True)
    ap.add_argument("--vault", default="/home/agautsc/Documents/ARG Full")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    asr = json.load(io.open(a.asr, encoding="utf-8"))
    aw = [norm(w["word"]) for w in asr]
    tw, nparas = transcript_words(a.vault)
    print(f"asr words: {len(aw)}   transcript words: {len(tw)}   paragraphs: {nparas}")

    sm = difflib.SequenceMatcher(None, aw, [w for w, _ in tw], autojunk=False)
    blocks = sm.get_matching_blocks()
    matched = sum(b.size for b in blocks)
    print(f"matched words: {matched} ({matched/max(1,len(tw)):.1%} of the transcript)")

    # every matched transcript word takes its timestamp from the ASR word
    t_start = [None] * len(tw)
    t_end = [None] * len(tw)
    for b in blocks:
        for k in range(b.size):
            t_start[b.b + k] = asr[b.a + k]["start"]
            t_end[b.b + k] = asr[b.a + k]["end"]

    # fill gaps by linear interpolation between the surrounding anchors
    known = [i for i, v in enumerate(t_start) if v is not None]
    known_set = set(known)
    if not known:
        sys.exit("no alignment anchors found -- the ASR and the transcript did not match")
    for idx in range(len(tw)):
        if t_start[idx] is not None:
            continue
        import bisect
        j = bisect.bisect_left(known, idx)
        lo = known[j - 1] if j > 0 else None
        hi = known[j] if j < len(known) else None
        if lo is None:
            t_start[idx] = t_start[known[0]]
        elif hi is None:
            t_start[idx] = t_end[known[-1]]
        else:
            span = (t_start[hi] - t_end[lo]) or 0
            t_start[idx] = t_end[lo] + span * ((idx - lo) / (hi - lo))
        t_end[idx] = t_start[idx]

    # collapse to paragraphs: the unit the page actually highlights
    out = []
    for p in range(nparas):
        ix = [i for i, (_, pi) in enumerate(tw) if pi == p]
        if not ix:
            out.append({"para": p, "start": None, "end": None, "anchors": 0})
            continue
        out.append({
            "para": p,
            "start": round(min(t_start[i] for i in ix), 2),
            "end": round(max(t_end[i] for i in ix), 2),
            "anchors": sum(1 for i in ix if i in known_set),
        })

    # monotonicity: a paragraph must not start before the one before it
    bad = sum(1 for i in range(1, len(out))
              if out[i]["start"] is not None and out[i-1]["start"] is not None
              and out[i]["start"] < out[i-1]["start"])
    print(f"paragraphs timed: {sum(1 for o in out if o['start'] is not None)}/{nparas}"
          f"   out-of-order: {bad}")
    weak = [o["para"] for o in out if o["anchors"] == 0]
    print(f"paragraphs with no real anchor (pure interpolation): {len(weak)}"
          + (f" -> {weak[:10]}" if weak else ""))
    if out and out[-1]["end"]:
        print(f"last paragraph ends at {out[-1]['end']:.0f}s")

    if not a.write:
        print("\n[dry-run] nothing written. pass --write")
        return
    # static/, not data/: Hugo does not publish data files, and the page fetches
    # this at runtime rather than inlining it against the page-weight budget
    d = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static", "research")
    os.makedirs(d, exist_ok=True)
    json.dump(out, io.open(os.path.join(d, "timings.json"), "w", encoding="utf-8"))
    print(f"wrote static/research/timings.json ({len(out)} paragraphs)")

if __name__ == "__main__":
    main()
