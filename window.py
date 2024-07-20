import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
import txtgen as tg

def select_font():
    file_path = filedialog.askopenfilename(filetypes=[("Font Files", "*.ttf")])
    font_path_entry.delete(0, tk.END)
    font_path_entry.insert(0, file_path)

def select_color():
    color_code = colorchooser.askcolor(title="Choose text color")[1]
    color_entry.delete(0, tk.END)
    color_entry.insert(0, color_code)

def clear():
    text_size_entry.delete(0, tk.END)
    text_entry.delete(0, tk.END)
    font_path_entry.delete(0, tk.END)
    color_entry.delete(0, tk.END)

def generate_image():
    text_size = int(text_size_entry.get())
    text = text_entry.get()
    font_path = font_path_entry.get()
    color = color_entry.get()
    invert = False
    
    try:
        message = tg.create_image(text_size, text, font_path, color, invert)
        messagebox.showinfo("Success", message)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate image: {e}")

def generate_image_inverted():
    text_size = int(text_size_entry.get())
    text = text_entry.get()
    font_path = font_path_entry.get()
    color = color_entry.get()
    invert = True
    
    try:
        message = tg.create_image(text_size, text, font_path, color, invert)
        messagebox.showinfo("Success", message)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate image: {e}")

# Cria a janela principal
root = tk.Tk()
root.title("Fontastic - Text Image Generator")

# Cria e posiciona os widgets na janela
tk.Label(root, text="Text Size:").grid(row=0, column=0, padx=10, pady=5)
text_size_entry = tk.Entry(root)
text_size_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Text:").grid(row=1, column=0, padx=10, pady=5)
text_entry = tk.Entry(root)
text_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Font Path:").grid(row=2, column=0, padx=10, pady=5)
font_path_entry = tk.Entry(root)
font_path_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_font).grid(row=2, column=2, padx=10, pady=5)

tk.Label(root, text="Color:").grid(row=3, column=0, padx=10, pady=5)
color_entry = tk.Entry(root)
color_entry.grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Choose Color", command=select_color).grid(row=3, column=2, padx=10, pady=5)

# botão para inverter as cores ao lado do botão de gerar imagem
tk.Button(root, text="Generate Image (Color on text)", command=generate_image).grid(row=5, column=0, columnspan=3, padx=10, pady=5)
tk.Button(root, text="Generate Image (Color on Backgound)", command=generate_image_inverted).grid(row=4, column=0, columnspan=3, padx=10, pady=5)
tk.Button(root, text="Clear", command=clear).grid(row=6, column=0, columnspan=3, padx=10, pady=5)

# Inicia o loop principal da interface
root.mainloop()
