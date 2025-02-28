# Import modules
import socket
import threading
import os


def handle_file_transfer(client_socket):
    file_name = 'test_file.txt'
    
    # Receive the file data
    with open(file_name, 'wb') as file:
        print("...\nReceiving file...\n...")
        while True:
            file_data = client_socket.recv(1024)
            if not file_data:
                break
            file.write(file_data)
    
    print(f"File {file_name} received and saved.")
    
    # Read and print the file contents
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content: ")
        print(content)
    
    # Append a line and send it back
    with open(file_name, 'a') as file:
        file.write("\nThis is an added line from the server")
    
    with open(file_name, 'rb') as file:
        print("...\nSending modified file back to client...\n...")
        client_socket.sendfile(file)


# Function to handle each client connection
def handle_client(c_socket, c_address):
	print(f"Connection establish with {c_address}")
	while True:
		message = c_socket.recv(1024).decode('utf-8')
		if not message:
			break
		print(f"Received from client: {message}")

		if "Bye from client Gabriella" in message:
			respose = f"Bye from server Gabriella {c_address}"
			c_socket.send(response.encode('utf-8'))
			print(f"Sent: {response}")
			break

		# Send a response to the client
		response = f"Hello from Server {c_address}"
		c_socket.send(response.encode('utf-8'))
		print(f"Sent: {response}")

	c_socket.close()
	print(f"Connection closed with {c_address}")

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Port number
port = 6009
# Binds port number to socket
server.bind(('', port)) # Replace with desired host 
server.listen(1)# server listens to 1 incomming and make other wait
print(f"Server listening on port {port}...")

while True:
	c_socket, c_address = server.accept()
	c_thread = threading.Thread(target = handle_client, args = (c_socket, 
c_address))
	c_thread.start() 
