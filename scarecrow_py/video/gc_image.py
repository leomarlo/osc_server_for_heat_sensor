from google.cloud import vision
from google.oauth2 import service_account
import io
# import dotenv
import os
from video.extract_numbers import process_numbers_and_find_extremes
from dotenv import load_dotenv
load_dotenv()
credentials_path = os.getenv('GOOGLE_CREDENTIAL_FILE')


def detect_text_from_image_path(path):
    """
    Detects text in the image file using explicit credentials.
    
    Args:
    - path (str): Path to the image file.
    - credentials_path (str): Path to the Google Cloud service account key file (JSON).
    """
    # Load credentials from the service account key file
    print('credentials', credentials_path)
    # join with scarecrow_py and video folder
    adjusted_path = os.path.join(os.path.dirname(__file__), '..', '..',credentials_path)
    print(adjusted_path)
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    
    # Create a client using the loaded credentials
    client = vision.ImageAnnotatorClient(credentials=credentials)

    print('path', path)
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations   

    extremes = process_numbers_and_find_extremes([text.description for text in texts])

    if response.error.message:
        raise Exception('{}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors'.format(response.error.message))

    return extremes

def detect_text_from_frame(frame):
    """
    Detects text in the given frame.
    
    Args:
    - frame: The frame to process.
    
    Returns:
    - dict: A dictionary containing the smallest, largest, and center values found in the frame.
    """
     # Load credentials from the service account key file
    print('credentials', credentials_path)
    # join with scarecrow_py and video folder
    adjusted_path = os.path.join(os.path.dirname(__file__), '..', '..',credentials_path)
    print(adjusted_path)
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    
    # Create a client using the loaded credentials
    client = vision.ImageAnnotatorClient(credentials=credentials)

    image = vision.Image(content=frame)
    response = client.text_detection(image=image)
    texts = response.text_annotations   

    extremes = process_numbers_and_find_extremes([text.description for text in texts])

    if response.error.message:
        raise Exception('{}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors'.format(response.error.message))

    return extremes
