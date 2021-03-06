# -*- coding: utf-8 -*-
#Oscar A. Nilsson
#from pandas import DataFrame
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from heapq import nlargest
from heapq import nsmallest

class neka52:
    """Test class for NEKA52 """
    
    def __init__(self, filename, xls_or_xlsx, contry):
        
        self.contry = contry
        
        if xls_or_xlsx == 0:
            self.name = filename + '.xls'
        else:
            self.name = filename + '.xlsx'
        
    def extractrows(self, Sheeet, yearfrom, yearto):
        """
        This is for exctracting rows from an excel sheet, which is in this 
        cases in terms of years from 1970 to 2014.
        
        :param Sheet: name of the sheet that you want to extract the data from.
        :type Sheet: string
        :param yearfrom: The year to start extracting from, in this case at 
                         least 1970 but less than 2014 and yearto
        :type yearfrom: int gretaer than 1970 but less than 2014 and yearto
        :param yearto: The year to stop extracting from, in this case
        :type yearto: int less than 2014 but greater than 1970 and yearfrom.
        :returns: Array of the values
        """
        if yearfrom < 1970:
            return 'yearfrom needs to be bigger than or equal to 1970.'
        elif yearto > 2014:
            return 'yearto needs to be less than or equal to 2014.'
        elif yearfrom > yearto:
            return 'You need to have yearfrom to be bigger or equal to yearto'
        
        x = pd.read_excel(self.name, Sheeet)
        v = x.loc[:,:]
        y = np.array(v)
        outarray = y[yearfrom - 1970:yearto - 1970 + 1][:]
        
        
        return outarray
        
    
    def biggest(self, Sheeet ,year, n):
        """
        This method is for getting the n number of biggest values on one row
        and from one sheet and then return the number of 
        
        :param Sheeet: Name of the sheet in the excel file that you want to 
                       extract the data from.
        :type Sheeet: string 
        :param year: the year i.e. row that you want to extract the 
                         information from
        :type year: int
        :param n: For choosing the number of biggest values on values.
        :type n: int
        :returns: String of the returned contries
        """
        
        newlist = []
        
        #Getting the rowes from the sheet using the method for extracting rows
        x = self.extractrows(Sheeet, year, year)
        
        for i in range(35):
            newlist.append(x[0][i ])
        newlist[0] = nsmallest(1, newlist)
        
        y = sorted(nlargest(n, newlist))
        y.reverse()
        
        outarraynames = []
        p = self.names()
        palla = []
        
        for i in range(n):
            palla.append( int(newlist.index(y[i])))
            outarraynames.append(p[palla[i]])
            newlist[newlist.index(y[i])] = ' '
            
        return outarraynames
            
    
    def smallest(self, Sheeet ,year, n):
        """
        Method for getting the n smallest value in an row, or in this case for
        a year on a give sheet and returns the coutries in decending order
        
        :param Sheeet: Name of the sheet you want to extract the nth numbers of 
                       smallest values of.
        :type Sheeet: String
        :param: year: The year you want to extract the data from
        :type year: int
        :param n: The number of smallest values you want to get
        :type n: int
        :returns: sting of coutries with the smallest values set in order
        
        
        """
        
        newlist = []
        x = self.extractrows(Sheeet, year, year)
        for i in range(35):
            newlist.append(x[0][i])
        #newlist[0] = nlargest(1, newlist)
        
        y = sorted(nsmallest(n, newlist))
        y.reverse()
        
        outarraynames = []
        p = self.names()
        palla = []
        
        for i in range(n):
            palla.append( int(newlist.index(y[i])))
            outarraynames.append(p[palla[i]])
            newlist[newlist.index(y[i])] = ' '
        
        
        return outarraynames
    
    def compare(self, Sheeet, year1, year2):
        """
        Method for comparing two year between eachother.
        
        :param Sheeet: The sheet you want to extract data from
        :type Sheet: string
        :param year1: the first year you want to comapre with will see if that 
                      one is the biggest one
        :type year1: int
        :param year2: the second year you want to compare with
        :type year2: int
        :returns: return the contries and that have higer values in year1 
                  than year2
        """
        x1 = self.extractrows(Sheeet, year1, year1)
        x2 = self.extractrows(Sheeet, year2, year2)
        
        helplist = []
        p = self.names()
        
        outarray = []
        for i in range(35):
            if x1[0][i] > x2[0][i]:
                helplist.append(i)
        
        for i in range(len(helplist)):
            outarray.append(p[helplist[i]])
        return outarray
        
    def def_inflation(self, year, percentage):
        x1 = self.extractrows('KPI', year, year)
        x2 = self.extractrows('KPI', year - 1, year - 1)
        
        helplist1 = []
        helplist2 = []
        p = self.names()
        
        outarray1 = []
        outarray2 = []
        
        for i in range(35):
            if (x1[0][i] - x2[0][i])*100/x2[0][i] > percentage:
                helplist1.append(i)
                
            elif (x1[0][i] - x2[0][i])*100/x2[0][i] < 0:
                helplist2.append(i)
        
        
        x = 'Contries with an inflation higher than '+\
                        str(percentage) + ' percentage year ' + str(year)
        
        for i in range(len(helplist1)):
            outarray1.append(p[helplist1[i]])
        
        
        
        y = 'Contries with deflation year ' + str(year)
        
        for i in range(len(helplist2)):
            outarray2.append(p[helplist2[i]])
            
        return x, outarray1, y, outarray2 
        
        
    
        
    def AllData(self):
        outarray = []
        lists = [ 'Nominell_BNP', 'BNP_deflator', 'Befolkning',\
                 'Vaxelkurs_Faktisk','Vaxelkurs_ppp', 'Export', 'Import', 'KPI',\
                 'Arbetsloshet', 'Statsskuld']
        #print(self.contry)
        #print(self.name)
        
        for i in range(len(lists)):
            outarray.append(np.array(list( \
                            pd.read_excel(self.name, lists[i])[self.contry])))
            
        return outarray
    
    def names(self):
        x = np.array(list(pd.read_excel(self.name)))
        return x
    
    def nettoexport(self):
        Workingarray = self.AllData()
        Netto = (Workingarray[5] - Workingarray[6])/Workingarray[3]
        return Netto
    
    
    def plotnettoexport(self, yearfrom, yearto):
        y = self.nettoexport()/1000
        y = y[yearfrom - 1970: yearto - 1970 + 1]
        x = np.linspace(yearfrom, yearto, yearto - yearfrom + 1)
        plt.plot(x, y, label = self.contry)
        plt.xlabel('Year ' + str(yearfrom) + '-' + str(yearto))
        plt.ylabel('NettoExport (1000 Dollar)')
        plt.title(self.contry)
        plt.legend()
        plt.grid(True)
    
    def NominellVaxel(self, yearfrom, yearto):
        Workingarray = self.AllData()
        Vaxelkurs = Workingarray[3]
        Vaxelkurs = Vaxelkurs[yearfrom - 1970: yearto - 1970 + 1]
        x = np.linspace(yearfrom, yearto, yearto - yearfrom + 1)
        plt.plot(x, Vaxelkurs, label = self.contry)
        plt.xlabel('Year ' + str(yearfrom) + '-' + str(yearto))
        plt.ylabel(' Nominell vaxelkurs( Dollar)')
        plt.title(self.contry)
        plt.legend()
        plt.grid(True)
        
    def PPPVaxel(self, yearfrom, yearto):
        Workingarray = self.AllData()
        Vaxelkurs = Workingarray[4]
        Vaxelkurs = Vaxelkurs[yearfrom - 1970: yearto - 1970 + 1]
        x = np.linspace(yearfrom, yearto, yearto - yearfrom + 1)
        plt.plot(x, Vaxelkurs, label = self.contry)
        plt.xlabel('Year ' + str(yearfrom) + '-' + str(yearto))
        plt.ylabel(' Nominell vaxelkurs( Dollar)')
        plt.title(self.contry)
        plt.legend()
        plt.grid(True)

Sweden = neka52('neka521', 0, 'Sweden')
France = neka52('neka521', 0, 'France')
#%%

#Exercise 1. Plotting the nettoexport for Germany and Sweden against time.
Sweden.plotnettoexport(1970, 2014)
France.plotnettoexport(1970, 2014)

#%%
#Exercise 2. Plotting 
Sweden.NominellVaxel(1970, 2014)
France.NominellVaxel(1970, 2014)

#%%
Sweden.PPPVaxel(1970, 2014)
France.PPPVaxel(1970, 2014)


#%%
Sweden.def_inflation(2014, 5)
France.def_inflation(2014, 5)

#%%

Sweden.biggest('Arbetsloshet', 2014, 3)

#%%
Sweden.smallest('Arbetsloshet', 2014, 3)

#%%
Sweden.compare('Arbetsloshet', 2008, 2014)
