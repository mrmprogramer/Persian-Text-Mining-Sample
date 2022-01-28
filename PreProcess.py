from operator import le
from hazm import Normalizer,Stemmer







def stemmingandcounting(s):
    # https://github.com/sobhe/hazm
    wordlist = getwords(open('whitoutstopword/'+s, 'r', encoding='utf-8').read())
    stemmset= set() #use set to distinct list 
    stemmer = Stemmer()
    for word in wordlist:
        stemmset.add(stemmer.stem(word)+';;'+str(wordlist.count(word)))
    pl('stemm set size : '+str(len(stemmset)))
    writetoFile('stemmsets/'+s,'\n'.join(stemmset))







def removestopwords(s):
    # https://www.ranks.nl/stopwords/persian
    wordlist = getwords(open('normalize/'+s, 'r', encoding='utf-8').read())
    # stopwords = open('stopwordlist.txt', 'r', encoding='utf-8').read().split('\n')
    pl('allword:'+str(len(wordlist)))
    for stopword in open('stopwordlist.txt', 'r', encoding='utf-8').read().split('\n'):
        if(wordlist.__contains__(stopword)):
            wordlist.remove(stopword)
    pl('after remove Stop word:'+str(len(wordlist)))
    writetoFile('whitoutstopword/'+s,' '.join(wordlist))
    
def Normalize(s):
    # https://github.com/sobhe/hazm
   normalizer = Normalizer()
   text = normalizer.normalize(open('datamodel/'+s, 'r', encoding='utf-8').read())
   writetoFile('normalize/'+s,text)

def getwords(string):
    s = list()
    for line in string.split('\n'):
        for word in line.split(' '):
            s.append(word)
    return s


def writetoFile(fileurl,string):
    # Open a file with access mode 'a'
        file_object = open(fileurl, 'w', encoding='utf-8')
    # Append 'hello' at the end of file
        file_object.write(string)
    # Close the file
        file_object.close()


def pl(string):
    print(string)
# Open a file with access mode 'a'
    file_object = open('ExcuteLog.txt', 'a', encoding='utf-8')
# Append 'hello' at the end of file
    file_object.write(string+'\n')
# Close the file
    file_object.close()






# from sets import Set


