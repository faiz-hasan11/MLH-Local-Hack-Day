import googletrans
from googletrans import Translator

translator = Translator()
print("AVAILABLE LANGUAGE FOR TRANSLATION FROM ENGLISH=>")
for i in googletrans.LANGUAGE:
    print(i)
dest = input("ENTER THE LANGUAGE CODE YOU WANT QUOTE IN =>\n")
text = input("ENTER TEXT TO TRANSLATE\n")
print(translator.translate(text, src="en", dest=dest).text)
