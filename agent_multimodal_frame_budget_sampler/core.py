"""Core multimodal frame budget sampler implementation."""
from typing import List

class VideoFrame:
    def __init__(self, frame_id: int, timestamp: float, pixel_hash: int):
        self.frame_id = frame_id
        self.timestamp = timestamp
        self.pixel_hash = pixel_hash

class TemporalMotionFilter:
    @staticmethod
    def difference_score(f1: VideoFrame, f2: VideoFrame) -> float:
        # XOR bit count difference
        diff = f1.pixel_hash ^ f2.pixel_hash
        return bin(diff).count("1") / 32.0

class FrameBudgetSampler:
    def __init__(self, min_motion_threshold: float = 0.15, max_budget_frames: int = 10):
        self.min_motion_threshold = min_motion_threshold
        self.max_budget_frames = max_budget_frames

    def sample_frames(self, frames: List[VideoFrame]) -> List[VideoFrame]:
        if not frames:
            return []

        sampled = [frames[0]]  # Always retain first frame
        last_kept = frames[0]

        for f in frames[1:]:
            motion = TemporalMotionFilter.difference_score(last_kept, f)
            if motion >= self.min_motion_threshold:
                sampled.append(f)
                last_kept = f
                if len(sampled) >= self.max_budget_frames:
                    break

        return sampled
