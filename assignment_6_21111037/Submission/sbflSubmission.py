#!/usr/bin/env python3

import argparse
import sys
import numpy as np
from numpy.core.numeric import NaN
sys.path.insert(0,'../KachuaCore/')
from irgen import *
from kast.builder import astGenPass
from sbfl import *
import csv
def fitnessScore(IndividualObject):
    """
    Parameters
    ----------
    IndividualObject : Individual (definition of this class is in KachuaCore/sbfl.py)
        This is a object of class Individual. The Object has 3 elements
        1. IndividualObject.individual : activity matrix.
                                    type : list, row implies a test
                                    and element of rows are components.
        2. IndividualObject.fitness : fitness of activity matix.
                                    type : float
        3. Indivisual.fitness_valid : a flag used by Genetic Algorithm.
                                    type : boolean
    Returns
    -------
    fitness_score : flaot
        returns the fitness-score of the activity matrix.
        Note : No need to set/change fitness and fitness_valid attributes.
    """


    #Design the fitness function
    fitness_score = 0
    activity_mat = np.array(IndividualObject.individual,dtype='int');
    activity_mat = activity_mat[:,:activity_mat.shape[1]-1]
    #Use 'activity_mat' to compute fitness of it.
    #ToDo : Write your code here to compute fitness of test-suite
    
    # Finding the number of columns of the given activity_mat matrix
    mycol = activity_mat.shape[1]
   
    # Define a DIctionary
    mydict = {}

    # declare a variable
    indy = 0

    # Convert the given Numpy array(activity_mat) into a dictionary of columns wise for ex column1 is in index1
    for i in range(mycol):
        x = list(activity_mat[:, i])
        
        mydict.update({indy:x})
        indy= indy + 1
    
    #define a numpy array intialize to zeroes
    w = np.zeros(mycol)

    # Finding the Weight for each columns i.e. how many times a column is duplicated
    for k in range(mycol):
        for i in range(mycol):
            if mydict.get(k) == list(activity_mat[:, i]):
                w[k] = w[k] + 1


    w = w-1
    w = w /(mycol-1)
    sum = np.sum(w)

    # Applying the Ulysis Score Formula to find the fitness_score
    fitness_score = sum / mycol
    
    return fitness_score

#This class takes a spectrum and generates ranks of each components.
#finish implementation of this class.
class SpectrumBugs():
    def __init__(self,spectrum):
        self.spectrum = np.array(spectrum,dtype='int')        
        self.comps = self.spectrum.shape[1] - 1
        self.tests = self.spectrum.shape[0]
        self.activity_mat = self.spectrum[:,:self.comps]
        self.errorVec = self.spectrum[:,-1]

    def getActivity(self,comp_index):
        '''
        get activity of component 'comp_index'
        Parameters
        ----------
        comp_index : int
        '''
        return self.activity_mat[:,comp_index]

    def suspiciousness(self,comp_index):
        '''
        Parameters
        ----------
        comp_index : int
            component number/index of which you want to compute how suspicious
            the component is. assumption: if a program has 3 components then
            they are denoted as c0,c1,c2 i.e 0,1,2
        Returns
        -------
        sus_score : float
            suspiciousness value/score of component 'comp_index'
        '''
        sus_score = 0

        #ToDo : implement the suspiciousness score function.
        icol = SpectrumBugs.getActivity(self,comp_index)
        errvec = self.errorVec

        # Finding the Cp,Cf,Np,Nf
        # Cf = Number of failing tests that execute C
        # Cp = Number of passing tests that execute C
        # Nf = Number of failing tests that do not execute C
        # Np = Number of passing tests that do not execute C

        Cp = Cf = Np = Nf =0
        for i in range(len(icol)):
            if icol[i] == 1 and errvec[i] == 0:
                Cp = Cp + 1
            if icol[i] == errvec[i] == 1:
                Cf = Cf + 1
            if icol[i] == errvec[i] == 0:
                Np = Np + 1
            if icol[i] == 0 and errvec[i] == 1:
                Nf = Nf + 1

        #Ochiai score
        # if Cf: 
        #     sus_score = Cf / np.sqrt((Cf + Nf)*(Cf + Cp))
        # else:
        #     sus_score = 0 
        
        #Tarantula score best work
        try:
            if Cf and (Cp or Np): 
                sus_score = (Cf / (Cf+Nf))/((Cf / (Cf+Nf))*(Cp/(Cp+Np)))

            else :
                sus_score = 0

        except ZeroDivisionError:
            sus_score = 1

        # Ochiai2 Score still good
        # if Cf and Np: 
        #     sus_score = Cf*Np / np.sqrt((Cf + Nf)*(Cf + Cp)*(Np + Nf)*(Np + Cf))
        # else:
        #     sus_score = 0 

        # OP square score
        # sus_score =Cf -  (Cp / (Cp + Np + 1))

        # Jaccard Score
        # if Cf:
        #     sus_score = Cf / (Cf + Cp + Nf)
        # else:
        #     sus_score = 0
        
        # D-star Score
        # if Cf and (Cp or Nf):
        #     sus_score = (Cf*Cf) / (Cp + Nf)
        
        
        return sus_score

    def getRankList(self):
        '''
        find ranks of each components according to their suspeciousness score.
        
        Returns
        -------
        rankList : list
            ranList will contain data in this format:
                suppose c1,c2,c3,c4 are components and their ranks are
                1,2,3,4 then rankList will be :
                    [[c1,1],
                     [c2,2],
                     [c3,3],
                     [c4,4]]
        '''
        # Define a list
        sus = []

        # Find the number of columns on which we will call suspicious Score
        col = self.spectrum.shape[1] - 1
     
        # suspicious call
        for i in range(col):
            m = []

            # Manipulation Required to produce the output accroding to given above
            m.insert(0, "c"+ str(i)) 
            m.insert(1, self.suspiciousness(i))

            sus.insert(i,m)

        #define a variable
        max = 0

        # Define a List
        rankList = []

        #ToDo : implement rankList
        for k in range(col):
            for i in range(len(sus)):
                if max <= sus[i][1]:
                    max = sus[i][1]
                    mark = i
            print(k,col,"mani",max,mark,sus)
            rankList.insert(k, [sus[mark][0],k+1])
            sus.remove(sus[mark]) 
            max = 0      
        
        
        return rankList

#do not modify this function.
def computeRanks(spectrum,outfilename):
    '''
    Parameters
    ----------
    spectrum : list
        spectrum
    outfilename : str
        components and their ranks.
    '''
    S = SpectrumBugs(spectrum)
    rankList = S.getRankList();
    with open(outfilename,"w") as file:
        writer = csv.writer(file)
        writer.writerows(rankList) 
