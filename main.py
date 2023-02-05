with open('books/frankenstein.txt') as f:
    file_contents = f.read().lower()

def wordCounter(file):
    words = file.split()
    return len(words)

def letterList(file):
    letterDict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
    'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in file:
        match i:
            case 'a':
                letterDict['a'] += 1
            case 'b':
                letterDict['b'] += 1
            case 'c':
                letterDict['c'] += 1
            case 'd':
                letterDict['d'] += 1
            case 'e':
                letterDict['e'] += 1
            case 'e':
                letterDict['e'] += 1
            case 'f':
                letterDict['f'] += 1
            case 'g':
                letterDict['g'] += 1
            case 'h':
                letterDict['h'] += 1
            case 'i':
                letterDict['i'] += 1
            case 'j':
                letterDict['j'] += 1
            case 'k':
                letterDict['k'] += 1
            case 'l':
                letterDict['l'] += 1
            case 'm':
                letterDict['m'] += 1
            case 'n':
                letterDict['n'] += 1
            case 'o':
                letterDict['o'] += 1
            case 'p':
                letterDict['p'] += 1
            case 'q':
                letterDict['q'] += 1
            case 'r':
                letterDict['r'] += 1
            case 's':
                letterDict['s'] += 1
            case 't':
                letterDict['t'] += 1
            case 'u':
                letterDict['u'] += 1
            case 'v':
                letterDict['v'] += 1
            case 'w':
                letterDict['w'] += 1
            case 'x':
                letterDict['x'] += 1
            case 'y':
                letterDict['y'] += 1
            case 'z':
                letterDict['z'] += 1
    return letterDict.items()

def sortKey(e):
    return e[1]

def main():
    wordList = list(letterList(file_contents))
    wordList.sort(key=sortKey, reverse=True)
    wordCount = wordCounter(file_contents)
    
    print('---Book Report of your Chosen Book---')
    print(str(wordCount) + ' words are present inside the document')
    print()
    for i in range(0, len(wordList)):
        print("The character '" + wordList[i][0] + "' is found " + str(wordList[i][1]) + " times")
    print('---End of Report---')

main()