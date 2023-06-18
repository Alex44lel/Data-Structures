import unittest


def reverse_words(message):

    # Decode the message by reversing the words
    reverse_characters(0,len(message)-1,message)
    
    start=0
    end=0
    print(message)
    for element in message:
        
        if element == " ":
            reverse_characters(start,end-1,message)
            start=end+1
            
        if end == len(message)-1:
            reverse_characters(start,end,message)
        end +=1


def reverse_characters(start_index,end_index,pharse):
    print(start_index,end_index)
    while start_index < end_index:
        pharse[start_index],pharse[end_index] = pharse[end_index],pharse[start_index]
        
        start_index+=1
        end_index-=1
        
    
    






# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)