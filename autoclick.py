import tkinter as tk
import pyautogui
import threading
import time
#

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Clicker")

        self.start_button = tk.Button(root, text="Start Auto Clicker", command=self.start_auto_clicker)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Auto Clicker", command=self.stop_auto_clicker)
        self.stop_button.pack(pady=10)
        self.stop_button["state"] = "disabled"

        self.interval_label = tk.Label(root, text="Interval (seconds):")
        self.interval_label.pack()
        self.interval_entry = tk.Entry(root)
        self.interval_entry.pack()

        self.area_label = tk.Label(root, text="Select Area:")
        self.area_label.pack()
        self.area_button = tk.Button(root, text="Select Area", command=self.select_area)
        self.area_button.pack()

        self.click_thread = None
        self.is_clicking = False

    def start_auto_clicker(self):
        try:
            interval = float(self.interval_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid interval.")
            return

        if interval <= 0:
            tk.messagebox.showerror("Error", "Interval must be greater than zero.")
            return

        self.is_clicking = True
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"

        def click():
            while self.is_clicking:
                pyautogui.click()
                time.sleep(interval)

        self.click_thread = threading.Thread(target=click)
        self.click_thread.start()

    def stop_auto_clicker(self):
        self.is_clicking = False
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"

    def select_area(self):
        tk.messagebox.showinfo("Select Area", "Click and drag to select the area.")
        area = pyautogui.confirm("Area Selected", "Area has been selected. Click OK to continue.")
        print("Selected Area:", area)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()
