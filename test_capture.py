# Import the function
from scarecrow_py.video.capture import check_webcam_input, get_random_frame_from_video  # Replace 'your_module_name' with the actual name of your Python file without the .py extension
from scarecrow_py.video.save_pic import save_frame_as_image  # Replace 'your_module_name' with the actual name of your Python file without the .py extension
from scarecrow_py.video.gc_image import detect_text  # Replace 'your_module_name' with the actual name of your Python file without the .py extension

def test_webcam(camera_index=0):
    """
    Test webcam input by checking if the webcam at the given index can capture a frame.
    
    Args:
    - camera_index (int): Index of the webcam to test.
    """
    print(f"Testing webcam at index {camera_index}...")
    flag, frame = get_random_frame_from_video("scarecrow_py/video/test_heat.mkv")
    if flag:
        print("Webcam is active and capturing input.")
        save_frame_as_image(frame, "test_image.png")
        extremes = detect_text("test_image.png")
        print("Image saved.")
    else:
        print("Failed to capture input from the webcam.")

if __name__ == "__main__":
    # Test the default webcam (usually the built-in webcam)
    test_webcam()

    # If you have an external webcam connected, you can test it by uncommenting the following line and adjusting the index if necessary
    # test_webcam(1)
