import os
import cv2
from ultralytics import YOLO
import pandas as pd
import cvzone
from tracker import Tracker

# Load YOLO model
model = YOLO('yolov8s.pt')
print("YOLO model loaded successfully.")

# Path to the local video file
video_path = r"tf.mp4"  # Update this with your actual video file name

# Check if the file exists
if not os.path.exists(video_path):
    print(f"Error: The video file '{video_path}' does not exist.")
    exit()

# Open the video file
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open the video.")
    exit()

# Read COCO class labels from coco.txt
with open("coco.txt", "r") as my_file:
    class_list = my_file.read().split("\n")

# Initialize tracker
tracker = Tracker()

# Set detection lines and offsets
cy1 = 184  # Upper line
cy2 = 209  # Lower line
offset = 8  # Buffer offset
count = 0  # Frame counter

# Main loop to process video frames
while True:
    ret, frame = cap.read()
    if not ret:
        break

    count += 1
    if count % 3 != 0:
        continue  # Skip frames for performance

    frame = cv2.resize(frame, (1020, 500))

    # Run YOLO object detection
    results = model.predict(frame)
    detections = results[0].boxes.data
    px = pd.DataFrame(detections).astype("float")

    # Initialize lists for detected objects
    car_list = []
    bus_list = []
    truck_list = []

    # Separate detections based on their class
    for _, row in px.iterrows():
        x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
        class_id = int(row[5])
        class_name = class_list[class_id]

        if 'car' in class_name:
            car_list.append([x1, y1, x2, y2])
        elif 'bus' in class_name:
            bus_list.append([x1, y1, x2, y2])
        elif 'truck' in class_name:
            truck_list.append([x1, y1, x2, y2])

    # Update and draw bounding boxes for cars
    car_bboxes = tracker.update(car_list)
    for bbox in car_bboxes:
        x3, y3, x4, y4, _ = bbox  # We don't need to display the ID
        cx, cy = (x3 + x4) // 2, (y3 + y4) // 2
        cv2.circle(frame, (cx, cy), 4, (255, 0, 0), -1)
        cv2.rectangle(frame, (x3, y3), (x4, y4), (255, 0, 255), 2)

    # Draw lines to count vehicles passing
    cv2.line(frame, (1, cy1), (1018, cy1), (0, 255, 0), 2)
    cv2.line(frame, (3, cy2), (1016, cy2), (0, 0, 255), 2)

    # Display the processed frame
    cv2.imshow("RGB", frame)

    # Exit when 'Esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release video and close windows
cap.release()
cv2.destroyAllWindows()
