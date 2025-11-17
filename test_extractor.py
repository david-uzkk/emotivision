from src.extractor.video_extractor import extract_frames

VIDEO_PATH = "data/input/video.mp4"
OUTPUT_DIR = "data/frames/teste_001"

print("🎬 EmotiVision - Starting frame extraction test...")
print("="*50)

try:
    frames = extract_frames(VIDEO_PATH, OUTPUT_DIR, fps=1)

    print("✅ Frame extraction test completed successfully.")
    print(f"📊 Total frames extracted: {len(frames)}")
    print("Saves at: {OUTPUT_DIR}")

except Exception as e:
    print("❌ Frame extraction test failed.")
    print(f"Error: {e}")