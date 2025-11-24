# 🖼️ Python Batch Image Resizer

A lightweight, robust Python script to batch resize and convert images while maintaining aspect ratios. Perfect for preparing datasets, optimizing images for the web, or simply reducing file sizes.

## ✨ Features

* **Batch Processing:** Resizes all images in a folder at once.
* **Smart Resizing:** Uses `LANCZOS` filtering for high-quality downscaling.
* **Aspect Ratio Protection:** Default behavior keeps images from looking stretched.
* **Format Conversion:** Easily convert files (e.g., PNG to JPG, WEBP to PNG).
* **Transparency Safety:** Automatically handles transparent backgrounds (Alpha channels) when converting to JPEG to prevent errors.
* **Auto-Directory:** Automatically creates the output folder if it doesn't exist.

## 🛠️ Prerequisites

You need to have **Python 3** installed.

You also need the **Pillow** library (Python Imaging Library). Install it by running this command in your terminal:

```bash
pip install Pillow
📂 Project Structure
Ensure your folder looks like this before running the script:

Plaintext

/MyProject
│
├── resizer.py           # The script file
├── README.md            # This documentation
│
├── /input_images        # (Folder) Place your original photos here
└── /resized_images      # (Folder) Script will save processed photos here
🚀 Usage
You can run the script in two ways: using default settings or using custom arguments.

Option 1: Default Settings (Easiest)
By default, the script looks for a folder named input_images, resizes images to max 800x600, and saves them to resized_images while keeping the original file format.

Run this command:

Bash

python resizer.py
Option 2: Custom Settings (CLI Arguments)
You can specify folders, dimensions, and output formats directly in the command line.

Syntax:

Bash

python resizer.py [input_folder] [output_folder] [width] [height] [format]
Examples:

Resize to 1920x1080 (HD):

Bash

python resizer.py input_images output_images 1920 1080
Resize and Convert to PNG:

Bash

python resizer.py input_images output_images 500 500 PNG
Resize and Convert to WEBP (Great for web):

Bash

python resizer.py input_images output_images 1024 768 WEBP
📋 Supported Formats
The script currently supports inputs and outputs for:

JPG / JPEG

PNG

WEBP

BMP

TIFF

⚠️ Troubleshooting
"Module not found" error: Make sure you ran pip install Pillow.

"Input folder does not exist" error: Ensure you have created a folder named input_images (or whatever name you provided in the arguments) and that your photos are inside it.

Transparency lost: If you convert a PNG with a transparent background to a JPEG, the background will turn black or white. This is normal because JPEG does not support transparency.

📜 License
Free to use and modify.


---

### How to use this file:
1.  Create a new file in your folder.
2.  Name it `README.md`.
3.  Paste the text above into it and save.
4.  If you upload this code to GitHub, this text will appear as the front page of your project.

