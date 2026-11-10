import sys
import unittest
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from audio_processing import SAMPLE_RATE, activity, prepare

class AudioProcessingTests(unittest.TestCase):
    def test_silent_or_invalid_recordings_fail(self):
        for samples in [np.array([]), np.zeros(1000), np.array([np.nan])]:
            with self.assertRaises(ValueError):prepare(samples)

    def test_preserves_quiet_consonants_and_internal_pauses(self):
        n=SAMPLE_RATE
        consonant=np.sin(np.arange(n//10)*.4)*.001
        vowel=np.sin(np.arange(n//5)*.1)*.15
        speech=np.concatenate([consonant,vowel,np.zeros(n//10),vowel,consonant])
        source=np.concatenate([np.zeros(n//5),speech,np.zeros(n//4)]).astype('<f4')
        out,stats=prepare(source)
        start,end=stats['trimStartSamples'],stats['trimEndSamples']
        ratio=out[np.argmax(abs(out))]/source[start:end][np.argmax(abs(out))]
        np.testing.assert_allclose(out, source[start:end]*ratio, atol=1e-7)
        self.assertEqual(start, round(n*.16))
        self.assertEqual(end, round(n*.975))
        self.assertLessEqual(abs(out).max(),10**(-3/20)+1e-7)
        first,last=activity(out)
        self.assertAlmostEqual(first/n,.04,places=3)
        self.assertAlmostEqual((len(out)-last)/n,.075,places=3)

    def test_adds_edge_padding_if_provider_has_none(self):
        samples=(np.sin(np.arange(4800)*.1)*.2).astype('<f4')
        out,stats=prepare(samples)
        self.assertEqual(len(out),len(samples)+2760)
        self.assertEqual(stats['trimStartSamples'],0)
        self.assertEqual(stats['trimEndSamples'],len(samples))
