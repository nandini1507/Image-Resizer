import os
import sys
from PIL import Image

# Allowed input formats
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff")

def resize_images(input_folder, output_folder, width, height, output_format=None, maintain_aspect=True):
    processed = 0
    failed = 0

    print("\n🚀 Starting image processing...")
    print(f"🎯 Target size: {width}x{height}")
    
    if output_format:
        print(f"🖼️ Converting to: {output_format}")

    print(f"📐 Aspect ratio: {'Maintained' if maintain_aspect else 'Stretched'}\n")

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of files
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(SUPPORTED_FORMATS)]
    total_files = len(files)

    if total_files == 0:
        print("❌ No images found in input folder!")
        return

    print(f"📂 Found {total_files} images\n")

    for file in files:
        input_path = os.path.join(input_folder, file)

        try:
            img = Image.open(input_path)

            # FIX: Handle transparency (Alpha channel) if converting to JPEG
            if output_format and output_format.upper() in ["JPG", "JPEG"] and img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Resize logic
            if maintain_aspect:
                # .thumbnail modifies the image in-place and preserves aspect ratio
                img.thumbnail((width, height), Image.Resampling.LANCZOS)
            else:
                # .resize returns a new image and forces exact dimensions
                img = img.resize((width, height), Image.Resampling.LANCZOS)

            # Determine save format and filename
            save_format = output_format if output_format else img.format
            # Handle case where original format might be None (rare)
            if not save_format: 
                save_format = "JPEG"
            
            # correct extension handling
            file_name_only = os.path.splitext(file)[0]
            # Mapping specific formats to extensions if needed, strictly ensuring dot
            ext = save_format.lower()
            if ext == "jpeg": ext = "jpg"
            
            output_filename = f"{file_name_only}.{ext}"
            output_path = os.path.join(output_folder, output_filename)

            img.save(output_path, save_format)
            processed += 1
            print(f"✔ Processed: {file} -> {output_filename}")

        except Exception as e:
            print(f"❌ Failed: {file} -> {e}")
            failed += 1

    print("\n🎉 Processing Completed!")
    print(f"✔ Successful: {processed}")
    print(f"❌ Failed: {failed}\n")


def main():
    # Default values
    input_folder = "input_images"
    output_folder = "resized_images"
    width = 800
    height = 600
    output_format = None
    maintain_aspect = True

    # Argument parsing
    try:
        if len(sys.argv) > 1:
            input_folder = sys.argv[1]
        if len(sys.argv) > 2:
            output_folder = sys.argv[2]
        if len(sys.argv) > 3:
            width = int(sys.argv[3])
        if len(sys.argv) > 4:
            height = int(sys.argv[4])
        if len(sys.argv) > 5:
            output_format = sys.argv[5].upper()
            # Fix common typo where user might type .jpg instead of JPG
            output_format = output_format.replace(".", "") 
            if output_format == "JPG": output_format = "JPEG"

    except ValueError:
        print("❌ Error: Width and Height must be numbers.")
        return
    except Exception as e:
        print(f"❌ Error parsing arguments: {e}")
        return

    if not os.path.exists(input_folder):
        print(f"❌ Input folder '{input_folder}' does not exist! Please create it.")
        return

    resize_images(input_folder, output_folder, width, height, output_format, maintain_aspect)


if __name__ == "__main__":
    main()