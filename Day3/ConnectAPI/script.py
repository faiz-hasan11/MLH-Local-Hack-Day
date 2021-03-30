import requests
import googletrans
from googletrans import Translator


def get_quote():
    api = "http://api.quotable.io/random"
    quote = requests.get(api).json()
    return quote['content']


quote = get_quote()
translator = Translator()
print("AVAILABLE LANGUAGE FOR TRANSLATION=>")
for i in googletrans.LANGUAGES:
    print(i)
dest = input("ENTER THE LANGUAGE CODE YOU WANT QUOTE IN =>")
print("YOUR QUOTE =>")
print(translator.translate(quote, src="en", dest=dest).text)
