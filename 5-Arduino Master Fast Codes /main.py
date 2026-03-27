import customtkinter as ctk
import pyperclip

class ArduinoAutoCoder(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Alven X - Arduino Master Automation V1")
        self.geometry("600x650")
        self.minsize(450, 600) # Minimum size set ki hai
        ctk.set_appearance_mode("dark")
        
        # Grid Configuration (for Responsiveness)
        self.grid_columnconfigure(1, weight=1) # Output area expands
        self.grid_rowconfigure(0, weight=1)

        # --- LEFT PANEL (Inputs & Buttons) ---
        self.left_panel = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.left_panel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.header = ctk.CTkLabel(self.left_panel, text="Alven X Pro", font=("Segoe UI", 24, "bold"), text_color="#00ffff")
        self.header.pack(pady=20)

        # Range Inputs
        ctk.CTkLabel(self.left_panel, text="Pin Range (Start - End):", font=("Arial", 12, "bold")).pack(pady=(10,0))
        self.range_f = ctk.CTkFrame(self.left_panel, fg_color="transparent")
        self.range_f.pack(pady=5)
        self.entry_start = ctk.CTkEntry(self.range_f, width=70); self.entry_start.insert(0, "0"); self.entry_start.pack(side="left", padx=5)
        self.entry_end = ctk.CTkEntry(self.range_f, width=70); self.entry_end.insert(0, "10"); self.entry_end.pack(side="left", padx=5)

        # Pattern & Delay
        ctk.CTkLabel(self.left_panel, text="Pattern (e.g. 1-10):", font=("Arial", 12, "bold")).pack(pady=(15,0))
        self.entry_pattern = ctk.CTkEntry(self.left_panel, width=200); self.entry_pattern.insert(0, "1-10"); self.entry_pattern.pack(pady=5)

        ctk.CTkLabel(self.left_panel, text="Delay (ms):", font=("Arial", 12, "bold")).pack(pady=(15,0))
        self.entry_delay = ctk.CTkEntry(self.left_panel, width=200); self.entry_delay.insert(0, "200"); self.entry_delay.pack(pady=5)

        # Buttons
        self.btn_gen = ctk.CTkButton(self.left_panel, text="Generate Pattern", command=lambda: self.generate_logic(reverse=False), fg_color="#6a0dad", height=35)
        self.btn_gen.pack(pady=15, padx=20, fill="x")

        self.btn_rev = ctk.CTkButton(self.left_panel, text="Generate Reverse Mode", command=lambda: self.generate_logic(reverse=True), fg_color="#ff8c00", text_color="black", height=35)
        self.btn_rev.pack(pady=5, padx=20, fill="x")

        self.btn_setup = ctk.CTkButton(self.left_panel, text="Generate void setup()", command=self.generate_setup, fg_color="#4B0082", height=35)
        self.btn_setup.pack(pady=5, padx=20, fill="x")

        self.btn_copy = ctk.CTkButton(self.left_panel, text="Copy to Clipboard", command=self.copy_to_clip, fg_color="#2e8b57", height=40)
        self.btn_copy.pack(pady=20, padx=20, fill="x")

        self.btn_clear = ctk.CTkButton(self.left_panel, text="Clear Screen", command=lambda: self.output_text.delete("0.0", "end"), fg_color="#8b0000")
        self.btn_clear.pack(pady=5, padx=20, fill="x")

        # --- NEW CREDIT SECTION (My Add) ---
        self.credit_frame = ctk.CTkFrame(self.left_panel, fg_color="#1a1a1a", corner_radius=10)
        self.credit_frame.pack(side="bottom", fill="x", padx=10, pady=20)
        
        credit_text = (
            "Founder: Alven Alex aka PRADEEP GUPTA\n"
            "Credit: Alven X AI\n"
            "Feature: Fast Automation Key Value"
        )
        self.lbl_credits = ctk.CTkLabel(self.credit_frame, text=credit_text, font=("Arial", 11), text_color="#aaaaaa", justify="left")
        self.lbl_credits.pack(pady=10, padx=10)

        # --- RIGHT PANEL (Output Text) ---
        self.output_text = ctk.CTkTextbox(self, font=("Consolas", 14), corner_radius=0)
        self.output_text.grid(row=0, column=1, sticky="nsew", padx=(0,10), pady=10)

    def get_pins_info(self):
        try:
            return int(self.entry_start.get()), int(self.entry_end.get()), self.entry_pattern.get().strip(), self.entry_delay.get()
        except: return None

    def generate_setup(self):
        info = self.get_pins_info()
        if info:
            st, en, _, _ = info
            code = "// Auto Generated Setup by Alven X\nvoid setup() {\n"
            for i in range(st, en + 1):
                code += f"  pinMode({i}, OUTPUT);\n"
            code += "}\n"
            self.update_output(code)

    def generate_logic(self, reverse=False):
        info = self.get_pins_info()
        if not info:
            self.update_output("Error: Check numeric values!"); return

        st, en, pattern_raw, delay = info
        all_pins = list(range(st, en + 1))
        final_code = ""

        try:
            if "-" in pattern_raw:
                p_st, p_en = map(int, pattern_raw.split("-"))
                p_range = list(range(p_st, p_en + 1))
                if reverse: p_range.reverse()

                for active in p_range:
                    final_code += f"// Step for Pin {active}\n"
                    for p in all_pins:
                        final_code += f"digitalWrite({p}, {'HIGH' if p == active else 'LOW'});\n"
                    final_code += f"delay({delay});\n\n"
            else:
                high_pins = [int(x.strip()) for x in pattern_raw.split(",") if x.strip()]
                for p in all_pins:
                    final_code += f"digitalWrite({p}, {'HIGH' if p in high_pins else 'LOW'});\n"
                final_code += f"delay({delay});\n"

            self.update_output(final_code)
        except Exception as e: self.update_output(f"Error: {e}")

    def update_output(self, text):
        self.output_text.delete("0.0", "end")
        self.output_text.insert("0.0", text)

    def copy_to_clip(self):
        pyperclip.copy(self.output_text.get("0.0", "end"))
        self.btn_copy.configure(text="COPIED!", fg_color="#1e5631")
        self.after(1500, lambda: self.btn_copy.configure(text="Copy to Clipboard", fg_color="#2e8b57"))

if __name__ == "__main__":
    app = ArduinoAutoCoder()
    app.mainloop()
