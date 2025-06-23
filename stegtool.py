import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from PIL import Image
import stepic
import numpy as np

class StegoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Tool")
        self.root.geometry("600x400")
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)
        
        # Embed Tab
        self.embed_frame = ttk.Frame(self.notebook, width=600, height=400)
        self.notebook.add(self.embed_frame, text="Embed Data")
        
        # Extract Tab
        self.extract_frame = ttk.Frame(self.notebook, width=600, height=400)
        self.notebook.add(self.extract_frame, text="Extract Data")
        
        self.create_embed_widgets()
        self.create_extract_widgets()
    
    def create_embed_widgets(self):
        # Cover Image Selection
        ttk.Label(self.embed_frame, text="Cover Image:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.cover_path = tk.StringVar()
        ttk.Entry(self.embed_frame, textvariable=self.cover_path, width=40).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.embed_frame, text="Browse", command=self.browse_cover_image).grid(row=0, column=2, padx=5, pady=5)

        # Secret Data
        ttk.Label(self.embed_frame, text="Secret Data:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.secret_data = tk.Text(self.embed_frame, width=40, height=5)
        self.secret_data.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        # Output Path
        ttk.Label(self.embed_frame, text="Output Image:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.output_path = tk.StringVar()
        ttk.Entry(self.embed_frame, textvariable=self.output_path, width=40).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(self.embed_frame, text="Browse", command=self.browse_output_image).grid(row=2, column=2, padx=5, pady=5)

        # Embed Button
        ttk.Button(self.embed_frame, text="Embed Data", command=self.embed_data).grid(row=3, column=1, pady=15)
    
    def browse_cover_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp")])
        if filename:
            self.cover_path.set(filename)
            # Auto-generate output filename
            base, ext = os.path.splitext(filename)
            self.output_path.set(f"{base}_stego{ext}")

    def browse_output_image(self):
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("BMP Files", "*.bmp")])
        if filename:
            self.output_path.set(filename)
    
    def embed_data(self):
        # Get all the input values
        cover_path = self.cover_path.get()
        secret_text = self.secret_data.get("1.0", tk.END).strip()
        output_path = self.output_path.get()
        
        if not all([cover_path, secret_text, output_path]):
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            # Open the cover image
            image = Image.open(cover_path)
            
            # Encode the data
            encoded_image = stepic.encode(image, secret_text.encode('utf-8'))
            
            # Save the result
            encoded_image.save(output_path)
            messagebox.showinfo("Success", f"Data embedded successfully in {output_path}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to embed data: {str(e)}")
    
    def create_extract_widgets(self):
        # Input Image Selection
        ttk.Label(self.extract_frame, text="Stego Image:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.stego_path = tk.StringVar()
        ttk.Entry(self.extract_frame, textvariable=self.stego_path, width=40).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.extract_frame, text="Browse", command=self.browse_stego_image).grid(row=0, column=2, padx=5, pady=5)

        # Extracted Data
        ttk.Label(self.extract_frame, text="Extracted Data:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.extracted_data = tk.Text(self.extract_frame, width=40, height=5, state="normal")
        self.extracted_data.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        # Extract Button
        ttk.Button(self.extract_frame, text="Extract Data", command=self.extract_data).grid(row=2, column=1, pady=15)
    
    def browse_stego_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp")])
        if filename:
            self.stego_path.set(filename)
    
    def extract_data(self):
        stego_path = self.stego_path.get()
        
        if not stego_path:
            messagebox.showerror("Error", "Please select an image file")
            return
        
        try:
            # Open the stego image
            image = Image.open(stego_path)
            
            # Decode the data
            decoded_data = stepic.decode(image)
            
            # Display the result
            self.extracted_data.config(state="normal")
            self.extracted_data.delete("1.0", tk.END)
            self.extracted_data.insert("1.0", decoded_data)
            self.extracted_data.config(state="disabled")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract data: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StegoApp(root)
    root.mainloop()