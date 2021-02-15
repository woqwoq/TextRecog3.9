import cv2
import pytesseract
from tkinter import *
from tkinter import filedialog


window = Tk()
window.title('Text Recognizer')
filename = filedialog.askopenfilename()

filename = filename[45:66]
print(len(filename))
print(filename)

def main():
    #pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\\Tesseract-OCR\\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = 'pyTesseract path'

    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    RecognizedText_Str = pytesseract.image_to_string(img)
    print(RecognizedText_Str)

    config = r'--oem 3 --psm 6'

    data = pytesseract.image_to_data(img, config=config)
    for i, el in enumerate(data.splitlines()):
        if i == 0:
            continue
        el = el.split()
        try:
            x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
            cv2.rectangle(img, (x,y), (w + x, h + y), (0, 0, 255), 1)
            cv2.putText(img, el[11], (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        except IndexError:
            print("Skipped")
    RecognizedTextLabel = Label(text=RecognizedText_Str,
                                font=("Arial 32",
                                10, "bold"))
    RecognizedTextLabel.pack()
    cv2.imshow('Result', img)
    cv2.waitKey(0)
recogButton = Button(text="Recognize",
                     width=15,
                     height=5)
recogButton.config(command=main)
recogButton.pack()
window.mainloop()
