from operator import le
from tkinter import N
import PreProcess as pr
from hazm import Normalizer,Stemmer
from os import listdir
from os.path import isfile, join

def responsequery(query):
    queryresponse = list()

    #normalize
    normalizer = Normalizer()
    ntext = normalizer.normalize(query)
    
   
    #remove stopwords 
    wordlist = pr.getwords(ntext)
 
    for stopword in open('stopwordlist.txt', 'r', encoding='utf-8').read().split('\n'):
        if(wordlist.__contains__(stopword)):
            wordlist.remove(stopword)

    #stemmer
    stemmset= set()
    stemmer = Stemmer()
    for word in wordlist:
        stemmset.add(stemmer.stem(word))


    #read all index file 
    files = [f for f in listdir('stemmsets') if isfile(join('stemmsets', f))]
    dfwordlist=list()
    for sfile in files:
        fwords=list()
        lines = open('stemmsets/'+sfile, 'r', encoding='utf-8').read()
        if any(ext in lines for ext in stemmset):
            for line in lines.split('\n'):
                for idx,val in  enumerate(stemmset):
                    if(line.__contains__(val)):
                        dfwordlist.append({
                            'word': wordlist[idx],
                            'stem': line.split(';;')[0],
                            'file':sfile
                        })   
                        fwords.append({
                            'word': wordlist[idx],
                            'stem': line.split(';;')[0],
                            'count': line.split(';;')[1]
                        })
        if(len(fwords)):
            queryresponse.append({
                'filename':sfile,
                'words':fwords
            })


    
    dflsit=list()
    for word in wordlist:
        filelistdf = set()
        for dfword in dfwordlist:
            if word == dfword['word']:
                filelistdf.add(dfword['file'])
        dflsit.append({
            'word':word,
            'files':list(filelistdf)
        })

    
    return {'response':queryresponse,'doccount':len(files),'dfwordlist':dflsit} 