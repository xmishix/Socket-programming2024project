import socket
import tkinter as tk
from tkinter import messagebox

class CalculatorClient:
        def __init__(self, master):
                self.master = master
                self.master.title("Network Calculator Client")
                self.master.geometry("300x200")

                # Create UI components
                self.label = tk.Label(master, text="Enter calculation:")
                self.label.pack(pady=5)
                
                self.entry = tk.Entry(master, width=30)
                self.entry.pack(pady=5)
                
                self.result_label = tk.Label(master, text="Result:")
                self.result_label.pack(pady=5)

                self.send_button = tk.Button(master, text="Calculate", command=self.send_request)
                self.send_button.pack(pady=5)

                self.quit_button = tk.Button(master, text="Quit", command=master.quit)
                self.quit_button.pack(pady=5)

                # Connect to server
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect(('127.0.0.1', 12345))  # Replace with server IP and port

        def send_request(self):
                # Get calculation from entry
                calculation = self.entry.get()
                if calculation:
                        self.client_socket.send(calculation.encode('utf-8'))
                
                # Receive and display result
                result = self.client_socket.recv(1024).decode('utf-8')
                self.result_label.config(text=f"Result: {result}")

        def close_connection(self):
                self.client_socket.close()

# Run the client
root = tk.Tk()
client_app = CalculatorClient(root)
root.protocol("WM_DELETE_WINDOW", client_app.close_connection)
root.mainloop()

