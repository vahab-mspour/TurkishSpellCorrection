#coding:utf8
directory= "C:/Users/siege/Downloads/_data/BounWebCorpusHasimSak/BounWebCorpusHasimSak/newscor.xml"

with open(directory, 'r')as corpus:
    for line in corpus:
        list =decode(str(line))
        print(line)