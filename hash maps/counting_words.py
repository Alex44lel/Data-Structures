import unittest


class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word
        self.words_to_counts = {}
        
    
        
        chars_to_skip= (".",",",";",":","?","¿","!","¡","="," ","","(",")","[","]","-")
        
        
        currentWord=[]
        for i in range(0,len(input_string)+1):
            
            if i<len(input_string) and input_string[i] not in chars_to_skip:
                currentWord.append(input_string[i])
                
                
            else:
                if(len(currentWord)):
                    separator=""
                    word = separator.join(currentWord)
                    if word in self.words_to_counts:
                        self.words_to_counts[word]=self.words_to_counts[word]+1
                    else:
                        self.words_to_counts[word]=1
                currentWord = []


#this approach has some caveats