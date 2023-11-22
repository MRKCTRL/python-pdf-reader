pip install PyPDF2
pip install pyttsx3

import PyPDF2
import pyttsx3


Reader = PyPDF2.PdfFileReader(open('clcoding.pdf', 'rb'))


speaker = pyttsx3.init()


for page_num in range(Reader.numPages): 
    text = Reader.getPage(page_num).extractText() 
    speaker.say(text)
    speaker.runAndWait()

 
speaker.stop() 
 
engine.save_to_file(text, 'E:\audio.mp3') 
engine.runAndWait()

