import random
from time import sleep
from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer

TIME_INTERVAL = 1.0  # seconds
MAX_NUMBER = 126
OSC_ADDRESS = "/scarecrow"
OSC_IP = "127.0.0.1"
OSC_PORT = 4560

def scarecrow(address, *args):
    """
    Handler function that gets called when an OSC message is received on the /scarecrow route.
    It prints the received message.
    """
    print(f"Received message on {address}: {args[0]}")
    # Example of processing and returning a value, though in this context, 'return' does not send data back
    # Instead, consider sending a response via OSC if needed
    random_number = random.randint(0, 126)  # Generate a random number
    print(f"Processing data to generate random number: {random_number}")
    return random_number  # Note: This return value is not sent back via OSC. Additional logic is required to send a response.

if __name__ == "__main__":
    # IP and port configuration for the OSC server
    OSC_IP = "127.0.0.1"
    OSC_PORT = 4560

    dispatcher = Dispatcher()
    # Map incoming OSC messages on the /scarecrow route to the scarecrow function
    dispatcher.map("/scarecrow", scarecrow)

    # Create and start the OSC server
    server = ThreadingOSCUDPServer((OSC_IP, OSC_PORT), dispatcher)
    print(f"Serving on {OSC_IP}:{OSC_PORT}")
    server.serve_forever()
