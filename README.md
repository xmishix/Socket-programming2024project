Overview

This repository contains the implementation of a socket programming project developed as part of a Network Architecture course. The project is divided into two distinct parts:


Part 1: Chat Application
The chat application is comprised of two primary components: the Server and the Client.

Server Side:
- Establishes a socket and binds it to a designated port.
- Listens for incoming client connections.
- Accepts connections from clients and establishes communication.
- Receives messages sent by the client.
- Sends appropriate responses back to the client.
- Terminates the connection after the communication has concluded.
Client Side:
- Creates a socket and establishes a connection to the server.
- Sends a message to the server.
- Receives the server’s response.
- Closes the connection once the interaction is complete.


Part 2: Server-Client Calculator
The server-client calculator follows a similar structure to the chat application but incorporates computation functionality. It consists of two primary components: the Server and the Client.

Server Side:
- Initializes a server socket and binds it to a specific IP address and port.
- Listens for incoming client connections.
- Accepts client connections and spawns a separate thread or process for each connection to handle multiple clients concurrently.
- Processes calculation requests received from clients.
- Executes the requested calculations using appropriate mathematical operations.
- Sends the results back to the respective client.

Client Side:
- Establishes a socket connection to the server using its IP address and port.
- Sends calculation requests to the server.
- Receives the results of the computations from the server.
- Displays the results to the user.

