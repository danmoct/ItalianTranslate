import cv2
import pytesseract
from googletrans import Translator
from os import path


def text_Read():
	imPath = input("Enter a filename to read: ")
	fPath = path.join('../IMG',imPath)
	img = cv2.imread(fPath)
	cv2.imshow("picture", img)
	cv2.waitKey(0)
	text = pytesseract.image_to_string(img)
	save = input("Enter a filename to save:")
	sPath = path.join('../Italian',save)
	file = open(sPath, "w")
	file.write(text)
	file.close()
	return text

def tTranslate():
	translator = Translator()
	file = input("Enter a filename to read: ")
	fPath = path.join('../Italian',file)
	file = open(fPath, 'r')
	text = file.read()
	text2 = (translator.translate(text, src = 'it' ,dest = 'en').text)
	print(text2)
	save = input("Enter a filename to save:")
	sPath = path.join('../English',save)
	file = open(sPath,'w')
	file.write(text2)
	file.close()

def main():
	print("\t\t\t\t\t\tMenu")
	print("---------------------------")
	print("1. Image to Text")
	print("2. Translate")

	value = int(input("Select an option: "))
	while value != 1 and value !=2:
		value = int(input("Select an option: "))
	if value == 1:
		text_Read()
	if value == 2:
		tTranslate()

if __name__ == "__main__":
	main()

