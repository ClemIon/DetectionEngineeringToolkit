from PIL import Image
from pyzbar.pyzbar import decode
import cv2
from gui import Window
from tkinter import Tk
"""
qr.py focusing on QRcode class that will include all of the functionality in regards to codes. I just need to 
fix my spaghetti code and learn better OOP practices.
- Mason AKA jlion
"""

class QRcode():
    def __init__(self, img_path):
        self.img_path = img_path
    # Function to decode QR code from an image file
    def scan_qr_code(file_path):
        try:
            with Image.open(file_path) as img:
                qr_codes = decode(img)
                if qr_codes:
                    data = qr_codes[0].data.decode('utf-8')
                    Tk.messagebox.showinfo("QR Code Detected", f"Data: {data}")
                else:
                    Window.tk.messagebox.showinfo("No QR Code Found", "No QR code found in the image.")
        except Exception as e:
            Window.tk.messagebox.showerror("Error", f"An error occurred: {e}")

    # Function to open a file dialog and get the file path
    def get_file_path():
        Window.Tk().withdraw() # Hide the root window
    file_path = Window.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        scan_qr_code(file_path)

    # Function to capture QR code and decode it
    def capture_qr_code():
        cap = cv2.VideoCapture(0)
        while True:
            _, frame = cap.read()
            qr_codes = decode(frame)
            for qr_code in qr_codes:
                data = qr_code.data.decode('utf-8')
                gui.messagebox.showinfo("QR Code Detected", f"Data: {data}")
                cap.release()
                cv2.destroyAllWindows()
                return
            cv2.imshow('QR Code Scanner', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    
