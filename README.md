# Italian Recipe Translator

## Description:
While traveling in Italy, I picked a couple of Italian cookbooks in hopes of becoming a better cook.  My only problem?  The cookbooks were in Italian.  After spending quite a bit of time typing and speaking Italian into a translator, I decided to write my own program that could work much faster.  The program has two main functionalities: image-to-text and text-to-text translation.  The image to text portion converts text from an image into a text file while the text-to-text translation portion translates Italian text into English, outputting a translated text file.  Future versions will provide better error handling and a better, more intuitive user experience.  

## Installation:
The program relies on the PyTesseract, OpenCV and googletrans APIs.  You must have these libraries installed in order for the project to run.  

## Usage:
To start the program, navigate to the directory containing the program and type:
python test.py

The program will provide a menu with 3 options: "Image to Text", "Translate" and "Exit."  If the user selects "Image to Text," the user will be prompted to enter the name of the file the user would like to read.  For this current version, the image needs to be in the IMG folder for the program to properly find the image.  If the program is able to find the image, the image will be displayed and the user will be prompted to name the file he will be creating.  The file will then be saved to the "Italian" folder.  

If the user select "Translate", the user will instructed to provide a filename to translate.  For this current version, the file needs to be in the "Italian" folder.  If the program is able to successfully access the text file, the translated text will be displayed on the console and the user will be prompted to provide a name for the newly created file.  This file will then be available in the "English" folder.  

Selecting "Exit" will exit the program.

## Credits
This program uses PyTesseract, OpenCV and googletrans libraries.  
