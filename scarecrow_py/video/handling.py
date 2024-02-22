def crop_frame(frame, crop):
    """
    Crops a frame based on specified margins.
    
    Args:
    - frame: The input frame.
    - crop (dict): A dictionary with keys 'left', 'right', 'top', 'bottom' indicating the crop margins.
    
    Returns:
    - The cropped frame.
    """
    h, w = frame.shape[:2]  # Get frame dimensions
    cropped_frame = frame[crop['top']:h-crop['bottom'], crop['left']:w-crop['right']]
    return cropped_frame


def scale_down_frame(frame, scale_factor):
    """
    Scales down a frame by a given factor.
    
    Args:
    - frame: The input frame.
    - scale_factor (float): The factor by which the frame should be scaled down.
    
    Returns:
    - The scaled-down frame.
    """
    width = int(frame.shape[1] * scale_factor)
    height = int(frame.shape[0] * scale_factor)
    dim = (width, height)
    scaled_down_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    return scaled_down_frame

