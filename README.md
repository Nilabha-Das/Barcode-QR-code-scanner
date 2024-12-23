# Barcode-QR-code-scanner
## Overview
This project is a simple Python-based application that uses a webcam to scan barcodes and QR codes. Once a valid QR code is detected, the program decodes the information, highlights the code in the video feed, opens the link (if it is a URL) in the default web browser, and exits automatically.

## Features
- Scans barcodes and QR codes in real-time using a webcam.
- Automatically detects and decodes barcode/QR code information.
- Opens URLs in the default browser if the QR code contains a valid link.
- Saves the scanned information in a text file (`barcode_result.txt`).
- Exits automatically after processing the first valid QR code or when ESC is pressed.

## Requirements
- Python 3.7 or later
- Libraries:
  - `opencv-python`
  - `pyzbar`
  - `webbrowser` (default Python library)

## Installation
1. Clone the repository or download the script.
2. Install the required Python libraries using pip:
   ```bash
   pip install opencv-python pyzbar
   ```

## Usage
1. Connect a webcam to your system if you're using a desktop.
2. Run the script:
   ```bash
   python barcode_scanner.py
   ```
3. A window labeled "Barcode/QR code reader" will open.
4. Place a QR code or barcode in the camera's view.
5. The program will:
   - Highlight the detected barcode/QR code with a green rectangle.
   - Display the decoded information.
   - Open the URL in the default browser if the QR code contains a valid link.
6. The program will exit automatically after processing the first valid QR code or when ESC is pressed.

## Output
- **Real-time Video Feed**: Displays the webcam feed with the detected QR code highlighted.
- **File**: Saves the scanned information in `barcode_result.txt`.
- **Browser**: Opens the link (if applicable) in the default web browser.

## Troubleshooting
- Ensure your webcam is connected and accessible.
- Verify that the QR code contains valid data (e.g., properly formatted URLs).
- If the URL doesn't open, check your system's default web browser settings.

## Example
### Scanned QR Code
- Input: `https://example.com`
- Output:
  - The URL is opened in the browser.
  - The following is saved to `barcode_result.txt`:
    ```
    Recognized Barcode: https://example.com
    ```

## Acknowledgments
- OpenCV for real-time image processing.
- Pyzbar for barcode and QR code decoding.

