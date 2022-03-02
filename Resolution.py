from copy import deepcopy
class Resolution:
    def __init__(self):
        self.alpha=[]
        self.KB=[]
    def readFile(self, filename):
        f=open(filename,'r')
        str=f.readline()
        str=str[:len(str)-1].split(' OR ')
        self.alpha.append(str)
        num= int(f.readline())
        for i in range(num):
            str=f.readline()
            str=str[:len(str)-1].split(' OR ')
            self.KB.append(str)
        self.alpha = self.cnfSentence(self.alpha)
        self.KB    = self.cnfSentence(self.KB)


    def cnfSentence(self, sentences):
        listSentence=[]
        for s in sentences:
            newS = sorted(list(set(deepcopy(s))), key=lambda x: x[-1])
            if self.checkSentence(newS) and newS not in listSentence:
                listSentence.append(newS)
        return listSentence
    def checkLiterals(self,l1, l2):
        if(l1[0] != l2[0] and l1[-1] == l2[-1]):
            return True
        return False

    def checkSentence(self, sentence):
        for i in range(len(sentence) - 1):
            if self.checkLiterals(sentence[i], sentence[i+1]):
                return False
        return True
    def negationSentence(self, sentence):
        negationS=[]
        for s in sentence:
            for literal in s:
                newLiteral=[self.negationLiteral(literal)]
                negationS.append(newLiteral)
        return negationS
    def negationLiteral(self, literal):
        if literal[0] == '-':
            return literal[1]
        return '-' + literal
        
    def solve2Sentence(self, s1, s2):
        newSentences= []
        for i in range(len(s1)):
            for j in range(len(s2)):
                if self.checkLiterals(s1[i], s2[j]):
                    newS = s1[:i] + s1[i + 1:] + s2[:j] + s2[j + 1:]
                    k = sorted(list(set(deepcopy(newS))), key=lambda x: x[-1])
                    newSentences.append(k)
        return newSentences
    def resolution(self, filename):
        f = open(filename, 'w')
        listSentence = deepcopy(self.KB)
        negOfAlpha = self.cnfSentence(self.negationSentence(self.alpha))
        for sentence in negOfAlpha:
            if sentence not in listSentence:
                listSentence.append(sentence)
        while True:
            newSentence=[]
            for i in range(len(listSentence)):
                for j in range(i + 1, len(listSentence)):
                    newS = self.solve2Sentence(listSentence[i], listSentence[j])
                    if [] in newS:
                        newSentence.append([])
                        print('len: ', str(len(newSentence)))  
                        f.write(str(len(newSentence)) + '\n')  
                        for i in range(len(newSentence)):
                            listSentence.append(newSentence[i])
                            print(self.sentenceToString(newSentence[i]))
                            f.write(self.sentenceToString(newSentence[i]) + '\n')
                        f.write('YES\n')
                        f.close()
                        return True

                    for s in newS:
                        if not self.checkSentence(s):
                            break
                        if s not in listSentence and s not in newSentence:
                            newSentence.append(s)
            print('len: ', str(len(newSentence)))  
            f.write(str(len(newSentence)) + '\n')  
            if len(newSentence) == 0:
                f.write('NO\n')
                f.close()
                return False
            for i in range(len(newSentence)):
                listSentence.append(newSentence[i])
                print(self.sentenceToString(newSentence[i]))
                f.write(self.sentenceToString(newSentence[i]) + '\n')
    def sentenceToString(self, sentence):
        if len(sentence) == 0:
            return '{}'
        string = ''
        for i in range(len(sentence) - 1):
            string =string+ str(sentence[i]) + ' OR '
        string =string+ str(sentence[len(sentence) - 1])

        return string



        