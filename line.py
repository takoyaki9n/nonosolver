#! C:/Python32/python.exe
# coding: UTF-8

class Line():
    def __init__(self,key,length,number=None):
        self.complete=False
        self.key=key
        self.length=length
        self.number=number
        self.prospects=[]
    
    def GetScore(self):
        score=0
        if sum(self.key)==0:
            score=self.length
        elif sum(self.key)+len(self.key)-1==self.length:
            score=self.length
        else:
            s=sum(self.key)
            for value in self.key:
                score+=value+s-self.length+len(self.key)-1
        return score#*1.0/self.length
    
    def SetProspects(self,sequence):
        prospect=[]
        self.SearchProspects(self.key, sequence, prospect)
        self.Complete()
        
    def SearchProspects(self,key,sequence,prospect):#再帰的に候補となる配置を検索
        if sum(key)==0:
            self.prospects.append([-1]*len(sequence))
        else:
            if len(key) != 1:
                start = sum(key[1:]) + len(key[1:]) - 1
                end = len(sequence) - key[0] - 1
                for i in range(end, start - 1, -1):
                    append = [-1] * (end - i) + [1] * key[0] + [-1]
                    if self.IsConsistent(append, sequence):
                        self.SearchProspects(key[1:], sequence[len(append):], prospect + append)
            elif len(key) == 1:
                for i in range(len(sequence) - key[0] + 1):
                    append = [-1] * i + [1] * key[0] + [-1] * (len(sequence) - i - key[0])
                    if self.IsConsistent(append, sequence):
                        self.prospects.append(prospect + append)
    
    def Refine(self,sequence):
        rem=[]
        for prospect in self.prospects:
            if not self.IsConsistent(prospect, sequence):
                rem.append(prospect)
        for prospect in rem:
            self.prospects.remove(prospect)
        return self.Complete()                
        
    def IsConsistent(self,prospect,sequence):#確定した配置と候補配置が矛盾しないか確認
        for i in range(len(prospect)):
            if prospect[i]*sequence[i]==-1:
                return False
        return True
    
    def Complete(self):#候補配置がなくなったらFalseそれ以外はTrueを返す
        if len(self.prospects)==1:
            self.complete=True
        elif len(self.prospects)==0:
            return False
        return True
    
    def GetSequence(self):
        sequence=[]
        if len(self.prospects)==0:
            return sequence
        else:
            for i in range(self.length):
                fill=True
                blank=True
                for j in range(len(self.prospects)):
                    if self.prospects[j][i]==-1:
                        fill=False
                    elif self.prospects[j][i]==1:
                        blank=False
                if fill and not blank:
                    sequence.append(1)
                elif not fill and blank:
                    sequence.append(-1)
                elif not(fill and blank):
                    sequence.append(0)
                else:
                    print("error")
            return sequence
                