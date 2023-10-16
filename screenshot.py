import time
import pyautogui
import tkinter as tk
from tkinter import ttk

def screenshot():
    name = int(round(time.time() * 1000))
    name = '/home/keshav/python-projects/ScreenShot-App/screenshots_data/{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
root.title("Screenshot App")
root.geometry("300x100")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

button = ttk.Button(frame, text="Take Screenshot", command=screenshot)
button.pack(side=tk.LEFT, padx=10, pady=10)

close = ttk.Button(frame, text="QUIT", command=root.destroy)
close.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
