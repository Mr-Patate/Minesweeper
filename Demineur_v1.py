import tkinter as tk
import random
from tkinter import messagebox

# Next time I really need to stop with self. It is really not a good way to programming.
# I did it right for counter and tabel at least.

class Application(tk.Frame):
    
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.buildInterface()
        self.mapp = self.buildMap()
        #self.fillMap() # FOR RUNNING APPLICATION WITH ALL BUTTON DISCOVERED

    def buildInterface(self): # Build the graphic interface
        self.case = []
        counter = 0
        for i in range(10):
            for j in range(10):
                # counter=counter helps to remember the position of each Button. It is really important for discoverCase(counter).
                # I need this to know which case to discover.
                self.case.append(tk.Button(self, width=3, height=2,state="normal", command=lambda counter=counter: self.discoverCase(counter)))
                self.case[counter].grid(row=i,column=j)
                counter += 1
    
    def fillMap(self): # Fill the map with mines mapping (takes numbers from tabel)
        for i in range(len(self.case)):
            if self.mapp[i] >= 9:
                self.case[i].configure(fg="red")
            self.case[i].configure(text=self.mapp[i])
        
    def buildMap(self): # Return tabel with mines mapping
        tabel = [0 for l in range(100)]
        for _ in range(40): # Takes maximal 20 mines. Sometimes 2 mines have the same position (that is why "maximal")
            grenadeCurrent = random.randint(0,99)

            if tabel[grenadeCurrent] == 9:
                break
            elif grenadeCurrent == 0: # If mine on left top corner
                tabel[0] = 9
                tabel[1] += 1
                tabel[10] += 1
                tabel[11] += 1
            elif grenadeCurrent == 9: # If mine on right top corner
                tabel[9] = 9
                tabel[8] += 1
                tabel[18] += 1
                tabel[19] += 1
            elif grenadeCurrent == 90: # If mine on left bottom corner
                tabel[90] = 9
                tabel[80] += 1
                tabel[81] += 1
                tabel[91] += 1
            elif grenadeCurrent == 99: # If mine of right bottom corner
                tabel[99] = 9
                tabel[88] += 1
                tabel[89] += 1
                tabel[98] += 1
            elif grenadeCurrent//10 == 0: # If mine on first row
                tabel[grenadeCurrent] = 9
                tabel[grenadeCurrent-1] += 1
                tabel[grenadeCurrent+9] += 1
                tabel[grenadeCurrent+10] += 1
                tabel[grenadeCurrent+11] += 1
                tabel[grenadeCurrent+1] += 1
            elif grenadeCurrent//10 == 9: # If mine on last row
                tabel[grenadeCurrent] = 9
                tabel[grenadeCurrent-1] += 1
                tabel[grenadeCurrent-11] += 1
                tabel[grenadeCurrent-10] += 1
                tabel[grenadeCurrent-9] += 1
                tabel[grenadeCurrent+1] += 1
            elif grenadeCurrent%10 == 0: # If mine on first column
                tabel[grenadeCurrent] = 9
                tabel[grenadeCurrent-10] += 1
                tabel[grenadeCurrent-9] += 1
                tabel[grenadeCurrent+1] += 1
                tabel[grenadeCurrent+11] += 1
                tabel[grenadeCurrent+10] += 1
            elif grenadeCurrent%10 == 9: # If mine on last column
                tabel[grenadeCurrent] = 9
                tabel[grenadeCurrent-10] += 1
                tabel[grenadeCurrent-11] += 1
                tabel[grenadeCurrent-1] += 1
                tabel[grenadeCurrent+9] += 1
                tabel[grenadeCurrent+10] += 1
            else: # If mine anywhere else
                tabel[grenadeCurrent] = 9
                tabel[grenadeCurrent-1] += 1
                tabel[grenadeCurrent-11] += 1
                tabel[grenadeCurrent-10] += 1
                tabel[grenadeCurrent-9] += 1
                tabel[grenadeCurrent+1] += 1
                tabel[grenadeCurrent+11] += 1
                tabel[grenadeCurrent+10] += 1
                tabel[grenadeCurrent+9] += 1

        return tabel

# For each click, the case will be discovered and get a color
    def discoverCase(self,counter):
        if self.mapp[counter] >= 9:
            print("PERDU")
            self.fillMap()
            tk.messagebox.showinfo("PERDU","essaie encore :)")
        elif self.mapp[counter] == 0:
            print("OK")
            self.case[counter].configure(fg="blue") # Unfortunately configure(bg="") doesn't work. configure(fg="") Works.
        else:
            print("warning")
            self.case[counter].configure(fg="orange")
        self.case[counter].configure(text=self.mapp[counter])
        print(counter)


# Having some configuration of the window
root = tk.Tk()
root.title("DEMINEUR")
root.geometry("400x400+520+200")
demineurInterface = Application(root)
demineurInterface.mainloop()