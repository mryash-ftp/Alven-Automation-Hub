import os
import sys
import threading
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def install_pyinstaller():
    """Ensure PyInstaller is installed in the current environment."""
    try:
        import PyInstaller
    except ImportError:
        status_label.config(text="Status: Installing PyInstaller...", fg="orange")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def browse_file():
    """Open file dialog to select the Python script."""
    path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if path:
        file_label.config(text=path, fg="#00FFC8")
        status_label.config(text="Status: Script Selected", fg="#00FFC8")

def browse_icon():
    """Open file dialog to select an optional .ico icon."""
    path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
    if path:
        icon_label.config(text=path, fg="#FF007F")
    else:
        icon_label.config(text="Using Default System Icon", fg="grey")

def start_conversion():
    """Initialize the conversion process in a separate thread."""
    file_path = file_label.cget("text")
    icon_path = icon_label.cget("text")
    
    if not file_path or file_path == "No file selected":
        messagebox.showwarning("Warning", "Please select a Python (.py) file first!")
        return

    def run_cmd():
        convert_btn.config(state="disabled", text="CONVERTING...")
        progress.start(10)
        status_label.config(text="Status: Creating Workspace...", fg="yellow")
        
        try:
            install_pyinstaller()
            
            # --- PATH MANAGEMENT ---
            desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
            file_base_name = os.path.splitext(os.path.basename(file_path))[0]
            
            # Create a dedicated project folder on the Desktop
            project_dir = os.path.join(desktop_path, f"{file_base_name}_Build")
            if not os.path.exists(project_dir):
                os.makedirs(project_dir)

            # Define subdirectories for a clean build
            dist_path = os.path.join(project_dir, "Release_EXE")
            build_path = os.path.join(project_dir, "Build_Logs")

            # Build PyInstaller Command
            cmd = [
                sys.executable, "-m", "PyInstaller", 
                "--onefile", 
                "--noconsole", 
                "--clean",
                f"--distpath={dist_path}",
                f"--workpath={build_path}",
                f"--specpath={project_dir}"
            ]
            
            # Append icon if provided
            if icon_path and os.path.exists(icon_path) and icon_path != "Using Default System Icon":
                cmd.extend(["--icon", icon_path])
            
            cmd.append(file_path)
            
            # Execute the conversion
            subprocess.run(cmd, check=True)
            
            messagebox.showinfo("Success", f"Build Complete!\n\nLocation: {file_base_name}_Build\nCheck the 'Release_EXE' folder.")
            status_label.config(text="Status: Conversion Successful! ✅", fg="#2ecc71")
            
            # Automatically open the output folder
            os.startfile(dist_path)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during conversion:\n{e}")
            status_label.config(text="Status: Build Failed! ❌", fg="red")
        finally:
            progress.stop()
            convert_btn.config(state="normal", text="GENERATE PROJECT FOLDER")

    threading.Thread(target=run_cmd, daemon=True).start()

# --- UI SETUP (ALVEN DARK THEME) ---
root = tk.Tk()
root.title("Alven Project Packer v2.2")
root.geometry("500x520")
root.configure(bg="#121212")

# Progress Bar Styling
style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", thickness=8, background="#00FFC8", troughcolor="#333")

# UI Components
tk.Label(root, text="ALVEN PROJECT PACKER", font=("Orbitron", 18, "bold"), fg="#00FFC8", bg="#121212").pack(pady=20)

# Input Section
tk.Button(root, text="SELECT PYTHON SCRIPT", command=browse_file, bg="#1e1e1e", fg="#00FFC8", font=("Poppins", 9, "bold"), bd=1, width=25).pack()
file_label = tk.Label(root, text="No file selected", fg="grey", bg="#121212", wraplength=400, font=("Poppins", 8))
file_label.pack(pady=10)

# Asset Section
tk.Button(root, text="SELECT CUSTOM ICON", command=browse_icon, bg="#1e1e1e", fg="#FF007F", font=("Poppins", 9, "bold"), bd=1, width=25).pack()
icon_label = tk.Label(root, text="Using Default System Icon", fg="grey", bg="#121212", wraplength=400, font=("Poppins", 8))
icon_label.pack(pady=10)

# Progress Indicator
progress = ttk.Progressbar(root, orient="horizontal", length=350, mode="indeterminate", style="TProgressbar")
progress.pack(pady=20)

# Execution Button
convert_btn = tk.Button(root, text="GENERATE PROJECT FOLDER", command=start_conversion, bg="#FF007F", fg="white", font=("Orbitron", 11, "bold"), width=30, bd=0, cursor="hand2", activebackground="#ff3399")
convert_btn.pack(pady=10)

# Footer Status
status_label = tk.Label(root, text="System Ready", fg="#00FFC8", bg="#121212", font=("Poppins", 9))
status_label.pack(side="bottom", pady=20)

root.mainloop()
