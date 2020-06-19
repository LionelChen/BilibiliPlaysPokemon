import socket
from pyboy import PyBoy, WindowEvent
pyboy = PyBoy('ROMs/yellow.gb',sound=True)



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
                    pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
                    pyboy.tick()
                    pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
                    pyboy.tick()
                    print('received {!r}'.format(data))
                    data = None
                elif data == b'b':
                    pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
                    pyboy.tick()
                    pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
                    pyboy.tick()
                    print('received {!r}'.format(data))
                    data = None
                elif data == b'u' or data == b'up':
                    pyboy.send_input(WindowEvent.PRESS_ARROW_UP)
                    pyboy.tick()
                    pyboy.send_input(WindowEvent.RELEASE_ARROW_UP)
                    pyboy.tick()
                    print('received {!r}'.format(data))
                    data = None
                elif data == b'd' or data == b'down':
                    pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
                    pyboy.tick()
                    pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)
                    pyboy.tick()
                    print('received {!r}'.format(data))
                    data = None
                elif data == b'r' or data == b'right':
                    pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
                    pyboy.tick()
                    pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
                    pyboy.tick()
                    print('received {!r}'.format(data))
                    data = None
                elif data == b'l' or data == b'left':
                    pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
                    pyboy.tick()
                    pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
                    pyboy.tick()
                    print('received {!r}'.format(data))
                    data = None
                else:
                    break;
                #if data:
                #    print('sending data back to the client')
                #    connection.sendall(data)
                #else:
                #    print('no data from', client_address)
                #    break

            connection.close()
        except BlockingIOError:
            pass

        #finally:
            #Clean up the connection
            #print("Closing current connection")
            #connection.close()