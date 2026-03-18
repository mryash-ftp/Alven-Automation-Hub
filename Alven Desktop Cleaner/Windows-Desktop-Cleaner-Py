import os
import shutil
from datetime import datetime, timedelta

# --- CONFIGURATION ---
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop') 
main_storage_name = "Store Folder"
storage_path = os.path.join(desktop_path, main_storage_name)

# PROTECTION SYMBOLS: Items containing these symbols will be ignored (e.g., Project+Info)
ignore_symbols = ['+', '-', '#', '!', '@'] 

# SYSTEM IGNORE LIST: Folders that should never be moved
folders_to_ignore = [main_storage_name, "Recycle Bin"]

def organize_with_subsystems():
    """Organizes desktop items into categorized subfolders based on type and date."""
    
    # Create main storage directory if it doesn't exist
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)

    items = os.listdir(desktop_path)
    now = datetime.now()
    one_day_ago = now - timedelta(days=1)

    for item in items:
        item_path = os.path.join(desktop_path, item)
        
        # 1. SYMBOL PROTECTION: Skip items with special markers
        if any(sym in item for sym in ignore_symbols):
            continue

        # 2. SYSTEM FILTER: Skip core storage and system folders
        if item in folders_to_ignore:
            continue

        # 3. AGE CHECK: Get modification time
        mtime = datetime.fromtimestamp(os.path.getmtime(item_path))

        # Only process items older than 24 hours
        if mtime < one_day_ago:
            date_str = mtime.strftime('%d-%m-%Y')
            
            # --- SUBSYSTEM CATEGORIZATION ---
            if os.path.isdir(item_path):
                # Category 1: Directories
                category_path = os.path.join(storage_path, "1] Folders")
                target_subfolder = os.path.join(category_path, f"Folders {date_str}")
            else:
                # Category 2: Documents & Files
                category_path = os.path.join(storage_path, "2] Documents")
                target_subfolder = os.path.join(category_path, f"Docs {date_str}")

            # Create target directory structure
            if not os.path.exists(target_subfolder):
                os.makedirs(target_subfolder)

            # 4. EXECUTE MOVE
            try:
                print(f"Archiving to {os.path.basename(category_path)}: {item}")
                shutil.move(item_path, os.path.join(target_subfolder, item))
            except Exception as e:
                print(f"Error processing {item}: {e}")

if __name__ == "__main__":
    print("--- Alven Desktop Cleaner: Analysis Started ---")
    organize_with_subsystems()
    print("\nCleanup Complete! Desktop is now organized.")
