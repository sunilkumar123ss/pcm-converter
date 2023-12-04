import unittest
try:
    from .main import decode_pcm16, encode_pcm16
except ImportError:
    from main import decode_pcm16, encode_pcm16

class PcmTests(unittest.TestCase):

    def test_known_bytes(self):
        self.assertEqual(encode_pcm16([[-1], [0], [0.5], [1]]), b'\x00\x80\x00\x00\x00@\xff\x7f')
        self.assertEqual(decode_pcm16(b'\x00\x80\xff\x7f'), [[-1], [32767 / 32768]])
