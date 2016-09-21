import re
import os
import csv
import glob


class MyCorpus(object):
     def __iter__(self):
         for line in open('mycorpus.txt'):
             # assume there's one document per line, tokens separated by whitespace
             yield dictionary.doc2bow(line.lower().split())

    

def makeCorpusFile(inDir : str,  outFileName : str) -> None:

    print("\n writing corpusfile ... \n")

    mastercorpus = os.path.join(os.getcwd(), outFileName)
    
    with open(mastercorpus, 'w', encoding = "utf-8") as data:
        inPath = os.path.join(os.getcwd(), inDir)
        folder = glob.glob(os.path.join(inPath, "*.txt"))
        for i, text in enumerate(folder):
            with open(text, 'r', encoding = "utf-8") as content:
                textline = [re.sub(r'\\n\\r', '', document) for document in ' '.join(content.read().split())]
                if i != len(folder) - 1:
                    data.write(os.path.splitext(os.path.basename(text))[0] + "\n" + "".join(textline) + "\n")
                else:
                    data.write(os.path.splitext(os.path.basename(text))[0] + "\n" + "".join(textline))

    print("\n corpusfile written successfully \n")

def readFromCorpusFile(corpusfile : str, outfolder : str) -> None:
    
    print("\n reading from corpus file ... \n")
    
    mastercorpus = os.path.join(os.getcwd(), corpusfile)
    outfolderpath = os.path.join(os.getcwd(), outfolder)
    
    
    if not os.path.exists(outfolderpath):
        print("\n creating output folder ... \n")
        os.makedirs(outfolder)
    
    for i, content in enumerate(open(mastercorpus, 'r', encoding = "utf-8")):
        if i%2 == 0:
            contentPath = os.path.join(outfolderpath, content[:-1] + ".txt")
            print("\n writing", os.path.basename(contentPath) ,"from corpusfile to ", outfolder, "\n")
        else:
            with open(contentPath, 'w', encoding = "utf-8") as file:
                file.write(content)
    
    print("\n reading successfull \n")
    print("\n files from corpus written successfully \n")
	
	
	
'''


Uncomment to use


'''

	
#makeCorpusFile("swcorp_off", "smallcorpusfile.txt")
#readFromCorpusFile("smallcorpusfile.txt", "tesoutfolder")