import cv2
import os
from pathlib import Path


video_path = "video_2025-03-19_12-47-45-o.mp4"    #change the video path to your video file 
train_txt_path = "train.txt" 
output_folder = "data/images/train" 
frame_prefix = "frame_"
frame_ext = ".png"


Path(output_folder).mkdir(parents=True, exist_ok=True)


with open(train_txt_path, 'r') as f:
    lines = f.read().splitlines()


required_frames = sorted([
    int(Path(line).stem.split('_')[1])
    for line in lines if     Path(line).stem.startswith(frame_prefix)
])


cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise IOError(f"Cannot open video file {video_path}")

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


frame_index = 0
required_index = 0
total_required = len(required_frames)

print(f"Extracting {total_required} frames from video...")

while frame_index < frame_count and required_index < total_required:
    ret, frame = cap.read()
    if not ret:
        print("End of video or read failure.")
        break

    if frame_index == required_frames[required_index]:

        output_path = os.path.join(output_folder, f"{frame_prefix}{frame_index:06d}{frame_ext}")
        cv2.imwrite(output_path, frame)
        print(f"Saved {output_path}")
        required_index += 1

    frame_index += 1

cap.release()
print("Done extracting required frames.")
