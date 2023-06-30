import argparse
from pythonosc import udp_client

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9000)
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.host, args.port)
    client.send_message("/chatbox/input",["Hello World!",True,True])

