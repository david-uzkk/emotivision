import cv2
import os
from pathlib import Path

def extract_frames(video_path, output_dir, fps=1):
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    print(f"📁 Extracting frames from: {video_path}")

    # Open the video file
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Could not open video {video_path}")
    print("✅ Video opened successfully.")
    fps_original = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps_original  

    print(f"🎬 Original FPS: {fps_original}")
    print(f"🎬 Total Frames: {total_frames}")
    print(f"⏱️ Duration: {duration:.2f} seconds")

    # Calculate frame interval
    frame_interval = int(fps_original / fps)
    print(f"⚙️ Frame interval for extraction: {frame_interval}")

    frames_saved = []

    count_extracted = 0

    count_read = 0

    print("🔄 Starting frame extraction...")

    # Read through the video frames
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # Determine if this frame should be saved
        if count_read % frame_interval == 0:
            file_name = f"frame_{count_extracted:04d}.jpg"
            dir_complete = os.path.join(output_dir, file_name)
            cv2.imwrite(dir_complete, frame)
            frames_saved.append(dir_complete)
            count_extracted += 1
            if count_extracted % 10 == 0:
                print(f"{count_extracted} frames extracted...")
        
        count_read += 1
    video.release()
    print(f"✅ Frame extraction completed.")
    print(f"📊 Total frames extracted: {count_extracted}")
    return frames_saved