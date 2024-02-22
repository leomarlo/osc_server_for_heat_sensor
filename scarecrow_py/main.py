import random
import time
from threading import Thread
from pythonosc import udp_client, dispatcher, osc_server
from config import CONFIG, CAPTURE_MODES
import video.heat_sensor as scarecrow


def scarecrow_handler(address, *args):
    """
    Handler function for received OSC messages.
    """
    print(f"Received message on {address}: {args}")

def send_signal_periodically():
    """
    Sends a random integer to the /scarecrow address periodically.
    """
    client = udp_client.SimpleUDPClient(CONFIG.OSC_IP, CONFIG.OSC_PORT)
    while True:
        if CONFIG.MODE==CAPTURE_MODES["body_in_center"]:
            number = scarecrow.body_in_center()
        elif CONFIG.MODE==CAPTURE_MODES["heat_sensor"]:
            number = scarecrow.heat_sensor()
        else:
            number = random.randint(0, CONFIG.MAX_NUMBER)

        client.send_message("/scarecrow", number)
        print(f"Sent: {number}")
        time.sleep(CONFIG.TIME_INTERVAL)

if __name__ == "__main__":
    # Set up the dispatcher for the OSC server
    disp = dispatcher.Dispatcher()
    disp.map("/scarecrow", scarecrow_handler)

    # Set up and start the OSC server
    server = osc_server.ThreadingOSCUDPServer((CONFIG.OSC_IP, CONFIG.OSC_PORT), disp)
    server_thread = Thread(target=server.serve_forever)
    server_thread.start()
    print(f"Serving on {CONFIG.OSC_IP}:{CONFIG.OSC_PORT}")

    # Start sending integers periodically
    sender_thread = Thread(target=send_signal_periodically)
    sender_thread.start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Graceful shutdown on Ctrl+C
        server.shutdown()
        print("Server shut down.")
