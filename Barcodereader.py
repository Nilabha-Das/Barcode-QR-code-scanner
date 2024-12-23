import cv2
from pyzbar import pyzbar
import webbrowser

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode: " + barcode_info + "\n")
        if barcode_info.startswith("http://") or barcode_info.startswith("https://"):
            webbrowser.open(barcode_info)
            return True
    return False

def main():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        return
    scanned = False
    try:
        while True:
            ret, frame = camera.read()
            if not ret:
                break
            if not scanned:
                scanned = read_barcodes(frame)
            cv2.imshow('Barcode/QR code reader', frame)
            if cv2.waitKey(1) & 0xFF == 27 or scanned:
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
