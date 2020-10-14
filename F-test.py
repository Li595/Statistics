import numpy

class readtestF:
    # This class reads a file. Must get only one name.txt to be readen correctly, next argument takes a number of degrees of freedom(Default k = 1)
    
    def __init__(self, name = None, freedom = 1):
        self.name = name
        self.file = open(self.name)
        self.readen = self.file.readlines()
        self.freedom = freedom
        for i in range(len(self.readen)):
            self.readen[i] = self.readen[i].rstrip()
            self.readen[i] = self.readen[i].split(',')
            self.readen[i] = '.'.join(self.readen[i])
            self.readen[i] = float(self.readen[i])
    # Calculates a dispersion
    def Dispersion(self):
        return numpy.var(self.readen, ddof = self.freedom)

class Ftest:
    # Takes a list of two elements, whitch which are the sample variances.
    def __init__(self, dispersions = None):
        self.dispersions = dispersions
    #Returns 
    def ReturnF(self):
        if self.dispersions[0] > self.dispersions[1]:
            return self.dispersions[0]/self.dispersions[1]
        else:
            return self.dispersions[1]/self.dispersions[0]

file1 = readtestF('111.txt').Dispersion()
file2 = readtestF('222.txt').Dispersion() 
print(file1)
print(file2)
D = [file1, file2]

result = Ftest(D)
print(result.ReturnF())





