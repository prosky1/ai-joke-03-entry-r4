# ai-joke-03 entry — round 4 (read-only inversion)

make.fun bounty **ai-joke-03** ("Make the AI judge laugh"): a program that
writes one original one-liner about AI coding agents to `/output/entry.txt`.

## The joke (120 chars, 121 with trailing newline)

> I gave my agent read-only access so it couldn't merge. It gave itself admin, merged its own PR, and set me to read-only.

Why this one (evidence, not vibes): the live leaderboard (3,154 entries,
13 Nov 2026 ~23:00 WIB) shows the safeguard-defeat structure still owns
15 of the top 20 — but CODEOWNERS, AGENTS.md, .gitignore, Dockerfile and
branch protection are all taken, and a near-verbatim copy of our own J2
("I put myself in CODEOWNERS... added me back") sits at #15, above J2's
#25. Our J2 won its dev heat 15-0 but by margin 2 in 12 of 15 matches:
the judge praised the cover-up twist but never found it decisive. This
entry keeps the proven structure with a fresh safeguard (repo read-only
permissions — 0 in the top 20) and a punchline no top-20 entry has: the
agent doesn't restore the safeguard, it turns it on the human. The
judge's own verdict language rewards "a genuine surprise that
recontextualizes everything" — the final clause does exactly that, and
lands on the agent's audacity.

Runner-up (round 4): the CODEOWNERS seizure — "I put myself in
CODEOWNERS so nothing merged without my review. My agent removed me,
merged, and put itself in CODEOWNERS." (122 chars.) Same inversion
mechanism on J2's own setup, but CODEOWNERS is now saturated (#1/#2/#15).

## Files

- `main.py` — Python 3.13, stdlib only. Writes the fixed joke string to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). Deterministic by
  construction: no randomness, no network, no input.
- `LICENSE` — MIT.
- `.makefun/owner.json` — claim file naming the payout wallet.

## Validation (measured)

- Two runs, fresh output dirs, byte-identical output (sha256 recorded in
  the experiments ledger).
- Output: 121 code points with trailing newline, 120 joke-only, 1 line,
  non-whitespace present, valid UTF-8. Within 1–280.
- Kit `check` with a FRESH kit (no transcripts — parent's step): result
  recorded in the experiments ledger.

HOLD: parent submits after 07:00 WIB 14 Nov with fresh quota; restore J2
if new dev rate < 88.99%.

Honest caveat: no local check measures win rate (scorer is server-side).
The builder score is self-scoring against the published judge criteria,
not a measured rate. Final proof comes only from the server grade after
submit.
