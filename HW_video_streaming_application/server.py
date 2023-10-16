import tkinter as tk
import cv2
from PIL import Image, ImageTk
import socket
import pickle
import struct

server_ip = '127.0.0.1'
server_port = 3400

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)

BUFFER = 1024


def update():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        label.config(image=photo)
        label.image = photo

        '''frame_bytes = pickle.dumps(frame)
        msg = struct.pack("Q", len(frame_bytes)) + frame_bytes
        client_socket.sendall(msg)

        cv2.imshow('', frame)'''

    window.after(10, update)


def send_message():
    message = entry.get()
    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, "나: " + message + "\n")
    chat_text.config(state=tk.DISABLED)
    entry.delete(0, tk.END)


'''def receive_message(): # 클라이언트가 전송한 메시지를 채팅창에 배포(오작동으로 주석 처리)
    data = client_socket.recv(BUFFER)
    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, "Client: " + data.decode() + "\n")
    chat_text.config(state=tk.DISABLED)
    entry.delete(0, tk.END)'''


while True:
    client_socket, addr = server_socket.accept()
    print("Client connected to server", addr)
    if client_socket:
        window = tk.Tk()
        window.title("화상 채팅")

        cap = cv2.VideoCapture(0)

        label = tk.Label(window)
        label.grid(row=0, column=0, padx=10, pady=10, rowspan=2, sticky="nsew")

        chat_text = tk.Text(window, wrap=tk.WORD, state=tk.DISABLED)
        chat_text.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        entry = tk.Entry(window)
        entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        send_button = tk.Button(window, text="보내기", command=send_message)
        send_button.grid(row=1, column=1, padx=10, pady=10, sticky="se")

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=4)
        window.grid_columnconfigure(1, weight=1)

        '''data = client_socket.recv(BUFFER)
        chat_text.insert(tk.END, "Client: " + data.decode() + "\n")
        print(data.decode())'''

        while cap.isOpened():
            update()

            window.mainloop()

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                client_socket.close()
                server_socket.close()

                cap.release()
