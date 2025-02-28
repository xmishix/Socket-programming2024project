import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Client {client_address} connected.")
    while True:
        try:
            # Receive the calculation request from the client
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break

            print(f"Received calculation request: {request}")
            
            # Perform the calculation and prepare the response
            try:
                result = eval(request)  # Use eval with caution; for controlled math expressions only
                response = f"Result: {result}"
            except Exception as e:
                response = f"Error: {e}"

            # Send the result back to the client
            client_socket.send(response.encode('utf-8'))
        except:
            break

    client_socket.close()
    print(f"Client {client_address} disconnected.")

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))  # Replace with desired IP and port
server.listen(5)
print("Calculator server listening on port 12345...")

while True:
    client_socket, client_address = server.accept()
    client_thread = threading.Thread(target=handle_client, 
args=(client_socket, client_address))
    client_thread.start()

