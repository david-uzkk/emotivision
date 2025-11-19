from deepface import DeepFace
import cv2
import os
from pathlib import Path
import json

from tqdm import tqdm

def detect_emotions_in_images(image_patch):
    """
    """

    # Perform emotion analysis using DeepFace
    try:
        result = DeepFace.analyze(
            img_path=image_patch,
            actions=['emotion'],
            enforce_detection=False,
            silent=True
        )

        # If multiple faces are detected, take the first one
        if isinstance(result, list):
            result = result[0]
        
        emotions = result['emotion']
        emotion_dominant = result['dominant_emotion']

        normalized_emotions = {
            emotion: valor / 100.0
            for emotion, valor in emotions.items()
        }

        return {
            'success': True,
            'emotions': normalized_emotions,
            'dominant_emotion': emotion_dominant,
            'image_path': image_patch
        }
    
    # Handle exceptions (e.g., no face detected)
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'image_path': image_patch
        }

# Process a batch of images for emotion detection
def process_batch(list_images, show_progress=True):
    """
    """
    print(f"\n🧠 Analyzing {len(list_images)} frames...")

    results = []

    # Show progress bar if enabled
    if show_progress:
        iterator = tqdm(list_images, desc="Detecting Emotions")
    else:
        iterator = list_imagesmacarrãopas

    for image_path in iterator:
        result = detect_emotions_in_images(image_path)
        results.append(result)

    success = sum(1 for r in results if r['success'])
    fails = len(results) - success

    print(f"✅ Emotion detection completed!")
    print(f"📊 Successful detections: {success}/{len(results)}")
    if fails > 0:
        print(f"⚠️ Fails: {fails}")

    return results

def process_folder(folder_frames)
    """
    """
    extensions = {'.jpg', '.jpeg', '.png'}
    list_images = []
    for file in sorted(os.listdir(folder_frames)):

        if any(file.lower().endswith(ext) for ext in extensions):
            dir_complete = os.path.join(folder_frames, file)
            list_images.append(dir_complete)
    print(f"📁 Found {len(list_images)} images in folder {folder_frames}")

    if len(list_images) == 0:
        raise Exception("No images found in the specified folder.")
    
    return process_batch(list_images):