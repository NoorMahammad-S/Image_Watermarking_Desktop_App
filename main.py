import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
    input_image_entry.delete(0, tk.END)
    input_image_entry.insert(0, file_path)

def add_watermark():
    input_path = input_image_entry.get()
    output_path = output_image_entry.get()
    watermark_text = watermark_text_entry.get()

    try:
        image = Image.open(input_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 36)  # You can specify your own font and size
        draw.text((20, 20), watermark_text, fill=(255, 0, 0), font=font)  # Red watermark text
        image.save(output_path)
        messagebox.showinfo("Success", "Watermark added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

app = tk.Tk()
app.title("Image Watermarking App")
app.geometry("500x300")  # Set the initial window size

app.configure(bg="#3498db")  # Background color for the main window

# Label styles
label_style = {
    "font": ("Helvetica", 12),
    "bg": "green",  # Background color for labels
    "fg": "white"  # Text color for labels
}

# Title Label
title_label = tk.Label(app, text="Image Watermarking Desktop App", font=("Helvetica", 16, "bold"), bg="#3498db")
title_label.pack(pady=10)

# Input Image Frame
input_image_frame = tk.Frame(app)
input_image_frame.pack(pady=10)

input_image_label = tk.Label(input_image_frame, text="Select an Image:", font=("Helvetica", 10, "bold"))
input_image_label.pack(side="left")

input_image_entry = tk.Entry(input_image_frame, width=40)
input_image_entry.pack(side="left")

input_image_button = tk.Button(input_image_frame, text="Browse", command=select_image, font=("Helvetica", 10))
input_image_button.pack(side="left")

# Watermark Text Frame
watermark_text_frame = tk.Frame(app)
watermark_text_frame.pack(pady=10)

watermark_text_label = tk.Label(watermark_text_frame, text="Watermark Text:", font=("Helvetica", 12))
watermark_text_label.pack(side="left")

watermark_text_entry = tk.Entry(watermark_text_frame, width=30, font=("Helvetica", 12, "bold"))
watermark_text_entry.pack(side="left")

# Output Image Frame
output_image_frame = tk.Frame(app)
output_image_frame.pack(pady=10)

output_image_label = tk.Label(output_image_frame, text="Output Image Path:",font=("Helvetica", 10, "bold"))
output_image_label.pack(side="left")

output_image_entry = tk.Entry(output_image_frame, width=40)
output_image_entry.pack(side="left")

# Add Watermark Button
add_watermark_button = tk.Button(app, text="Add Watermark", command=add_watermark, font=("Helvetica", 14, "bold"), bg="green")
add_watermark_button.pack(pady=10)

app.mainloop()
