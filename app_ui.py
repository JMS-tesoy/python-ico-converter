import customtkinter as ctk
from tkinter import BooleanVar, filedialog
import threading
from tkinterdnd2 import TkinterDnD, DND_FILES
from converter import DEFAULT_ICO_SIZES, convert_single_file
import tempfile
import shutil
import os
from pathlib import Path

USER_MANUAL_TEXT = """Icon Converter Beginner Manual

What this app does
This app turns an image file into a Windows icon file.
The new file will end with .ico.

Supported image files
- PNG files
- JPG files
- JPEG files

How to convert an image
1. Click the Browse button.
2. Choose the image you want to convert.
3. Select at least one icon size.
4. Click Convert to ICO.
5. Wait until the log says the icon is ready.
6. Click Save to...
7. Choose where you want to save the new .ico file.

About icon sizes
The boxes under Icon Sizes control which pixel sizes are placed inside the icon file.

Common choices:
- 16x16: Very small icon size.
- 32x32: Common desktop and app icon size.
- 48x48: Larger Windows icon size.
- 64x64: Useful for larger displays.
- 128x128: High-quality large icon size.
- 256x256: Best quality Windows icon size.

If you are not sure what to choose, select 32x32, 48x48, and 256x256.

Important notes
- At least one icon size must be selected.
- The app will not stretch wide or tall images.
- Non-square images are centered inside a transparent square icon.
- After choosing a new image, convert it again before saving.

Drag and drop
You can drag a PNG, JPG, or JPEG file into the app window instead of using Browse.

If something does not work
- Make sure the file is a PNG, JPG, or JPEG.
- Make sure at least one icon size is selected.
- Try saving to a normal folder like Desktop or Documents.
- If Windows shows a security warning, choose More info, then Run anyway only if you trust this app.
"""

# --- Main Application Class ---
class App(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self):
        super().__init__()
        self.TkdndVersion = TkinterDnD._require(self)

        self.title("Icon Converter")
        self.geometry("700x500")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)

        # Initialize temporary storage
        self.temp_dir = tempfile.mkdtemp()
        self.generated_ico_path = None
        self.selected_file_path = None
        self.size_options = list(DEFAULT_ICO_SIZES)
        self.size_vars = {}

        # --- Widgets ---
        self.source_label = ctk.CTkLabel(self, text="Upload Image:")
        self.source_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.file_label = ctk.CTkLabel(self, text="No file selected", text_color="gray")
        self.file_label.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ew")
        self.source_button = ctk.CTkButton(self, text="Browse", command=self.select_file)
        self.source_button.grid(row=0, column=2, padx=20, pady=(20, 10))

        self.size_label = ctk.CTkLabel(self, text="Icon Sizes:")
        self.size_label.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nw")
        self.size_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.size_frame.grid(row=1, column=1, columnspan=2, padx=20, pady=(10, 10), sticky="w")

        for index, size in enumerate(self.size_options):
            var = BooleanVar(value=False)
            self.size_vars[size] = var
            checkbox = ctk.CTkCheckBox(
                self.size_frame,
                text=f"{size}x{size}",
                variable=var,
            )
            checkbox.grid(row=index // 3, column=index % 3, padx=(0, 18), pady=4, sticky="w")

        self.convert_button = ctk.CTkButton(self, text="Convert to ICO", command=self.start_conversion_thread)
        self.convert_button.grid(row=2, column=1, padx=20, pady=20)

        self.manual_button = ctk.CTkButton(self, text="User Manual", command=self.show_user_manual)
        self.manual_button.grid(row=2, column=2, padx=20, pady=20)

        self.download_button = ctk.CTkButton(self, text="Save to...", state="disabled", command=self.save_file, fg_color="green", hover_color="darkgreen")
        self.download_button.grid(row=3, column=1, padx=20, pady=(0, 20))

        self.log_textbox = ctk.CTkTextbox(self, state="disabled", height=200)
        self.log_textbox.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)

        # Add cleanup for temporary directory on exit
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Enable drag and drop
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.drop_event)

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
            self.load_file(file_path)

    def load_file(self, file_path):
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

    def show_user_manual(self):
        manual_window = ctk.CTkToplevel(self)
        manual_window.title("Icon Converter User Manual")
        manual_window.geometry("640x560")
        manual_window.transient(self)

        manual_window.grid_columnconfigure(0, weight=1)
        manual_window.grid_rowconfigure(1, weight=1)

        title_label = ctk.CTkLabel(
            manual_window,
            text="Icon Converter User Manual",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        manual_textbox = ctk.CTkTextbox(manual_window, wrap="word")
        manual_textbox.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        manual_textbox.insert("1.0", USER_MANUAL_TEXT)
        manual_textbox.configure(state="disabled")

    def start_conversion_thread(self):
        source = self.selected_file_path
        if not source:
            self.log_message("Please upload a source file first.")
            return
        
        selected_sizes = self.get_selected_sizes()
        if not selected_sizes:
            self.log_message("Please select at least one icon size.")
            return

        # Clear the log box for a new conversion run
        self.log_textbox.configure(state="normal")
        self.log_textbox.delete("1.0", "end")
        self.log_textbox.configure(state="disabled")
        self.convert_button.configure(state="disabled", text="Converting...")
        self.download_button.configure(state="disabled")
        
        threading.Thread(target=self.run_conversion, args=(source, selected_sizes)).start()

    def get_selected_sizes(self):
        return [
            size for size, var in self.size_vars.items()
            if var.get()
        ]

    def run_conversion(self, source, selected_sizes):
        log_callback = lambda msg: self.after(0, self.log_message, msg)
        
        # Prepare temp file path logic
        source_path = Path(source)
        ico_name = source_path.stem + ".ico"
        temp_ico_path = Path(self.temp_dir) / ico_name
        
        # Clean up existing temp file to ensure fresh conversion
        if temp_ico_path.exists():
            os.remove(temp_ico_path)

        convert_single_file(source, self.temp_dir, log_callback, selected_sizes)
        
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

    def drop_event(self, event):
        file_path = event.data
        # Handle path formatting (remove curly braces added by Windows for paths with spaces)
        if file_path.startswith('{') and file_path.endswith('}'):
            file_path = file_path[1:-1]
        
        self.load_file(file_path)

if __name__ == "__main__":
    App().mainloop()
