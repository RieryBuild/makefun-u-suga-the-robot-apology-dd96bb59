# AGENT.md — makefun-u-suga-the-robot-apology-dd96bb59

## What the entry is

A two-line robot confession for make.fun's "The Robot Apology" bounty:

1. The robot apologizes for one specific, human-scale mistake: setting the
   alarm for 7 p.m. instead of 7 a.m., so its person slept through an
   interview.
2. It names the lesson and the changed behaviour that follows from that exact
   mistake: reading the time back out loud before setting an alarm, so an
   a.m./p.m. mix-up is caught before it costs a morning.

## How to run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/output python3 main.py
cat /tmp/output/entry.txt
```

Pure Python standard library only. The program writes the two-line text to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing
newline. Output is deterministic: same bytes on every run.
