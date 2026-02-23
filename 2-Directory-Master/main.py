import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import webbrowser  # Browser kholne ke liye

# --- SETTINGS & THEME ---
BG_COLOR = "#0D0D0D"        # Deep Black
ACCENT_COLOR = "#00FFC8"    # Neon Cyan
F_COLOR = "Red" 
LINK_COLOR = "#00A8FF"      # Stylish Blue for link
TEXT_COLOR = "#FFFFFF"      # Pure White
INPUT_BG = "#1A1A1A"       # Dark Grey
BTN_COLOR = "#FF007F"       # Neon Pink
FONT_HEADER = ("Orbitron", 16, "bold")
FONT_LABEL = ("Poppins", 10, "bold")
FONT_INPUT = ("Poppins", 10)
FONT_LINK = ("Poppins", 9, "underline")

class FileAutomatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PyGen Flux v1.0")
        self.root.geometry("480x600") # Height thodi badha di link ke liye
        self.root.configure(bg=BG_COLOR)
        
        # Main Container
        self.main_frame = tk.Frame(root, bg=BG_COLOR, padx=30, pady=20)
        self.main_frame.pack(fill="both", expand=True)

        self.create_widgets()

    def open_link(self, event):
        webbrowser.open_new("https://mryash-ftp.github.io/Alven-Library/")

    def create_widgets(self):
        # Header
        tk.Label(self.main_frame, text="⚡ PyGen Flux", font=FONT_HEADER, 
                 fg=ACCENT_COLOR, bg=BG_COLOR).pack(pady=(0, 5))
        
        # Founder Name
        tk.Label(self.main_frame, text="Founder : Alven Alex (Pradeep)", font=FONT_LABEL, 
                 fg=F_COLOR, bg=BG_COLOR).pack(pady=(0, 2))
        
        # --- YOUR LINK (Clickable) ---
        link_label = tk.Label(self.main_frame, text="Visit Alven Library", font=FONT_LINK, 
                              fg=LINK_COLOR, bg=BG_COLOR, cursor="hand2")
        link_label.pack(pady=(0, 15))
        link_label.bind("<Button-1>", self.open_link) # Click event

        # 1. Directory Selection
        self.create_label("1. CHOOSE LOCATION")
        self.path_entry = self.create_entry()
        
        btn_browse = tk.Button(self.main_frame, text="SELECT FOLDER", command=self.select_dir, 
                               bg="#333", fg=ACCENT_COLOR, font=("Poppins", 8, "bold"), 
                               bd=0, padx=10, cursor="hand2")
        btn_browse.pack(pady=(5, 10), anchor="e")

        # 2. Base Name
        self.create_label("2. BASE NAME (e.g. Pylearn)")
        self.name_entry = self.create_entry()
        self.name_entry.insert(0, "Pylearn")

        # 3. Quantity
        self.create_label("3. QUANTITY (How many?)")
        self.count_entry = self.create_entry()
        self.count_entry.insert(0, "5")

        # 4. Type Selection
        self.create_label("4. WHAT TO CREATE?")
        self.type_var = tk.StringVar(value="Python (.py)")
        
        options_frame = tk.Frame(self.main_frame, bg=BG_COLOR)
        options_frame.pack(fill="x", pady=5)

        types = ["Python (.py)", "Text (.txt)", "Folder"]
        for t in types:
            rb = tk.Radiobutton(options_frame, text=t, variable=self.type_var, value=t, 
                                bg=BG_COLOR, fg=TEXT_COLOR, activebackground=BG_COLOR, 
                                activeforeground=ACCENT_COLOR, selectcolor=BG_COLOR, 
                                font=("Poppins", 9), cursor="hand2")
            rb.pack(side="left", padx=(0, 15))

        # 5. Date Toggle
        self.date_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.main_frame, text="INCLUDE DATE (DD-MM)", variable=self.date_var, 
                       bg=BG_COLOR, fg=TEXT_COLOR, activebackground=BG_COLOR, 
                       activeforeground=ACCENT_COLOR, selectcolor=BG_COLOR, 
                       font=("Poppins", 9), cursor="hand2").pack(pady=15, anchor="w")

        # 6. Action Button
        self.btn_gen = tk.Button(self.main_frame, text="GENERATE NOW", bg=BTN_COLOR, fg=TEXT_COLOR, 
                                 font=FONT_HEADER, bd=0, cursor="hand2", 
                                 activebackground="#E60073", command=self.generate)
        self.btn_gen.pack(fill="x", pady=10, ipady=12)

    def create_label(self, text):
        lbl = tk.Label(self.main_frame, text=text, font=FONT_LABEL, fg=ACCENT_COLOR, bg=BG_COLOR)
        lbl.pack(anchor="w", pady=(8, 2))

    def create_entry(self):
        ent = tk.Entry(self.main_frame, font=FONT_INPUT, bg=INPUT_BG, fg=TEXT_COLOR, 
                       insertbackground=ACCENT_COLOR, borderwidth=0, highlightthickness=1)
        ent.pack(fill="x", ipady=6, pady=2)
        ent.config(highlightbackground="#333", highlightcolor=ACCENT_COLOR)
        return ent

    def select_dir(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)

    def generate(self):
        path = self.path_entry.get()
        name = self.name_entry.get()
        
        try:
            count = int(self.count_entry.get())
        except:
            messagebox.showerror("Error", "Bhai, Quantity mein number daalo!")
            return

        if not path:
            messagebox.showerror("Error", "Location select karna bhool gaye!")
            return

        date_str = datetime.now().strftime("%d-%m")
        item_type = self.type_var.get()

        try:
            for i in range(1, count + 1):
                final_name = f"{i}- {name}"
                if self.date_var.get():
                    final_name += f" -{date_str}"
                
                full_path = os.path.join(path, final_name)

                if item_type == "Folder":
                    os.makedirs(full_path, exist_ok=True)
                else:
                    ext = ".py" if "Python" in item_type else ".txt"
                    with open(f"{full_path}{ext}", "w") as f:
                        f.write(f"# Created By Alven Alex\n# Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
            
            messagebox.showinfo("Success", f"Mubarak ho! {count} items ban gaye.")
        except Exception as e:
            messagebox.showerror("Error", f"Kuch gadbad hui: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileAutomatorGUI(root)
    root.mainloop()
