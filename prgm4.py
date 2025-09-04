str = '''New Delhi is the Capital of India.
Bangalore is a Capital of Karnataka. Karnataka is India.
India is the worlds largest Democratic Country '''

print("Entered Paragraph\n"+str)

wordCount= len(str.split())
print("Total Number of words", wordCount)


counts = dict()
words=str.split()

for word in words:
    if word in counts:
        counts[word] = counts[word]+1
    else:
        counts[word] = 1

print("Word Frequency: ", counts)
searchWord=input("\nEnter the word to search: ")

result = str.find(searchWord)
if(result != -1):
    print(searchWord + " Word found in Paragraph")
else:
    print(searchWord + " !!!!! Word not found in Paragraph")
