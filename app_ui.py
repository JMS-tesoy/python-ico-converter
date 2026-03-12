import customtkinter as ctk
from tkinter import filedialog
import threading
from converter import convert_single_file
import tempfile
import shutil
import os
from pathlib import Path

# --- Main Application Class ---
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Icon Converter")
        self.geometry("700x500")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)

        # Initialize temporary storage
        self.temp_dir = tempfile.mkdtemp()
        self.generated_ico_path = None
        self.selected_file_path = None

        # --- Widgets ---
        self.source_label = ctk.CTkLabel(self, text="Upload Image:")
        self.source_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.file_label = ctk.CTkLabel(self, text="No file selected", text_color="gray")
        self.file_label.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ew")
        self.source_button = ctk.CTkButton(self, text="Browse", command=self.select_file)
        self.source_button.grid(row=0, column=2, padx=20, pady=(20, 10))

        self.convert_button = ctk.CTkButton(self, text="Convert to ICO", command=self.start_conversion_thread)
        self.convert_button.grid(row=1, column=1, padx=20, pady=20)

        self.download_button = ctk.CTkButton(self, text="Save to...", state="disabled", command=self.save_file, fg_color="green", hover_color="darkgreen")
        self.download_button.grid(row=2, column=1, padx=20, pady=(0, 20))

        self.log_textbox = ctk.CTkTextbox(self, state="disabled", height=200)
        self.log_textbox.grid(row=3, column=0, columnspan=3, padx=20, pady=10, sticky="nsew")
        self.grid_rowconfigure(3, weight=1)

        # Add cleanup for temporary directory on exit
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def select_folder(self, entry_widget):
        folder_path = filedialog.askdirectory()
        if folder_path:
            entry_widget.delete(0, "end")
            entry_widget.insert(0, folder_path)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image File",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            self.selected_file_path = file_path
            self.file_label.configure(text=Path(file_path).name, text_color=("black", "white"))
            # Reset download state when a new file is selected
            self.download_button.configure(state="disabled")
            self.generated_ico_path = None

    def log_message(self, message):
        self.log_textbox.configure(state="normal")
        self.log_textbox.insert("end", message + "\n")
        self.log_textbox.configure(state="disabled")
        self.log_textbox.see("end")

    def start_conversion_thread(self):
        source = self.selected_file_path
        if not source:
            self.log_message("Please upload a source file first.")
            return

        # Clear the log box for a new conversion run
        self.log_textbox.configure(state="normal")
        self.log_textbox.delete("1.0", "end")
        self.log_textbox.configure(state="disabled")
        self.convert_button.configure(state="disabled", text="Converting...")
        self.download_button.configure(state="disabled")
        
        threading.Thread(target=self.run_conversion, args=(source,)).start()

    def run_conversion(self, source):
        log_callback = lambda msg: self.after(0, self.log_message, msg)
        
        # Prepare temp file path logic
        source_path = Path(source)
        ico_name = source_path.stem + ".ico"
        temp_ico_path = Path(self.temp_dir) / ico_name
        
        # Clean up existing temp file to ensure fresh conversion
        if temp_ico_path.exists():
            os.remove(temp_ico_path)

        convert_single_file(source, self.temp_dir, log_callback)
        
        self.convert_button.configure(state="normal", text="Convert to ICO")

        if temp_ico_path.exists():
            self.generated_ico_path = temp_ico_path
            self.download_button.configure(state="normal")
            log_callback("✅ Ready to download!")

    def save_file(self):
        if not self.generated_ico_path:
            return
        
        dest_path = filedialog.asksaveasfilename(defaultextension=".ico", initialfile=self.generated_ico_path.name, filetypes=[("Icon Files", "*.ico")])
        if dest_path:
            shutil.copy(self.generated_ico_path, dest_path)
            self.log_message(f"💾 Saved to: {dest_path}")

    def on_closing(self):
        """Clean up temporary files and close the application."""
        try:
            shutil.rmtree(self.temp_dir)
        except Exception as e:
            # Log error if cleanup fails, but don't prevent exit
            print(f"Error cleaning up temp directory: {e}")
        self.destroy()

if __name__ == "__main__":
    App().mainloop()