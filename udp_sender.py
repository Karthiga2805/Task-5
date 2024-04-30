import socket

# Define the IP address and port number of the receiver
RECEIVER_IP = '127.0.0.1'  # Loopback address for localhost
RECEIVER_PORT = 12345

# Create a UDP socket
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Get user input for message to send
    message = input("Sender - Enter message to send: ")

    # Send the message to the receiver
    sender_socket.sendto(message.encode(), (RECEIVER_IP, RECEIVER_PORT))

    # Receive response from receiver
    response, _ = sender_socket.recvfrom(1024)
    print("Sender - Received response:", response.decode())
