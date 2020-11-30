import pyzbar.pyzbar as pyzbar
import cv2
class Barcode:
    def readBarcode(self):
        cap = cv2.VideoCapture(0)
        i = 0
        while (cap.isOpened()):
            ret, img = cap.read()

            if not ret:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            decoded = pyzbar.decode(gray)

            for d in decoded:
                barcode_data = d.data.decode("utf-8")
                return barcode_data

            cv2.imshow('img', img)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord('s'):
                i += 1
                cv2.imwrite('c_%03d.jpg' % i, img)

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    barcode = Barcode()
    print(barcode.readBarcode())
