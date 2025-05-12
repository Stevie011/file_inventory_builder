# file_inventory.py - Windows-compatible version
import os
import sys
import traceback
from datetime import datetime

def get_application_path():
    # Get the correct path whether running as script or exe
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.realpath(sys.argv[0]))

def create_file_inventory():
    try:
        # Import here to ensure PyInstaller captures these dependencies
        import pandas as pd
        
        # Get the current directory (where the exe is running)
        current_dir = get_application_path()
        
        print(f"Working in directory: {current_dir}")
        
        # Get all files in the current directory
        files = []
        for f in os.listdir(current_dir):
            if os.path.isfile(os.path.join(current_dir, f)):
                files.append(f)
        
        print(f"Found {len(files)} files in directory")
        
        # Create a DataFrame with the filenames
        df = pd.DataFrame(files, columns=['Filename'])
        
        # Generate the output filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_filename = f"file_inventory_{timestamp}.xlsx"
        output_path = os.path.join(current_dir, output_filename)
        
        print(f"Creating Excel file at: {output_path}")
        
        # Create Excel file with extra error handling for Windows
        try:
            # First, try the standard method
            df.to_excel(output_path, index=False, engine='openpyxl')
        except Exception as excel_error:
            print(f"First Excel creation method failed: {str(excel_error)}")
            
            # Try an alternative method
            try:
                with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
            except Exception as alt_error:
                print(f"Alternative Excel creation method failed: {str(alt_error)}")
                # Last resort - try the xlsxwriter engine if openpyxl fails
                df.to_excel(output_path, index=False, engine='xlsxwriter')
        
        # Verify the file was created
        if os.path.exists(output_path):
            print(f"Success! File created: {output_filename}")
            print(f"File size: {os.path.getsize(output_path)} bytes")
        else:
            print(f"Warning: File creation may have failed. Cannot find: {output_filename}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print("Detailed error information:")
        traceback.print_exc()
        
        # Write error to log file
        try:
            with open(os.path.join(get_application_path(), "error_log.txt"), "w") as f:
                f.write(f"Error: {str(e)}\n")
                f.write(traceback.format_exc())
            print("Error details written to error_log.txt")
        except:
            print("Could not write to error log file")

if __name__ == "__main__":
    print("File Inventory Tool - Starting...")
    create_file_inventory()
    print("\nPress Enter to exit...")
    input()  # Keeps the window open so you can see any error messages