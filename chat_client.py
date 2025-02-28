# Import socket
import socket

# Port number
port = 6009

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.200.0.0', port))  # connect client to server

# Initial message to start communication
client.send("Hello from client your name".encode('utf-8'))
print(client.recv(1024).decode('uft-8'))

def send_file(client_socket, file_path):
    with open(file_path, 'rb') as file:
        print("Sending file...")
        client_socket.sendfile(file)
        print("File sent.")
    
    # Receive and display the updated file
    received_data = b""
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        received_data += chunk
    
    print("Updated file received:")
    print(received_data.decode('utf-8'))


while True:
	message = input("Enter a message (type 'Bye from client computer' to quit):")
	client.send(message.encode('utf-8'))
	
	if "Bye from client" in message:
		break

	response = client.recv(1024).decode('utf-8')
	print(f"Server response: {response}")

client.close()

