



""" import tkinter as tk
 
from qr import QRcode

from tkinter import Tk, Button


class Window:
    def __init__(self) -> None:
        self.scan_QR = QRcode.scan_qr_code
        self.QRcode = QRcode
        self.capture = QRcode.capture_qr_code
    
        pass
    def showWindow():

        # Create a GUI window
        root = tk.Tk()
        root.title("QR Code Scanner")

        # Create a button to trigger QR code scanning
        scan_button = tk.Button(root, text="Scan QR Code", command=QRcode.capture_qr_code)
        # Create a button to trigger file dialog for selecting an image
        scan_button2 = QRcode.Button(root, text="Select Image File", command=QRcode.get_file_path)
        scan_button2.pack(pady=10)
        scan_button.pack(pady=10)

        # Create a GUI window
        root = Tk()
        root.title("QR Code Scanner")

        # Run the GUI main loop
        root.mainloop()# Create a GUI window
        root = tk.Tk()
        root.title("QR Code Scanner")

        # Create a button to trigger QR code scanning
        scan_button = tk.Button(root, text="Scan QR Code", command=QRcode.capture_qr_code)
        # Create a button to trigger file dialog for selecting an image
        scan_button2 = Button(root, text="Select Image File", command=QRcode.get_file_path)
        scan_button2.pack(pady=10)
        scan_button.pack(pady=10)

        # Create a GUI window
        root = Tk()
        root.title("QR Code Scanner")

        # Run the GUI main loop
        root.mainloop() """