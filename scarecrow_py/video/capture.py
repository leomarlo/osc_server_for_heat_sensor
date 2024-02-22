import cv2
import os
import random
from config import CONFIG


def check_webcam_input(camera_index=0):
    """
    Attempts to capture a frame from the webcam.
    
    Args:
    - camera_index (int): Index of the webcam to use.
    
    Returns:
    - bool: True if a frame is captured, False otherwise.
    - frame: The captured frame, or None if no frame was captured.
    """
    # Initialize the webcam
    cap = cv2.VideoCapture(camera_index)
    
    # Attempt to capture a frame
    ret, frame = cap.read()
    print("ret:", ret)
    print("type of frame:", type(frame))
    
    # Release the webcam
    cap.release()
    
    # Return both the success flag and the captured frame
    return ret, frame


def get_random_frame_from_video(video_file):
    """
    Opens a video file, counts the number of frames, picks a random frame,
    and returns it with a boolean flag indicating success.
    
    Args:
    - video_file (str): Path to the video file.
    
    Returns:
    - bool: True if a frame is successfully retrieved, False otherwise.
    - frame: The randomly selected frame, or None if retrieval was unsuccessful.
    """
    # Try to open the video file
    cap = cv2.VideoCapture(video_file)
    
    if not cap.isOpened():
        print("Error opening video file.")
        return False, None
    
    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if total_frames <= 0:
        print("Video file contains no frames.")
        cap.release()
        return False, None
    
    # Generate a random frame number
    random_frame_number = random.randint(0, total_frames - 1)
    
    # Set the current frame position to the random frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame_number)
    
    # Read the frame
    ret, frame = cap.read()
    
    # Release the video capture object
    cap.release()
    
    # Check if the frame was successfully read
    if not ret:
        print("Failed to retrieve the frame.")
        return False, None
    
    print(f"Retrieved frame number {random_frame_number} out of {total_frames} total frames.")
    return True, frame


def capture_video_frame():
    """
    Captures video from the default webcam and saves it to a file.
    """
    if CONFIG.ENVIRONMENT == "production":
        # Use the default webcam
        camera_index = CONFIG.CAMERA_ID
        ret, frame = check_webcam_input(camera_index)
        return frame
    else:
        video_file_name = CONFIG.TEST_VIDEO_FILE
        path = os.path.join(os.path.dirname(__file__), video_file_name)
        ret, frame = get_random_frame_from_video(path)
        return frame