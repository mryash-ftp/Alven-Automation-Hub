# ⚡ Alven Project Packer v2.2
A professional, high-performance GUI utility to package Python scripts into standalone Windows Executables with a clean workspace logic.

## ✨ Key Features
* **Clean Workspace:** Unlike standard converters, it isolates `build` and `dist` files into a single project folder on your Desktop.
* **One-Click Conversion:** Bundles everything into a single `--onefile` executable.
* **Threading Enabled:** Real-time status updates without UI freezing.
* **Custom Branding:** Support for `.ico` assets to give your apps a professional look.
* **Auto-Environment Setup:** Automatically detects and installs missing dependencies.

## 🛠️ Requirements
* **Python:** 3.8 or higher
* **OS:** Windows (Internal logic uses `USERPROFILE` paths)

## 🚀 Professional Workflow
1.  **Select Script:** Choose the `.py` file you want to convert.
2.  **Add Icon (Optional):** Pick a `.ico` file for custom branding.
3.  **Generate:** Click `GENERATE PROJECT FOLDER`. 
4.  **Result:** The script will automatically open the `Release_EXE` folder once finished.

## 📂 Output Architecture
The tool prevents Desktop clutter by organizing files as follows:
`[YourFileName]_Build/` -> `Release_EXE/` (Final Output)

---
*Developed by Alven Alex (Pradeep Kumar Gupta)*
