import socket

# Define the IP address and port number to listen on
LISTEN_IP = '127.0.0.1'  # Loopback address for localhost
LISTEN_PORT = 12345

# Create a UDP socket
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the listening IP and port
receiver_socket.bind((LISTEN_IP, LISTEN_PORT))

while True:
    # Receive message from sender
    message, address = receiver_socket.recvfrom(1024)

    print(f"Receiver - Received message from {address}: {message.decode()}")
    response = input("Receiver - Enter response to send: ")

    # Send the response to the sender
    receiver_socket.sendto(response.encode(), address)
