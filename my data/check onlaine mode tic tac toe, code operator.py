import socket
import tkinter as tk

def send_move(row, col):
    move = f"{row}{col}"
    client_socket.send(move.encode())

def on_click(row, col):
    global current_player

    if board[row][col] == "":
        if current_player == "X":
            buttons[row][col].config(text="X", state=tk.DISABLED)
            current_player = "O"
        else:
            buttons[row][col].config(text="O", state=tk.DISABLED)
            current_player = "X"

        send_move(row, col)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5555))
    server_socket.listen(1)
    print("Ждем подключения...")
    client_socket, address = server_socket.accept()
    print(f"Подключен клиент {address}")
    return client_socket

def receive_move():
    while True:
        move = client_socket.recv(1024).decode()
        row, col = int(move[0]), int(move[1])
        if board[row][col] == "":
            if current_player == "X":
                buttons[row][col].config(text="O", state=tk.DISABLED)
                current_player = "X"
            else:
                buttons[row][col].config(text="X", state=tk.DISABLED)
                current_player = "O"

def setup_gui():
    root = tk.Tk()
    root.title("Крестики-нолики")

    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, width=10, height=5, font=("Arial", 20),
                                       command=lambda row=i, col=j: on_click(row, col))
            buttons[i][j].grid(row=i, column=j)

    root.mainloop()

if __name__ == "__main__":
    client_socket = start_server()

    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    receive_move_thread = threading.Thread(target=receive_move)
    receive_move_thread.start()

    setup_gui()