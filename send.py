import socket
from pyboy import PyBoy, WindowEvent
pyboy = PyBoy('ROMs/yellow.gb',sound=False)
keyMap = {"up":[WindowEvent.PRESS_ARROW_UP,WindowEvent.RELEASE_ARROW_UP],
          "down":[WindowEvent.PRESS_ARROW_DOWN, WindowEvent.RELEASE_ARROW_DOWN],
          "left":[WindowEvent.PRESS_ARROW_LEFT, WindowEvent.RELEASE_ARROW_LEFT],
          "right":[WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT],
          "a":[WindowEvent.PRESS_BUTTON_A, WindowEvent.RELEASE_BUTTON_A],
          "b":[WindowEvent.PRESS_BUTTON_B, WindowEvent.RELEASE_BUTTON_B]
            }

def parseCmd(cmdStr, pyboy):
    #Single CMD:
    if len(cmdStr) == 1:
        if cmdStr == b'a':
            pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
            pyboy.tick()
            pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
            pyboy.tick()
        elif cmdStr == b'b':
            pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
            pyboy.tick()
            pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
            pyboy.tick()
        elif cmdStr == b'u':
            pyboy.send_input(WindowEvent.PRESS_ARROW_UP)
            pyboy.tick()
            pyboy.send_input(WindowEvent.RELEASE_ARROW_UP)
            pyboy.tick()
        elif cmdStr == b'd':
            pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
            pyboy.tick()
            pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)
            pyboy.tick()
        elif cmdStr == b'r':
            pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
            pyboy.tick()
            pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
            pyboy.tick()
        elif cmdStr == b'l':
            pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
            pyboy.tick()
            pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
            pyboy.tick()

def sendKey(key):
    try:
        press, release = keyMap[key][0], keyMap[key][1]
        pyboy.send_input(press)
        pyboy.tick()
        pyboy.tick()
        pyboy.tick()
        pyboy.send_input(release)
        pyboy.tick()
    except KeyError:
        print("Invalid Key on keymap")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 50007)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)


# Listen for incoming connections
sock.listen(1)

sock.setblocking(0)

while True:
    # Wait for a connection
    print('waiting for a connection')
    while not pyboy.tick():
        try:
            connection, client_address = sock.accept()

            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                if data == b'a':
                    sendKey("a")
                    print('received {!r}'.format(data))
                    data = None
                elif data == b'b':
                    sendKey("b")
                    print('received {!r}'.format(data))
                    data = None
                elif data == b'u' or data == b'up':
                    sendKey("up")
                    print('received {!r}'.format(data))
                    data = None
                elif data == b'd' or data == b'down':
                    sendKey("down")
                    print('received {!r}'.format(data))
                    data = None
                elif data == b'r' or data == b'right':
                    sendKey("right")
                    print('received {!r}'.format(data))
                    data = None
                elif data == b'l' or data == b'left':
                    sendKey("left")
                    print('received {!r}'.format(data))
                    data = None

                else:
                    break;
                data = None


            connection.close()
        except BlockingIOError:
            pass
