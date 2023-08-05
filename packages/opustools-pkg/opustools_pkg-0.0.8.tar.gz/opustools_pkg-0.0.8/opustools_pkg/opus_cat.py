import argparse
import xml.parsers.expat
import zipfile

class SentenceParser:
    
    def __init__(self, document, args):
        self.document = document
        self.args = args

        self.start = ""
        self.sid = ""
        self.chara = ""
        self.end = ""
        
        self.stopit = False

        self.parser = xml.parsers.expat.ParserCreate()
        self.parser.StartElementHandler = self.start_element
        self.parser.CharacterDataHandler = self.char_data
        self.parser.EndElementHandler = self.end_element
        
        self.sfound = False
        self.efound = False

    def start_element(self, name, attrs):
        self.start = name
        if "id" in attrs.keys() and name == "s":
            self.sfound = True
            self.sid = attrs["id"]

    def char_data(self, data):
        if self.sfound:
            self.chara += data

    def end_element(self, name):
        self.end = name
        if name == "s":
            self.efound = True
        if name == "text":
            self.stopit = True

    def parseLine(self, line):
        self.parser.Parse(line.strip())

    def processTokenizedSentence(self, sentence):
        newSentence, stop = sentence, 0
        if self.efound:
            self.sfound = False
            self.efound = False
            stop = -1
            if newSentence == "":
                newSentence = self.chara
                self.chara = ""
        if self.sfound:
            if self.start == "w" and self.end == "w":
                newSentence = sentence + " " + self.chara
                self.chara = ""
        return newSentence, stop

    def readSentence(self):
        sentence = ""
        while True:
            line = self.document.readline()
            self.parseLine(line)
            newSentence, stop = self.processTokenizedSentence(sentence)
            sentence = newSentence
            if stop == -1 or self.stopit:
                break

        sentence = sentence.strip()

        if sentence == "":
            return ""

        if self.args.i:
            return sentence
        else:
            return '("' + self.sid + '")>' + sentence

class OpusCat:

    def __init__(self, arguments):
        parser = argparse.ArgumentParser(prog="opus_cat", description="Read a document from OPUS and print to STDOUT")

        parser.add_argument("-d", help="Corpus name", required=True)
        parser.add_argument("-l", help="Language", required=True)
        parser.add_argument("-i", help="Print without ids when using -p", action="store_true")
        parser.add_argument("-m", help="Maximum number of sentences", default="all")
        parser.add_argument("-p", help="Print in plain txt", action="store_true")

        if len(arguments) == 0:
            self.args = parser.parse_args()
        else:
            self.args = parser.parse_args(arguments)

        self.lzip = zipfile.ZipFile("/proj/nlpl/data/OPUS/" + self.args.d + "/latest/xml/" + self.args.l + ".zip" , "r")

        if self.args.m == "all":
            self.maximum = -2
        else:
            self.maximum = int(self.args.m)

    def printSentences(self):
        xml_break = False
        for n in self.lzip.namelist():
            if n[-4:] == ".xml":
                with self.lzip.open(n, "r") as f:
                    if self.args.p:
                        spar = SentenceParser(f, self.args)
                        print("\n# "+n+"\n")
                        while True:
                            sent = spar.readSentence()
                            if sent != "":
                                print(sent)
                                self.maximum -= 1
                            if spar.stopit or self.maximum == 0:
                                break
                        spar.document.close()
                    else:
                        for line in f:
                            line = line.decode("utf-8")
                            if "<s id=" in line or "<s hun=" in line:
                                self.maximum -= 1
                                if self.maximum == -1:
                                    xml_break = True
                                    break
                            print(line, end="")                            
                                
                if xml_break:
                    break
                                
            if self.maximum == 0:
                break


