"""CLI for agent-multimodal-frame-budget-sampler."""
import argparse
import sys
from .core import FrameBudgetSampler, VideoFrame

def main():
    parser = argparse.ArgumentParser(description="Agent Multimodal Frame Budget Sampler CLI")
    parser.add_argument("--demo", action="store_true", help="Run frame budget sampling demo")
    args = parser.parse_args()

    if args.demo:
        sampler = FrameBudgetSampler(min_motion_threshold=0.20, max_budget_frames=4)
        # Create 10 frames: 4 static, 1 motion, 3 static, 1 motion
        frames = [
            VideoFrame(1, 0.0, 0xAAAA0000),
            VideoFrame(2, 0.1, 0xAAAA0000), # static
            VideoFrame(3, 0.2, 0xAAAA0000), # static
            VideoFrame(4, 0.3, 0xFFFF0000), # motion!
            VideoFrame(5, 0.4, 0xFFFF0000), # static
            VideoFrame(6, 0.5, 0x0000FFFF)  # motion!
        ]
        kept = sampler.sample_frames(frames)
        print(f"[+] Total input frames: {len(frames)} -> Sampled keyframes: {len(kept)}")
        for k in kept:
            print(f"    Frame {k.frame_id} (t={k.timestamp:.1f}s, hash={hex(k.pixel_hash)})")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
