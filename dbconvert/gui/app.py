import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from dbconvert.converters.converter_factory import ConverterFactory
from dbconvert.writers.sqlite_writer import SQLiteWriter
from dbconvert.core.enums import DatabaseType
from dbconvert.core.loggingsetup import LoggerManager
import os
from PIL import Image, ImageTk

logger = LoggerManager.get_logger()

class DbConvertGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DbConvert")
        self.root.minsize(600, 400)

        self.setup_window_icon()
        self.setup_ui()
        self.setup_logging()
    
    def setup_window_icon(self):
        logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
        if os.path.exists(logo_path):
            try:
                icon = Image.open(logo_path)
                icon = icon.resize((32, 32), Image.Resampling.LANCZOS)
                icon_photo = ImageTk.PhotoImage(icon)
                self.root.iconphoto(True, icon_photo)
            except Exception as e:
                logger.error(f"Could not set window icon: {str(e)}")

    def setup_logging(self):
        # Create a text widget for logging
        self.log_text = tk.Text(self.root, height=10, width=50)
        self.log_text.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=5)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.log_text.yview)
        scrollbar.grid(row=6, column=2, sticky=(tk.N, tk.S))
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        # Configure the logger to use the text widget
        LoggerManager.set_gui_logger(self.log_text)

    def setup_ui(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Database type selection
        ttk.Label(main_frame, text="Database Type:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.db_type = tk.StringVar(value=DatabaseType.values()[0])
        db_combo = ttk.Combobox(main_frame, textvariable=self.db_type, values=DatabaseType.values(), state="readonly")
        db_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Connection string
        ttk.Label(main_frame, text="Connection String:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.conn_string = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.conn_string, width=50).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # SQLite file path
        ttk.Label(main_frame, text="SQLite File Path:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.sqlite_path = tk.StringVar()
        path_frame = ttk.Frame(main_frame)
        path_frame.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        ttk.Entry(path_frame, textvariable=self.sqlite_path, width=40).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(path_frame, text="Browse", command=self.browse_sqlite).pack(side=tk.RIGHT, padx=5)
        
        # Convert button
        ttk.Button(main_frame, text="Convert", command=self.convert).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Status label
        self.status_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.status_var).grid(row=5, column=0, columnspan=2, pady=5)
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(6, weight=1)

    def browse_sqlite(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".sqlite",
            filetypes=[("SQLite databases", "*.sqlite"), ("All files", "*.*")]
        )
        if filename:
            self.sqlite_path.set(filename)

    def convert(self):
        logger = LoggerManager.get_logger()
        try:
            # Validate inputs
            if not self.conn_string.get():
                logger.error("Please enter a connection string")
                messagebox.showerror("Error", "Please enter a connection string")
                return
            if not self.sqlite_path.get():
                logger.error("Please select a SQLite file path")
                messagebox.showerror("Error", "Please select a SQLite file path")
                return

            self.status_var.set("Converting...")
            self.root.update()

            # Create converter
            converter = ConverterFactory.create_converter(
                self.db_type.get(),
                self.conn_string.get()
            )

            # Read source database
            tables = converter.read_all_tables()

            # Write to SQLite
            writer = SQLiteWriter(self.sqlite_path.get())
            writer.write_all_tables(tables)

            # Show success message
            logger.info("Conversion completed successfully!")
            self.status_var.set("Conversion completed successfully!")
            messagebox.showinfo("Success", "Database conversion completed successfully!")

        except Exception as e:
            logger.error(f"Error occurred during conversion: {str(e)}")
            self.status_var.set("Error occurred during conversion")
            messagebox.showerror("Error", str(e))
    
    def mainloop(self):
        self.root.mainloop()

def main():
    app = DbConvertGUI()
    app.mainloop()

if __name__ == "__main__":
    main() 