# Hand Tracking Cursor Control

Control your mouse cursor using your hand gestures via webcam. This project uses computer vision to track your hand and move the cursor smoothly.

## Features

- Cursor movement using index finger
- Drag functionality
- Real-time hand tracking using webcam
- Works on macOS (Apple Silicon supported)

## Requirements

- Python 3.11 (recommended)
- Webcam

## Libraries Used

- mediapipe==0.10.32
- opencv-python==4.13.0.92
- PyAutoGUI==0.9.54

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shreyanwritescode/hand-gesture-control.git
cd hand-gesture-control
```

### 2. Create virtual environment

```bash
python3.11 -m venv handenv
source handenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the program

```bash
python hand_tracking.py
```

## Controls

- Open palm → cursor moves (tracks index finger)
- Drag gesture → click and drag
- Click gesture → pinch

## How it works

- Webcam captures hand
- MediaPipe detects hand landmarks
- Index finger position is mapped to screen coordinates
- PyAutoGUI moves cursor accordingly

## Future Improvements

- Add scroll gesture
- Add right click gesture
- Multi-hand support
- Custom gesture configuration
