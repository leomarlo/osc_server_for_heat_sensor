from video.capture import capture_video_frame
from video.gc_image import detect_text_from_frame
from config import CONFIG, BODY_TEMP_ON_CAPTURE

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


def body_in_center():
    """
    Simulates a body detection system by returning True if the heat sensor returns a value greater than 0.8 * MAX_NUMBER.
    """
    frame = capture_video_frame()
    extremes = detect_text_from_frame(frame)
    center = extremes["center"]
    # if center is less than 26 return 0. If is is between 26 and 31 linearly scale it to 0.5. If it is between 31 and 34 linearly scale it to 0.8. If it between 34 and 37 scale to 1 and above 1 its just 1
    res = 0
    if center < BODY_TEMP_ON_CAPTURE.MIN:
        res = 0  
    elif center < (BODY_TEMP_ON_CAPTURE.MIN + 5):
        res = ((center - BODY_TEMP_ON_CAPTURE.MIN) / 5) * 0.5
    elif center < BODY_TEMP_ON_CAPTURE.MIN + 8:
        res = ((center - (BODY_TEMP_ON_CAPTURE.MIN + 5)) / 3) * 0.3 + 0.5
    elif center < (BODY_TEMP_ON_CAPTURE.MIN + 11):
        res = ((center - (BODY_TEMP_ON_CAPTURE.MIN + 8)) / 3) * 0.2 + 0.8
    else:
        res = 1
    
    # scale res between 0 and 1 to 0 and CONFIG.MAX_NUMBER
    return int(round(res * CONFIG.MAX_NUMBER, 0))