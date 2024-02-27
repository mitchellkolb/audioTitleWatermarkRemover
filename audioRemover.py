"""
#removes the text in front of every file for spotify songs downloaded from that one site.
 
""" 
import os
import tkinter
from tkinter import filedialog, messagebox
import customtkinter

def removeprefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    else:
        return text

def removeLabel():
    try:
        if folder_path == "":
            tkinter.messagebox.showwarning("Warning", "No folder selected.")
            return
        
        prefix = '[SPOTIFY-DOWNLOADER.COM] '
        files_renamed = 0

        for file in os.listdir(folder_path):
            filepath = os.path.join(folder_path, file)
            if file.startswith(prefix):
                new_filename = removeprefix(file, prefix)
                new_filepath = os.path.join(folder_path, new_filename)
                os.rename(filepath, new_filepath)
                files_renamed += 1

        if files_renamed > 0:
            tkinter.messagebox.showinfo("Success", "Successful", icon='info')
        else:
            tkinter.messagebox.showinfo("Info", "No files needed renaming.", icon='info')
    except Exception as e:
        print(e)  # Printing the exception to the console (optional)
        tkinter.messagebox.showerror("Error", "Failed", icon='error')

def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()  # Open the dialog to choose a folder
    if folder_path:  # Check if a folder was selected
        print(f"Folder selected: {folder_path}")
        # Extract the last part of the folder path and update the label
        folder_name = os.path.basename(folder_path)
        selected_folder_label.configure(text=f"/{folder_name}")  # Update label text using 'configure'
    else:
        folder_path = ""  # Reset folder path if no folder is selected
        print("No folder was selected.")
        selected_folder_label.configure(text="")  # Clear label text using 'configure'

def start_rename():
    if folder_path:
        removeLabel()
    else:
        tkinter.messagebox.showwarning("Warning", "Please select a folder first.")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("200x150")  # Adjust the window size
app.title("Audio Remover")

# Label for showing the selected folder's last part
selected_folder_label = customtkinter.CTkLabel(app, text="")
selected_folder_label.pack(padx=10, pady=5)

# title = customtkinter.CTkLabel(app, text="Select Audio Folder")
# title.pack(padx=10, pady=10)

select_folder_button = customtkinter.CTkButton(app, text="Select Folder", command=select_folder)
select_folder_button.pack(padx=10, pady=10)

start_button = customtkinter.CTkButton(app, text="Start", command=start_rename)
start_button.pack(padx=10, pady=10)

folder_path = ""  # Initialize the folder_path variable

app.mainloop()
