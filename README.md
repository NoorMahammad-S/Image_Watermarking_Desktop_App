# Image Watermarking Desktop App using GUI

This is a simple desktop application that allows you to add a watermark to images. You can use this tool to add text watermarks to your images.

## Features

- Select an input image from your computer.
- Specify the text for the watermark.
- Add the watermark to the selected image.
- Save the watermarked image to your computer.

## Prerequisites

Before running this application, make sure you have the following installed on your system:

- Python (3.x recommended)
- Python libraries: tkinter, Pillow (PIL)

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/image-watermark-app.git
   cd image-watermark-app
   ```

2. Install the required Python libraries if you haven't already:

   ```bash
   pip install pillow
   ```

3. Run the application:

   ```bash
   python image_watermark_app.py
   ```

4. The application window will open.

5. Use the "Select an Image" button to choose the image you want to watermark.

6. Enter the text for your watermark in the "Watermark Text" field.

7. Specify the output image path where you want to save the watermarked image.

8. Click the "Add Watermark" button.

9. A new image with the watermark will be saved at the specified output path.

## Customize

- You can customize the font and size of the watermark by modifying the `font = ImageFont.truetype("arial.ttf", 36)` line in the `add_watermark` function.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the tkinter library for the GUI and the Pillow library for image processing.

Feel free to contribute to this project or report any issues you encounter. Enjoy watermarking your images!
