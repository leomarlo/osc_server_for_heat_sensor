from video.capture import capture_video_frame
from video.gc_image import detect_text_from_frame
from config import CONFIG

def heat_sensor():
    """
    Simulates a heat sensor by returning a random integer between 0 and MAX_NUMBER.
    """
    frame = capture_video_frame()
    extremes = detect_text_from_frame(frame)
    smallest = extremes["smallest"] 
    largest = extremes["largest"]
    center = extremes["center"]
    # scale extremes["smallest"] and extremes["largest"] to a value between 0 and CONFIG.MAX_NUMBER and figure out what extremes["center"] is
    if center == largest:
        return CONFIG.MAX_NUMBER
    elif center == smallest:
        return 0
    else:
        return int(round((center - smallest) / (largest - smallest) * CONFIG.MAX_NUMBER, 0))
