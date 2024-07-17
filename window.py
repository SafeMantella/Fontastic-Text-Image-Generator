import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
import txtgen as tg

def select_font():
    file_path = filedialog.askopenfilename(filetypes=[("Font Files", "*.ttf")])
    font_path_entry.delete(0, tk.END)
    font_path_entry.insert(0, file_path)

def select_output_dir():
    directory = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, directory)

def select_color():
    color_code = colorchooser.askcolor(title="Choose text color")[1]
    color_entry.delete(0, tk.END)
    color_entry.insert(0, color_code)

def clear():
    text_size_entry.delete(0, tk.END)
    text_entry.delete(0, tk.END)
    font_path_entry.delete(0, tk.END)
    color_entry.delete(0, tk.END)
    output_dir_entry.delete(0, tk.END)

def generate_image():
    text_size = int(text_size_entry.get())
    text = text_entry.get()
    font_path = font_path_entry.get()
    color = color_entry.get()
    output_dir = output_dir_entry.get()
    
    try:
        message = tg.create_image(text_size, text, font_path, color, output_dir)
        messagebox.showinfo("Success", message)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate image: {e}")

# Cria a janela principal
root = tk.Tk()
root.title("Fontastic - Text Image Generator")

# Cria e posiciona os widgets na janela
tk.Label(root, text="Text Size:").grid(row=0, column=0, padx=10, pady=10)
text_size_entry = tk.Entry(root)
text_size_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Text:").grid(row=1, column=0, padx=10, pady=10)
text_entry = tk.Entry(root)
text_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Font Path:").grid(row=2, column=0, padx=10, pady=10)
font_path_entry = tk.Entry(root)
font_path_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_font).grid(row=2, column=2, padx=10, pady=10)

tk.Label(root, text="Color:").grid(row=3, column=0, padx=10, pady=10)
color_entry = tk.Entry(root)
color_entry.grid(row=3, column=1, padx=10, pady=10)
tk.Button(root, text="Choose Color", command=select_color).grid(row=3, column=2, padx=10, pady=10)

tk.Label(root, text="Output Directory:").grid(row=4, column=0, padx=10, pady=10)
output_dir_entry = tk.Entry(root)
output_dir_entry.grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_dir).grid(row=4, column=2, padx=10, pady=10)

tk.Button(root, text="Generate Image", command=generate_image).grid(row=5, column=0, columnspan=3, padx=10, pady=20)
tk.Button(root, text="Clear", command=clear).grid(row=6, column=0, columnspan=3, padx=10, pady=10)
# Inicia o loop principal da interface
root.mainloop()
