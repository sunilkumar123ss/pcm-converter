# PCM16 Codec Utility

**Demo/starter · Python standard library only.**

Convert normalized interleaved frames to signed PCM16 little-endian bytes and decode them back.

All bundled fixtures are synthetic and contain no customer data or secrets.

## Run

Use Python 3.9 or later (validated with Python 3.9.6). No installation or network access is needed. From this project directory:

```sh
python3 main.py
python3 main.py --input fixtures/stereo.pcm --channels 2
python3 -m unittest -v
```

The default CLI executes a deterministic working demo. Invalid input exits with a readable error and nonzero status.

## Behavior

The CLI reads raw headerless PCM and uses `--channels` to interpret its layout. It prints decoded frames and their count. The Python `encode_pcm16` API returns bytes; out-of-range input is rejected unless `clip=True` is explicitly requested. Incomplete interleaved frames are rejected.

## Limits and optional provider boundary

Scaling uses 32768 with integer saturation: +1 encodes 32767, while -1 encodes -32768. Channel count must be known externally. This does not handle compressed codecs. The binary fixture contains eight explicitly chosen synthetic signed integers.

This can sit at a provider’s PCM input boundary. It does not contact a provider or synthesize/transcribe speech.

## Tests

`test_main.py` checks fixed expected results, edge cases and invalid inputs with `unittest`. These tests validate the local implementation, not real-world speech accuracy or production readiness. Run `python3 verify.py` to repeat this repository’s checks.

## Scope

This is an educational implementation with synthetic fixtures. Run the tests and inspect the documented limits before adapting it.

## Repository checks

```sh
python3 verify.py
```

This runs the isolated test suite, synthetic example, and CLI help. The included GitHub Actions workflow repeats these checks when the repository is published. No hosted CI result is claimed by the local verification report.
