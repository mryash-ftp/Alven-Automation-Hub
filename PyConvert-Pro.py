import os
import sys
import threading
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def install_pyinstaller():
    try:
        import PyInstaller
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def browse_file():
    path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if path:
        file_label.config(text=path, fg="white")
        status_label.config(text="File Selected. Ready to convert.", fg="#00FFC8")

def browse_icon():
    path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
    if path:
        icon_label.config(text=path, fg="white")
    else:
        icon_label.config(text="Default Logo Use Hoga", fg="grey")

def start_conversion():
    file_path = file_label.cget("text")
    icon_path = icon_label.cget("text")
    
    if not file_path or file_path == "Koi file select nahi ki":
        messagebox.showwarning("Warning", "Pehle ek Python (.py) file select karein!")
        return

    def run_cmd():
        convert_btn.config(state="disabled", text="Converting...")
        status_label.config(text="Processing... (Check CMD for details)", fg="yellow")
        
        try:
            install_pyinstaller()
            
            # Base Command
            cmd = f'pyinstaller --onefile --noconsole --clean'
            
            # Agar icon select kiya hai toh add karo, warna default
            if icon_path and icon_path != "Default Logo Use Hoga":
                cmd += f' --icon="{icon_path}"'
            
            cmd += f' "{file_path}"'
            
            subprocess.run(cmd, shell=True, check=True)
            
            messagebox.showinfo("Success", "EXE successfully ban gayi hai!\n'dist' folder check karein.")
            status_label.config(text="Conversion Complete! ✅", fg="#2ecc71")
        except Exception as e:
            messagebox.showerror("Error", f"Kuch gadbad ho gayi:\n{e}")
            status_label.config(text="Error occurred! ❌", fg="red")
        
        convert_btn.config(state="normal", text="Convert to EXE")

    threading.Thread(target=run_cmd).start()

# --- UI Setup (Modern Dark Theme) ---
root = tk.Tk()
root.title("Python to EXE Master v2.0")
root.geometry("500x450")
root.configure(bg="#121212")

# Header
tk.Label(root, text="EXE CONVERTER PRO", font=("Orbitron", 18, "bold"), fg="#00FFC8", bg="#121212").pack(pady=15)

# Python File Section
tk.Label(root, text="1. Select Python File:", font=("Poppins", 10, "bold"), fg="white", bg="#121212").pack(anchor="w", padx=50)
btn_browse = tk.Button(root, text="BROWSE .PY", command=browse_file, bg="#333", fg="#00FFC8", bd=0, padx=10, cursor="hand2")
btn_browse.pack(pady=5)
file_label = tk.Label(root, text="Koi file select nahi ki", fg="grey", bg="#121212", wraplength=400)
file_label.pack(pady=5)

# Icon Section (Naya Addition)
tk.Label(root, text="2. Select Logo (Optional .ico):", font=("Poppins", 10, "bold"), fg="white", bg="#121212").pack(anchor="w", padx=50, pady=(10,0))
btn_icon = tk.Button(root, text="SELECT ICON", command=browse_icon, bg="#333", fg="#FF007F", bd=0, padx=10, cursor="hand2")
btn_icon.pack(pady=5)
icon_label = tk.Label(root, text="Default Logo Use Hoga", fg="grey", bg="#121212", wraplength=400)
icon_label.pack(pady=5)

# Conversion Button
convert_btn = tk.Button(root, text="CONVERT TO EXE", command=start_conversion, bg="#FF007F", fg="white", font=("Orbitron", 12, "bold"), width=25, bd=0, cursor="hand2")
convert_btn.pack(pady=30)

# Status
status_label = tk.Label(root, text="Ready", fg="#00FFC8", bg="#121212", font=("Poppins", 9))
status_label.pack(side="bottom", pady=10)

root.mainloop()
