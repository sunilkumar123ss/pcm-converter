import unittest
try:
    from .main import decode_pcm16, encode_pcm16
except ImportError:
    from main import decode_pcm16, encode_pcm16

class PcmTests(unittest.TestCase):

    def test_known_bytes(self):
        self.assertEqual(encode_pcm16([[-1], [0], [0.5], [1]]), b'\x00\x80\x00\x00\x00@\xff\x7f')
        self.assertEqual(decode_pcm16(b'\x00\x80\xff\x7f'), [[-1], [32767 / 32768]])

    def test_stereo_roundtrip(self):
        frames = [[-0.5, 0.5], [0, 0.25]]
        self.assertEqual(decode_pcm16(encode_pcm16(frames, 2), 2), frames)

    def test_clipping_is_explicit(self):
        with self.assertRaises(ValueError):
            encode_pcm16([[2]])
        self.assertEqual(encode_pcm16([[2]], clip=True), b'\xff\x7f')
