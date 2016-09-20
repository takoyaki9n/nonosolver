#! C:/Python32/python.exe
# coding: UTF-8

from line import *
import operator
import copy

sma=[[[7],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[7],[1,3,1],[1,1],[1,5,1]],
    [[8,1,1],[1,1],[1,1,1],[1,4],[1,2,1],[1,4],[1,1,1],[1,1],[8,1,1]]]
nes=[[[7],[1,6],[1,6],[1,6],[1,4],[1,2],[1,1],[1,2,1]],
    [[7],[1],[4,1],[4,1],[5],[5,1],[6],[7]]]
soc=[[[3],[5],[3,1],[2,1],[3,3,4],[2,2,7],[6,1,1],[4,2,2],[1,1],[3,1],[6],[2,7],[6,3,1],[1,2,2,1,1],[4,1,1,3],[4,2,2],[3,3,1],[3,3],[3],[2,1]]
     ,[[2],[1,2],[2,3],[2,3],[3,1,1],[2,1,1],[1,1,1,2,2],[1,1,3,1,3],[2,6,4],[3,3,9,1],[5,3,2],[3,1,2,2],[2,1,7],[3,3,2],[2,4],[2,1,2],[2,2,1],[2,2],[1],[1]]]
kam=[[[6],[6],[1,1],[10,5],[1,2,8],[1,1,5,3],[1,1,1,4,1,2],[1,1,4,4,1],[1,1,2,7],[4,12],[1,9,1],[3,9,1],[2,6,2],[5,7],[2],[1,8],[1,3,4],[1,2],[1,1],[7]]
     ,[[1,5],[2,2],[4,1,1],[2,1,2,1],[2,1,1],[2,1,2,1],[2,1,2],[5,1,1,2],[7,3,1],[1,5,2,1],[2,3,1,1,1],[3,4,1,1],[3,5,2,1],[3,6,1,1,1],[2,7,1,1,1],[3,7,1,2],[2,8,2],[3,5,1,2],[4,2,2,2],[5,4,2]]]

class Sheet():

    def __init__(self,parent=None):
        self.width=0
        self.height=0
        self.matrix=[]
        self.lines=[]
        self.answers=[]
        self.progress=0

    def Solve(self,rowkeys,colkeys):
        if self.SetSheet(rowkeys, colkeys):
            sheet=self.Clone()
            self.Search(sheet,100.0)
            if len(self.answers)==0:
                print("解がありませんでした。")
            else:
                print(str(len(self.answers))+"個の解が見つかりました。")
                for answer in self.answers:
                    print(self.ToString(answer) + "\n")

    def SetSheet(self,rowkeys,colkeys):
        if self.KeyCheck(rowkeys, colkeys):
            self.width=len(colkeys)
            self.height=len(rowkeys)
            self.matrix=self.InitMatrix()
            self.SetLines(rowkeys,colkeys)
            return True
        else:
            self.error.emit("初期化に失敗しました。")
            return False

    def KeyCheck(self,rowkeys,colkeys):
        consistent=True
        rowsum=0
        for i in range(len(rowkeys)):
            keysum=0
            for j in range(len(rowkeys[i])):
                if rowkeys[i][j]<0:
                    consistent=False
                    self.error.emit(str(i)+"行の"+str(j)+"番目の鍵の値が負です。")
                keysum+=rowkeys[i][j]
            rowsum+=keysum
            if keysum+len(rowkeys[i])-1>len(colkeys):
                consistent=False
                self.error.emit(str(i)+"行の鍵の合計値が大きすぎます。")
        colsum=0
        for i in range(len(colkeys)):
            keysum=0
            for j in range(len(colkeys[i])):
                if colkeys[i][j]<0:
                    consistent=False
                    self.error.emit(str(i)+"列の"+str(j)+"番目の鍵の値が負です。")
                keysum+=colkeys[i][j]
            colsum+=keysum
            if keysum+len(colkeys[i])-1>len(rowkeys):
                consistent=False
                self.error.emit(str(i)+"列の鍵の合計値が大きすぎます。")
        if rowsum!=colsum:
            consistent=False
            self.error.emit("縦と横の鍵の総合計値が違います")
        return consistent

    def InitMatrix(self):
        matrix=[]
        for i in range(self.height):
            matrix.append([0]*self.width)
        return matrix

    def SetLines(self,rowkeys,colkeys):#行の番号はそのまま、列の番号は列番号+高さで全体を通し番号で管理
        for i in range(self.height):
            self.lines.append(Line(rowkeys[i],self.width,i))
        for i in range(self.width):
            self.lines.append(Line(colkeys[i],self.height,self.height+i))
        for line in self.lines:
            sequence=self.Sequence(line.number)
            line.SetProspects(sequence)
            self.UpdateLine(line.number,line.GetSequence())

    def Sieving(self):
        matrix=self.InitMatrix()
        while self.Updated(matrix):
            matrix=copy.deepcopy(self.matrix)
            for line in self.lines:
                if not line.complete:
                    sequence=self.Sequence(line.number)
                    if line.Refine(sequence):
                        self.UpdateLine(line.number,line.GetSequence())
#                        print(self.ToString(self.matrix)+"\n")
                    else:
                        return False
        return True

    def Search(self,sheet,value):
        if sheet.Sieving():
            line=sheet.InCompleteLine()
            if line:
                oldsheet=sheet.Clone()
                for prospect in line.prospects:
                    sheet.UpdateLine(line.number,prospect)
                    line.complete=True
                    self.Search(sheet,value/len(line.prospects))
                    sheet=oldsheet.Clone()
            else:
                self.progress+=value
                self.answers.append(sheet.matrix)
        else:
            self.progress+=value
            print(self.progress)


    def InCompleteLine(self):
        for line in self.lines:
            if not line.complete:
                return line
        return None

    def Sequence(self,number):
        if number<self.height:
            return self.matrix[number]
        else:
            return list(map(operator.itemgetter(number-self.height),self.matrix))

    def Updated(self,matrix):
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j]!=matrix[i][j]:
                    return True
        return False

    def UpdateLine(self,number,sequence):
        if number<self.height:
            self.matrix[number]=sequence
        else:
            for i in range(self.height):
                self.matrix[i][number-self.height]=sequence[i]

    def GetKeys(self,i,j):
        keys=[]
        for n in range(i,j+1):
            keys.append(self.lines[n].key)
        return tuple(keys)

    def ToString(self,matrix):
        string=""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num=matrix[i][j]
                if num==1:
                    string+="■"
                elif num==-1:
                    string+="×"
                elif num==0:
                    string+=" "
            string+="\n"
        string=string[:len(string)-1]
        return string

    def Clone(self):
        sheet=Sheet()
        sheet.width=self.width
        sheet.height=self.height
        sheet.matrix=copy.deepcopy(self.matrix)
        sheet.lines=copy.deepcopy(self.lines)
        sheet.answers=copy.deepcopy(self.answers)
        sheet.progress=self.progress
        return sheet

if __name__ =="__main__":
    s=Sheet()
    keys = soc
    s.Solve(keys[0], keys[1])
