
# ⚡ Alven Desktop Cleaner (Python Automation)

A professional-grade desktop automation tool that prevents clutter by archiving old files and folders into a structured date-wise subsystem.

---

## ✨ Advanced Features

- **Dual-Subsystem Logic** Automatically separates **Directories** and **Files** into organized "Folders" and "Documents" branches.
  
- **Symbol Protection (Quick Lock)** Ignore any file/folder instantly by adding a special symbol (e.g., `+`, `#`, `@`) to its name.
  
- **Modification-Time Awareness** Uses `os.path.getmtime` to ensure only truly inactive items (older than 24h) are moved.

- **Zero Clutter Architecture** Organizes everything into a central `Store Folder` without creating a mess on the root desktop.

---

## 🧠 Smart Organization Logic

The tool categorizes items as follows:

1. **Check Symbols:** If name contains `+ - # ! @`, it stays on Desktop.
2. **Identify Type:** - Directories → `Store Folder/1] Folders/Folders [Date]`
   - Files → `Store Folder/2] Documents/Docs [Date]`
3. **Move:** Safely transfers items using `shutil` with error handling.

---

## 📁 Example Structure

### Desktop (Before)
- `Project_Alpha` (Old)
- `Invoice.pdf` (Old)
- `Important+Notes` (Protected with +)
- `Active_Work` (Modified today)

### Desktop (After Cleanup)
- `Important+Notes` ✅ (Stays)
- `Active_Work` ✅ (Stays)
- `Store Folder/`
  - `1] Folders/Folders 15-03-2026/Project_Alpha`
  - `2] Documents/Docs 15-03-2026/Invoice.pdf`

---

## 🚀 Setup & Execution

### Prerequisites
- Windows OS
- Python 3.8+

### Quick Start
```bash
# Clone the repository
git clone [https://github.com/pradeep-kumar-gupta/Windows-Desktop-Cleaner-Py.git](https://github.com/pradeep-kumar-gupta/Windows-Desktop-Cleaner-Py.git)

# Navigate to directory
cd Windows-Desktop-Cleaner-Py

# Run the automation
python organizer.py
