from src.detector.emotion_detector import (
    detect_emotions_in_images,
    process_folder,
    save_results
)

print("🧠 EmotiVision - Running tests for emotion_detector.py")
print("="*50)

# Test data paths
FOLDER_FRAMES = "data/frames/teste_001"
OUTPUT_PATH = "data/results/test_emotion_detection.json"

try:
    # Test 1: Detect emotions in a single image
    print("\n📸 Test 1: Detect emotions in a single image")

    first_image = f"{FOLDER_FRAMES}/frame_0000.jpg"
    result_single = detect_emotions_in_images(first_image)

    if result_single['success']:
        print("✅ Emotion detection successful for single image.")
        print(f"    Emotion dominant: {result_single['dominant_emotion']}")
        print(f"    All emotions")
        for emotion, score in result_single['emotions'].items():
            print(f"      - {emotion}: {score*100:.2f}")
    else:
        print("❌ Erro: {result_single['error']}")

    # Save single result to output file
    print("\n📸 Test 2: Process batch of images in folder")

    complete_results = process_folder(FOLDER_FRAMES)

    # Save batch results to output file
    save_results(complete_results, OUTPUT_PATH)

    print(f"\n🎉 All tests completed!")

except Exception as e:
    print(f"\n❌ Error: {e}")