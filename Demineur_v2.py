import tkinter as tk
import random

class Application(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        mapTabelFilledMines = self.buildMines()
        mapTabelFilledAll = self.buildValues(mapTabelFilledMines)
        self.buildInterface(mapTabelFilledAll)

    def buildMines(self): # Build the matrix with mines as 9 and empty as 0
        mapTabel = [[0 for _ in range(10)] for _ in range(10)]
        for _ in range(20):
            grenadeCurrent = random.randint(0,99)
            ligneCurrent = grenadeCurrent // 10
            colonneCurrent = grenadeCurrent % 10

            if mapTabel[ligneCurrent][colonneCurrent] != 9:
                mapTabel[ligneCurrent][colonneCurrent] = 9
        return mapTabel

    def buildValues(self,mapTabel): # Scan the matrix with mines and affect the correct number on every case
        for i in range(10):
            for j in range(10):
                valeurCase = 0

                if mapTabel[i][j] == 9: # If mine, we don't change anything
                    continue
                """
                Here is a big change from v1.
                on v1: We place a mine and then we increment all neighbour
                on v2: mines are placed from buildMines(). buildValue() calculate the value for each case by scanning his neighbour
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

                mapTabel[i][j] = valeurCase
        return mapTabel
    
    def buildInterface(self,mapTabelFilledAll): # Build the graphic interface
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
                self.case[i][j] = tk.Button(self, width=3, height=2, command=lambda i=i, j=j: self.discoverCase(mapTabelFilledAll,i,j))
                self.case[i][j].grid(row=i,column=j) 

    def discoverCase(self,mapTabelFilledAll,i,j): # Discover the clicked case
        if mapTabelFilledAll[i][j] == 9:
            print("perdu")
            self.fillMap(mapTabelFilledAll)
        elif mapTabelFilledAll[i][j] == 0:
            print("OK")
        else:
            print("warning")
        self.case[i][j].configure(text=mapTabelFilledAll[i][j])
    
    def fillMap(self,mapTabelFilledAll): # If loose, the map is entirely discovered
        for i in range(10):
            for j in range(10):
                self.case[i][j].configure(text=mapTabelFilledAll[i][j])

# Having some configuration of the window
root = tk.Tk()
root.title("DEMINEUR")
root.geometry("400x400+520+200")
demineurInterface = Application(root)
demineurInterface.mainloop()