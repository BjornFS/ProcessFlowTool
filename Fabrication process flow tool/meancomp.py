import tkinter as tk
from statistics import median, mode, stdev

class Calculator(tk.Frame):
    """Calculate mean median mode and standard deviation"""
    def __init__(self, parent, *args, **kwargs):
        #setup tkinter frame
        tk.Frame.__init__(self, parent, *args, **kwargs)
        parent = parent

        self.makeWidgets()

    def makeWidgets(self):
        """make and pack various widgets"""
        self.meanLabel = tk.Label(self, text="")
        self.medianLabel = tk.Label(self, text="")
        self.modeLabel = tk.Label(self, text="")
        self.sdLabel = tk.Label(self, text="")
        self.entry = tk.Entry(self)
        self.calcuateButton = tk.Button(self, text="Calculate!", command = self.calculate)
        self.meanLabel.pack()
        self.medianLabel.pack()
        self.modeLabel.pack()
        self.sdLabel.pack()
        self.entry.pack()
        self.calcuateButton.pack()

    def calculate(self):
        self.listOfNumbers = self.entry.get()
        #get what is inputed into the entry widget
        self.listOfNumbers = self.listOfNumbers.split(' ')
        #split the input string by spaces
        for ind, i in enumerate(self.listOfNumbers):
            #convert each item in the list of strings of numbers to ints
            self.listOfNumbers[ind] = int(i)
        #calculate!
        self.calcMean()
        self.calcMedian()
        self.calcMode()
        self.calcSd()

    def calcMean(self):
        """calculate the mean"""
        mean = sum(self.listOfNumbers)/len(self.listOfNumbers)
        self.meanLabel.config(text='mean = ' + str(mean))
        return mean

    def calcMedian(self):
        """calculate the median"""
        med = median(self.listOfNumbers)
        self.medianLabel.config(text='median = ' + str(med))
        return med

    def calcMode(self):
        """calculate the mode"""

        Mode = max(set(self.listOfNumbers), key=self.listOfNumbers.count)
        self.modeLabel.config(text='mode = ' + str(Mode))
        return Mode

    def calcSd(self):
        """calculate the standard deviation"""
        sd = stdev(self.listOfNumbers)
        self.sdLabel.config(text='Standard deviation = ' + str(sd))
        return sd

if __name__ == '__main__':
    root = tk.Tk()
    root.title('calculate mean, median, mode and standard deviation')
    root.geometry('400x200')
    Calculator(root).pack(side="top", fill="both", expand=True)
    root.mainloop() 