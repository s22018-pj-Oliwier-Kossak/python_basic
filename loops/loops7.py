
a1 = 0
a2 = 1
a3 = 0

for i in range(5):
    a3 = a2 + a1
    a1 = a2
    a2 = a3
print(a3)

text='''
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn't do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it's an easier-to-learn language that the
organization can implement incrementally. In addition, Python
this can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can't.
'''
listOfWords = text.replace("\n"," ").split(' ')

print(listOfWords)

for word in listOfWords:
    if word.find('p') > 0:
        print(word)

dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less than 50%'}

for keys in dictionary.keys():
    print(keys, dictionary[keys])

wordDictionary = {}

listOfWords = text.replace("\n",' ').split(' ')

for i in listOfWords:

    if i in wordDictionary.keys():
        wordDictionary[i] = wordDictionary[i] + 1
    else:
        wordDictionary[i] = 1

print(wordDictionary)