import requests
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)

def download_gif():
    url = url_var.get().strip()
    folder = folder_var.get().strip()

    if not url:
        messagebox.showerror("Error", "Enter a GIF URL first")
        return
    if not folder:
        messagebox.showerror("Error", "Choose a download folder")
        return

    try:
        filename = os.path.basename(url.split("?")[0])
        if not filename.lower().endswith(".gif"):
            filename += ".gif"

        filepath = os.path.join(folder, filename)

        data = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).content
        with open(filepath, "wb") as f:
            f.write(data)

        messagebox.showinfo("Success", f"Downloaded:\n{filepath}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("GIF Downloader")
root.geometry("500x120")
root.resizable(False, False)

url_var = tk.StringVar()
folder_var = tk.StringVar()

tk.Label(root, text="GIF URL:").pack(anchor="w", padx=10)
tk.Entry(root, textvariable=url_var, width=60).pack(padx=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Entry(frame, textvariable=folder_var, width=45).pack(side="left", padx=5)
tk.Button(frame, text="Browse", command=browse_folder).pack(side="left")

tk.Button(root, text="Download GIF", command=download_gif).pack(pady=5)

root.mainloop()
