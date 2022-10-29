import re
from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as sklearnStopWords

# This functions strips all tags from the XML Document
# and creates a text file without the tags.
# Ex. <Title>, <Head>, etc.
def stripXMLTags(xmlFile, outputFile):
    text = re.sub('<[^<]+>', "", open(xmlFile).read())
    with open("output.txt", "w") as f:
        f.write(text)
    print(len(text))

# This functions creates a token sequence from a text file and writes to 
# a separate file.
# Also doesn't add punctuations (can add them by commenting out lines 27 and 28).
def tokenizing(textFile, tokenSequenceOutput):
    with open(textFile, "r") as file1:
        doc = file1.read()

    tokenizer = TreebankWordTokenizer()
    tokenSequence = tokenizer.tokenize(doc.lower())
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

    with open(tokenSequenceOutput, 'w') as f:
        for line in tokenSequence:
            if line not in punc:
                f.write(f"{line}\n")

# This functions gets the word frequency including stop words.
# Writes the results to a text file.
def termFrequencyWithStopWords(tokenSequenceFile, termFrequencyOutput):
    with open(tokenSequenceFile, "r") as file3:
        tokenSeq = file3.read()
    
    tokenSeq = tokenSeq.split("\n")
    bagOfWords = Counter(tokenSeq)
    with open(termFrequencyOutput, "w") as file4:
        file4.write(str(bagOfWords))

# Same as above function except it leaves out stop words.
def termFrequencyWithoutStopWords(tokenSequenceFile, termFrequencyOutput):
    with open(tokenSequenceFile, "r") as file3:
        tokenSeq = file3.read()
    
    tokenSeq = tokenSeq.split("\n")
    tokenSeqWithoutStopWords = [word for word in tokenSeq if word not in sklearnStopWords]
    bagOfWords = Counter(tokenSeqWithoutStopWords)
    #print(bagOfWords.most_common(10))
    with open(termFrequencyOutput, "w") as file5:
        file5.write(str(bagOfWords))

# A function that writes all the stopwords to a text file.
def stopWords():
    with open("stopwords.txt", "w") as file6:
        file6.write(str(sklearnStopWords))

# Uncomment the below lines to run 
'''stripXMLTags("ECFR-title47.xml", "ECFR-output.txt")
stopWords()
tokenizing("ECFR-output.txt", "ECFR-tokenSeq.txt")
termFrequencyWithStopWords("ECFR-tokenSeq.txt", "ECFR-termFreqStopWords.txt")
termFrequencyWithoutStopWords("ECFR-tokenSeq.txt", "ECFR-termFreqNoStopWords.txt")'''


