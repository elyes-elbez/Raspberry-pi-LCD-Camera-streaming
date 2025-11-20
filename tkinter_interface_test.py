import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import torch
from torchvision import models, transforms
import numpy as np
from picamera2 import Picamera2
import cv2
import random

# Define image transforms
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# Main GUI App
class InjuryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Skin Injury Diagnosis")
        self.root.configure(bg="#f0f4f7")
        self.root.geometry("700x550")

       
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_preview_configuration(main={"size": (640, 480)}))

        self.video_label = tk.Label(self.root, bg="#f0f4f7")
        self.video_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start Camera", command=self.start_camera,
                                      bg="#4CAF50", fg="white", font=("Helvetica", 14), width=20)
        self.start_button.pack()

        self.current_frame = None
        self.running = False

    def start_camera(self):
        self.start_button.pack_forget()
        self.capture_button.pack()
        self.picam2.start()
        self.running = True
        self.update_frame()

    def update_frame(self):
        if self.running:
            frame = self.picam2.capture_array()
            self.current_frame = frame
            image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = Image.fromarray(image)
            imgtk = ImageTk.PhotoImage(image=img.resize((640, 480)))
            self.video_label.imgtk = imgtk
            self.video_label.config(image=imgtk)
            self.root.after(30, self.update_frame)

    def on_close(self):
        self.running = False
        self.picam2.stop()
        self.root.destroy()

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = InjuryApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()





