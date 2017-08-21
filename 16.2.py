'''
Word Frequencies: Design a method to find the frequency of occurrences of any given word
in a book. What if we were running this algorithm multiple times?
'''

#global variable of sorts
freq = {}

def store_frequencies(book):
	book = book.split(" ")
	for word in book:
		word = word.lower()
		if word in freq:
			freq[word] += 1
		else:
			freq[word] = 1


book1 = "The quick brown fox jumped over the lazy dogs"
store_frequencies(book1)
print(freq)
book2 = "the quick girl skipped under the bridge"
store_frequencies(book2)
print(freq)

