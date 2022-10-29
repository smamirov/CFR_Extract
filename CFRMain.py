import re
from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as sklearnStopWords

def stripXMLTags(xmlFile, outputFile):
    text = re.sub('<[^<]+>', "", open(xmlFile).read())
    with open("output.txt", "w") as f:
        f.write(text)
    print(len(text))

def tokenizing(textFile, tokenSequenceOutput):
    with open(textFile, "r") as file1:
        doc = file1.read()

    tokenizer = TreebankWordTokenizer()
    tokenSequence = tokenizer.tokenize(doc.lower())
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    #with open(tokenSequenceOutput, "w") as file2:
        #file2.write(str(tokenSequence))
    with open(tokenSequenceOutput, 'w') as f:
        for line in tokenSequence:
            if line not in punc:
                f.write(f"{line}\n")

def termFrequencyWithStopWords(tokenSequenceFile, termFrequencyOutput):
    with open(tokenSequenceFile, "r") as file3:
        tokenSeq = file3.read()
    
    tokenSeq = tokenSeq.split("\n")
    bagOfWords = Counter(tokenSeq)
    with open(termFrequencyOutput, "w") as file4:
        file4.write(str(bagOfWords))

def termFrequencyWithoutStopWords(tokenSequenceFile, termFrequencyOutput):
    with open(tokenSequenceFile, "r") as file3:
        tokenSeq = file3.read()
    
    tokenSeq = tokenSeq.split("\n")
    tokenSeqWithoutStopWords = [word for word in tokenSeq if word not in sklearnStopWords]
    bagOfWords = Counter(tokenSeqWithoutStopWords)
    #print(bagOfWords.most_common(10))
    with open(termFrequencyOutput, "w") as file5:
        file5.write(str(bagOfWords))

def stopWords():
    with open("stopwords.txt", "w") as file6:
        file6.write(str(sklearnStopWords))

'''stripXMLTags("ECFR-title47.xml", "ECFR-output.txt")
stopWords()
tokenizing("ECFR-output.txt", "ECFR-tokenSeq.txt")
termFrequencyWithStopWords("ECFR-tokenSeq.txt", "ECFR-termFreqStopWords.txt")
termFrequencyWithoutStopWords("ECFR-tokenSeq.txt", "ECFR-termFreqNoStopWords.txt")'''


