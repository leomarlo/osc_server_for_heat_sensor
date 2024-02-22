import cv2

def save_frame_as_image(frame, filename="test_image.png"):
    """
    Saves the given frame as an image file.
    
    Args:
    - frame: The frame to save.
    - filename (str): The filename for the saved image.
    """
    # Check if frame is not None
    if frame is not None:
        # Save the frame as an image file
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
    else:
        print("No frame to save.")
