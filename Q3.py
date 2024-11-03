import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
ps = PorterStemmer()
def morphological_analysis(text):
    words = word_tokenize(text)
    stems = [ps.stem(word) for word in words]
    return stems
text = "running runs runner"
print(morphological_analysis(text))
