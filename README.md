#**CODE IS KUMARAGURU COLLEGE OF TECHNOLOGY'S ASSESTS**#

# Vehicle Detection and Tracking Using YOLO

**Project Description**

This project implements a vehicle detection and tracking system using the YOLOv8 model. It detects vehicles (cars, buses, and trucks) in a video, tracks their movement, and identifies objects crossing predefined lines for counting purposes. The system processes video frames and draws bounding boxes and tracking IDs for detected vehicles.

---

**Features**

1. **Vehicle Detection with YOLOv8**
2. **Object Tracking using a Custom Tracker Class**
3. **Vehicle Counting Across Defined Lines**
4. **Real-time Visualization with OpenCV**

---

**Prerequisites**

1. **Python (3.x)**
2. **Libraries:**
   - OpenCV
   - pandas
   - cvzone
   - ultralytics (YOLOv8)
3. **Software:**
   - Any IDE or text editor (e.g., VS Code, PyCharm)
   - A video file (e.g., `tf.mp4` for testing)
4. **YOLOv8 Model:**
   - Pre-trained weights (`yolov8s.pt`)
5. **COCO Class Labels:**
   - A `coco.txt` file containing class labels.

---

**Installation Steps**

 1. Set Up Python Environment

Ensure Python is installed. You can download it from [Python.org](https://www.python.org/).

 2. Install Required Libraries

Run the following commands in the terminal or command prompt:

```bash
pip install opencv-python pandas cvzone ultralytics
```

 3. Clone or Copy the Project

Clone this repository or copy the project files into your workspace.

 4. Download YOLOv8 Pre-trained Weights

Download `yolov8s.pt` from the [Ultralytics Repository](https://github.com/ultralytics/ultralytics) and place it in the project directory.

 5. Add Video and Class Label Files

- Place your video file (e.g., `tf.mp4`) in the project directory.
- Ensure the `coco.txt` file (with COCO class labels) is also in the project directory.

---

**Project Structure**

```
VehicleTrackerProject/
├── tracker.py          # Custom tracker class for object tracking
├── main.py             # Main script for video processing
├── yolov8s.pt          # YOLOv8 pre-trained weights
├── tf.mp4              # Video file for testing
├── coco.txt            # COCO class labels
```

---

Running the Project

1. Run the Main Script

Run the following command to start the detection and tracking process:

```bash
python main.py
```

2. View the Output

The script will display the processed video with bounding boxes, vehicle counts, and tracking IDs. Press the `Esc` key to exit the video window.

---

How It Works

1. **YOLO Detection:**
   - YOLOv8 detects objects in video frames.
   - The detections are filtered to focus on cars, buses, and trucks.

2. **Object Tracking:**
   - A custom tracker class maintains IDs for detected objects.
   - Tracks object movements and matches objects across frames.

3. **Vehicle Counting:**
   - Counts vehicles crossing predefined lines using their center positions.

4. **Real-time Updates:**
   - Draws bounding boxes, tracking IDs, and counting lines on each frame.

---

**Troubleshooting**

- **Error: Video file does not exist:** Ensure `tf.mp4` is in the correct directory.
- **COCO class labels missing:** Verify `coco.txt` is in the project directory.
- **Performance issues:** Adjust frame skipping (e.g., `count % 3`) for better performance.

---

**Future Enhancements**

1. Improve detection accuracy by using YOLOv8 advanced features.
2. Add support for real-time camera input.
3. Extend tracking to additional object classes.
4. Integrate analytics for traffic flow monitoring.

---

**License**

This project is open-source and free to use.

