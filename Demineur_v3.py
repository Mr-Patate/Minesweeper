import tkinter as tk
import random

class Application(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.counterCase = 100 # counterCase is decreasing with: mine placing or case discovering. At 0, an if statement allow victory
        mapTabelFilledMines = self.buildMines()
        self.buildInterface(mapTabelFilledMines)

    def buildMines(self): # Build the matrix with mines as 9 and empty as 0
        mapTabel = [[0 for _ in range(10)] for _ in range(10)]
        for _ in range(1):
            grenadeCurrent = random.randint(0,99)
            ligneCurrent = grenadeCurrent // 10
            colonneCurrent = grenadeCurrent % 10

            if mapTabel[ligneCurrent][colonneCurrent] != 9:
                mapTabel[ligneCurrent][colonneCurrent] = 9
                print("te")
                self.counterCase -= 1
        print(mapTabel)
        return mapTabel

    def buildValues(self,mapTabel,i,j):
        valeurCase = 0
        """
        Here is a big change from v1 and v2.
        on v1: We place a mine and then we increment all neighbour
        on v2: mines are placed from buildMines(). buildValue() calculate the value for each case by scanning his neighbour
        on v3: only clicked case is calculated. This inproves the programm efficiency: only what we need to see is calculated
        We have also less stored data
        """
        for t in range(-1,2):
            for l in range(-1,2):
                if t == 0 & l == 0:
                    pass
                elif (i+t) < 0:
                    continue 
                elif (j+l) < 0:
                    continue
                else:
                    pass
                try:
                    if mapTabel[i+t][j+l] == 9:
                        valeurCase += 1
                except IndexError:
                    pass

        return valeurCase
    
    def buildInterface(self,mapTabelFilledMines): # Build the graphic interface
        self.case = [[0 for _ in range(10)] for _ in range(10)]
        """
        Here is a big change from v1.
        v1 has an array of dimension 1. It was a complete mess to find neighbour
        v2 has now an array of dimension 2. It makes it easier to find neighbour with loops
        """
        for i in range(10):
            for j in range(10):
                # i=i, j=j helps to remember the position of each Button. It is really important for discoverCase().
                # I need this to know which case to discover.
                self.case[i][j] = tk.Button(self, width=3, height=2, command=lambda i=i, j=j: self.discoverCase(mapTabelFilledMines,i,j))
                self.case[i][j].grid(row=i,column=j)

    def discoverCase(self,mapTabelFilledMines, i,j): # Discover the clicked case
        self.counterCase -= 1
        print(self.counterCase)
        if mapTabelFilledMines[i][j] == 9:
            print("perdu")
            self.fillMap(mapTabelFilledMines)
        else:
            self.case[i][j].configure(text=self.buildValues(mapTabelFilledMines,i,j))
        if self.counterCase == 0:
            print("gagné")

    def fillMap(self,mapTabelFilledMines): # If loose, the map is entirely discovered
        for i in range(10):
            for j in range(10):
                if mapTabelFilledMines[i][j] == 9:
                    continue
                else:
                    self.case[i][j].configure(text=self.buildValues(mapTabelFilledMines,i,j))

# Having some configuration of the window
root = tk.Tk()
root.title("DEMINEUR")
root.geometry("400x400+520+200")
demineurInterface = Application(root)
demineurInterface.mainloop()