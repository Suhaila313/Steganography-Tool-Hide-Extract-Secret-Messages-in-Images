
# 🖼️ Steganography Tool – Hide & Extract Secret Messages in Images

A simple Python-based GUI application that lets you hide secret messages inside image files using **Least Significant Bit (LSB) steganography**. Built with **Tkinter** and **Stepic**, this tool provides an easy-to-use interface for both embedding and extracting hidden text.


## 🎯 Objective

To demonstrate how information can be concealed within image pixels using steganography techniques and retrieved later without any noticeable difference to the image.

## 🧰 Technologies Used

| Component        | Technology       |
| ---------------- | ---------------- |
| GUI Framework    | Tkinter (Python) |
| Image Processing | Pillow (PIL)     |
| Steganography    | Stepic Library   |


## ⚙️ Features

✅ Simple GUI with **two tabs** – Embed and Extract
✅ Supports `.png` and `.bmp` image formats
✅ Allows hiding any text message inside an image
✅ Extracts hidden messages from stego images
✅ Auto-generates file names for stego images


## 📦 How to Run

### 1. Clone the Repository

git clone https://github.com/yourusername/steganography-tool.git
cd steganography-tool

### 2. Install Required Packages

pip install pillow stepic

### 3. Run the Application

python stego_gui.py

> You’ll see a window with two tabs: “Embed Data” and “Extract Data”.


## 🖥️ How It Works

### 🔐 Embed Process:

1. Select a cover image (`.png` or `.bmp`)
2. Enter your secret text in the text box
3. Choose the output file path
4. Click **"Embed Data"**
   👉 A new image file will be saved with your hidden message

### 🔍 Extract Process:

1. Select a stego image with a hidden message
2. Click **"Extract Data"**
3. The secret message will be shown in the text area


## 🧪 Example

* Cover image: `cover.png`
* Secret message: `The password is cyber123`
* Output file: `cover_stego.png`
* Later extraction from `cover_stego.png` will reveal `The password is cyber123`


## ✅ Use Cases

* Educational demonstration of steganography
* Practicing data hiding techniques in cybersecurity
* A fun way to exchange hidden messages through images



## 👤 Author

Suhaila P.S
Cybersecurity Enthusiast & Python Developer

