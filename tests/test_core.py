"""Unit tests for agent-multimodal-frame-budget-sampler."""
import unittest
from agent_multimodal_frame_budget_sampler.core import FrameBudgetSampler, VideoFrame

class TestFrameBudgetSampler(unittest.TestCase):
    def setUp(self):
        self.sampler = FrameBudgetSampler(min_motion_threshold=0.20)

    def test_static_frames_pruned(self):
        frames = [
            VideoFrame(1, 0.0, 0x12345678),
            VideoFrame(2, 1.0, 0x12345678), # identical
            VideoFrame(3, 2.0, 0x87654321)  # motion
        ]
        sampled = self.sampler.sample_frames(frames)
        self.assertEqual(len(sampled), 2)
        self.assertEqual(sampled[0].frame_id, 1)
        self.assertEqual(sampled[1].frame_id, 3)
