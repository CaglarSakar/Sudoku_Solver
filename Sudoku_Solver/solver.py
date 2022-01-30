class Game():
    def __init__(self, *args, **kwargs):
        if "table" not in kwargs.keys():
            raise NameError("There is no table")
        if len(kwargs["table"]) != 9:
            raise TypeError("Table is not 9x9")
        for line in kwargs["table"]:
            if len(line) != 9:
                raise TypeError("Table is not 9x9")
        
        self.table= kwargs["table"]
        self.ihtimal_table = self.__create9x9List()
        self.change_indexes = []

    def show(self,**kwargs):
        if "table" in kwargs.keys():
            table = kwargs["table"]
        else:
            table =self.table
        for j,line in enumerate(table):
            if j != 0 and j%3==0:
                    print()
            for i,num in enumerate(line):
                if i != 0 and i%3==0:
                    print(" ",end="")
                if num == 0:
                    num = " "
                print(num,end="")
            print()
    
    def taketable(self):
        return self.table
    
    def __checkLine(self,i,j):
        ihtimal = [1,2,3,4,5,6,7,8,9]
        for k,num in enumerate(self.table[i]):
            if k == j or num == 0:
                continue
            else:
                ihtimal.remove(num)
        
        return ihtimal
    
    def __checkColumn(self,i,j):
        ihtimal = [1,2,3,4,5,6,7,8,9]
        for k,line in enumerate(self.table):
            if line[j] == 0:
                continue
            else:
                
                ihtimal.remove(line[j])
        
        return ihtimal

    def __checkGrid(self,i,j):
        ihtimal = [1,2,3,4,5,6,7,8,9]
        grid_i = i//3
        grid_j = j//3
        for k,line in enumerate(self.table):
            if grid_i != k//3:
                continue
            else:
                for l,num in enumerate(line):
                    if grid_j != l//3:
                        continue
                    else:
                        if (i == k and j == l) or num == 0:
                            continue
                        else:
                            ihtimal.remove(num)
        
        return ihtimal

    def __checkNum(self,i,j):
        lis1 = self.__checkLine(i,j)
        lis2 = self.__checkColumn(i,j)
        lis3 = self.__checkGrid(i,j)

        intersection = self.__intersection(lis1,lis2)
        intersection = self.__intersection(intersection,lis3)
        self.ihtimal_table[i][j] = intersection

    def __intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3
    
    def __create9x9List(self):
        line = []
        table = []
        for i in range(9):
            line.append([])
        for j in range(9):
            table.append(line.copy())
        return table
    
    def __changeCurrent(self,i,j):
        if self.table[i][j] == 0:
            self.__checkNum(i,j)
            if len(self.ihtimal_table[i][j]) != 0:
                self.change_indexes.append([i,j])
                self.table[i][j] = self.ihtimal_table[i][j][-1]
                return 1
            else:
                self.__changePrevious()
                return -1
        else:
            return 0
    
    def __changePrevious(self):
        i = self.change_indexes[-1][0]
        j = self.change_indexes[-1][1]
        self.ihtimal_table[i][j].pop()
        if len(self.ihtimal_table[i][j]) != 0:
            self.table[i][j] = self.ihtimal_table[i][j][-1]
        else:
            self.table[i][j] = 0
            self.change_indexes.pop()
            self.__changePrevious()


    
    def solve(self):
        while True:
            break_all = False
            for i,line in enumerate(self.table):
                for j,current_num in enumerate(line):
                    ret = self.__changeCurrent(i,j)
                    if ret == -1:
                        break_all = True
                    else:
                        continue
                    if break_all == True:
                        break
                if break_all == True:
                    break
            if i == 8 and j == 8:
                break


if __name__ == "__main__":

    ornek =  [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

    mosth =  [[8,0,0,0,0,0,0,0,0],
            [0,0,3,6,0,0,0,0,0],
            [0,7,0,0,9,0,2,0,0],
            [0,5,0,0,0,7,0,0,0],
            [0,0,0,0,4,5,7,0,0],
            [0,0,0,1,0,0,0,3,0],
            [0,0,1,0,0,0,0,6,8],
            [0,0,8,5,0,0,0,1,0],
            [0,9,0,0,0,0,4,0,0]]


    table1 = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]

    table2 = [[6,0,3,0,0,0,1,0,0],
            [0,0,9,0,0,0,2,0,0],
            [0,0,7,4,0,9,0,0,0],
            [0,0,0,0,1,0,0,0,7],
            [4,0,0,0,6,0,0,0,0],
            [0,0,0,0,7,0,0,5,3],
            [0,1,0,0,0,0,0,4,0],
            [0,0,6,3,0,7,0,9,0],
            [0,9,0,0,0,2,0,3,0]]


    game = Game(table=table2)

    game.show()
    print("---------------")
    game.solve()

    game.show()