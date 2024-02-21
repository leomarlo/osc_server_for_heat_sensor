from pythonosc import dispatcher
from pythonosc import osc_server

OSC_IP = "127.0.0.1"
OSC_PORT = 4560

def handle_message(address, *args):
    print(f"Received OSC message on {address}: {args}")

if __name__ == "__main__":
    disp = dispatcher.Dispatcher()
    disp.map("/scarecrow", handle_message)

    server = osc_server.ThreadingOSCUDPServer((OSC_IP, OSC_PORT), disp)
    print(f"Serving on {OSC_IP}:{OSC_PORT}")
    server.serve_forever()
