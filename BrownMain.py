from CFRMain import stopWords, tokenizing, termFrequencyWithoutStopWords, termFrequencyWithStopWords

# No need to strip XML tags b/c its already a text file
tokenizing("BrownCorpus.txt", "Brown-tokenSeq.txt")
termFrequencyWithStopWords("Brown-tokenSeq.txt", "Brow-termFreqStopWords.txt")
termFrequencyWithoutStopWords("Brown-tokenSeq.txt", "Brown-termFreqNoStopWords.txt")