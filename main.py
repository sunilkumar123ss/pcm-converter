"""Convert signed PCM16 little-endian bytes and normalized samples."""
import argparse
import json
import math
from pathlib import Path
import struct

def decode_pcm16(data, channels=1):
    if isinstance(channels, bool) or not isinstance(channels, int) or channels < 1:
        raise ValueError('channels must be a positive integer')
    if not isinstance(data, bytes) or len(data) % (2 * channels):
        raise ValueError('PCM bytes must contain complete interleaved frames')
    values = [x[0] / 32768 for x in struct.iter_unpack('<h', data)]
    return [values[i:i + channels] for i in range(0, len(values), channels)]

def encode_pcm16(frames, channels=1, clip=False):
    if isinstance(channels, bool) or not isinstance(channels, int) or channels < 1 or (not isinstance(clip, bool)):
        raise ValueError('Invalid channel count or clip flag')
    if not isinstance(frames, list):
        raise ValueError('frames must be a list')
    output = bytearray()
    for frame in frames:
        if not isinstance(frame, list) or len(frame) != channels:
            raise ValueError('Each frame must match channels')
        for value in frame:
            if isinstance(value, bool) or not isinstance(value, (int, float)) or (not math.isfinite(value)):
                raise ValueError('Samples must be finite numbers')
            if abs(value) > 1 and (not clip):
                raise ValueError('Sample outside [-1,1]; use clip explicitly')
            value = max(-1, min(1, value))
            integer = max(-32768, min(32767, round(value * 32768)))
            output.extend(struct.pack('<h', integer))
    return bytes(output)
