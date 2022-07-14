from typing import Text
from textblob import TextBlob, Word

for text in ("how are you doing", "another sily mistake", "i am responsible"):
    TextBlob(text).correct()
    TextBlob("how are you doing")
    TextBlob("another silk mistake")
    TextBlob("I am responsible")


w = Word('sily')
khalil = w.spellcheck()
print(khalil)
