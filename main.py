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
