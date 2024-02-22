CAPTURE_MODES = dict(
    body_in_center=1,
    heat_sensor=2
)

class BODY_TEMP_ON_CAPTURE:
    MIN = 18
    MAX = 37
    
class CONFIG: 
    # Configuration for both sending and receiving
    OSC_IP = "127.0.0.1"
    OSC_PORT = 4560
    TIME_INTERVAL = 8.0  # seconds for sending messages
    MAX_NUMBER = 126
    # Configuration for video handling
    ENVIRONMENT="development"
    CAMERA_ID = 0
    TEST_VIDEO_FILE = "test_heat.mkv"
    MODE=1