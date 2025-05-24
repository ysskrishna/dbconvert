import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from dbconvert.converters.converter_factory import ConverterFactory
from dbconvert.writers.sqlite_writer import SQLiteWriter
from dbconvert.core.enums import DatabaseType


class DbConvertGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DbConvert")
        self.root.minsize(600, 400)
        
        self.setup_ui()

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
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=20)
        
        # Convert button
        ttk.Button(main_frame, text="Convert", command=self.convert).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Status label
        self.status_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.status_var).grid(row=5, column=0, columnspan=2, pady=5)
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def browse_sqlite(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".sqlite",
            filetypes=[("SQLite databases", "*.sqlite"), ("All files", "*.*")]
        )
        if filename:
            self.sqlite_path.set(filename)

    def convert(self):
        try:
            # Validate inputs
            if not self.conn_string.get():
                messagebox.showerror("Error", "Please enter a connection string")
                return
            if not self.sqlite_path.get():
                messagebox.showerror("Error", "Please select a SQLite file path")
                return

            # Start progress bar
            self.progress.start()
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
            self.progress.stop()
            self.status_var.set("Conversion completed successfully!")
            messagebox.showinfo("Success", "Database conversion completed successfully!")

        except Exception as e:
            self.progress.stop()
            self.status_var.set("Error occurred during conversion")
            messagebox.showerror("Error", str(e))
    
    def mainloop(self):
        self.root.mainloop()

def main():
    app = DbConvertGUI()
    app.mainloop()

if __name__ == "__main__":
    main() 