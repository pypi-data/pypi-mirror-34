# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 13:16:34 2018

@author: Stefan
"""
import numpy as np
import numba

class CrystalGrid:
    #variables
    __baseGrid = []
    __renderedGrid = []
    __mode = "" #Either positions, regular, or Crystfel File
    __GridParameters = []
    __angleOne = 0.
    __angleTwo = 0.
    __angleThree = 0.
    __offset = np.array([0, 0, 0])
    
    #constants
    __allowedModes = ['positions', 'regular', 'crystalfile']
    
    def __init__(self):
        """ Init of Grid """
        pass
    
    def setMode(self, Mode):
        """ Defines GridMode {Positions, Regular, CrystFel} """
        self.__mode = Mode
    
    def setGridParameters(self, GridParameters):
        """ Sets the needed GridParameters accordingliy to the input """
        self.__GridParameters = GridParameters
    
    def createBaseGrid(self):
        """ craeates a baisc and centered grid """
        if  self.__mode not in self.__allowedModes:
            raise ValueError('mode not allowed')
        if self.__mode == 'crystalfile':
            raise NotImplementedError
        if self.__mode == 'positions':
            rawPositions = self.__GridParameters["rawPositions"]
            zeroVector = self.__CenterOfMassOfBasegrid(rawPositions)
            self.__baseGrid = np.array(np.subtract(rawPositions, zeroVector))

        if self.__mode == 'regular':
            Dimensions = self.__GridParameters["Dimension"]
            NumberOfEmitters = self.__GridParameters["NumberOfEmitters"]
            DistanceBetweenEmitters = self.__GridParameters["DistanceBetweenEmitters"]

            axisOne = np.arange(NumberOfEmitters) * DistanceBetweenEmitters
            vectors = []
            for item in axisOne:
                vectors.append([item, 0, 0])
            if (Dimensions == 1):
                ZeroPosition = self.__CenterOfMassOfBasegrid(vectors)
                self.__baseGrid = np.array(np.subtract(vectors, ZeroPosition))
                return
            vectors2 = []
            for item in vectors:
                for item2 in axisOne:
                    vectors2.append([item[0], item2, 0])
            del vectors
            if (Dimensions == 2):
                ZeroPosition = self.__CenterOfMassOfBasegrid(vectors2)
                self.__baseGrid = np.array(np.subtract(vectors2, ZeroPosition))
                return
            vectors3 = []
            for item in vectors2:
                for item2 in axisOne:
                    vectors3.append([item[0], item[1], item2])
            if (Dimensions == 3):
                ZeroPosition = self.__CenterOfMassOfBasegrid(vectors3)
                self.__baseGrid = np.array(np.subtract(vectors3, ZeroPosition))
                return
            raise ValueError('wrong dimension')

    
    def setAngles(self, angleOne, angleTwo, angleThree):
        """ sets angles for grid rotation """
        self.__angleOne = angleOne
        self.__angleTwo = angleTwo
        self.__angleThree = angleThree
        
    def setOffset(self, Offset):
        """ defines Offset of grid """
        self.__offset = np.array(Offset)
        
    def createRenderedGrid(self):
        """ Apply rotation and offset to baseGrid """        
        tempoGrid = np.zeros_like(self.__baseGrid, dtype=np.float64)
        #Rotational Stuff
        eulerMatrix = self.__getEulerMatrix()
        for i in range(len(self.__baseGrid)):
            tempoGrid[i] = np.dot(eulerMatrix, self.__baseGrid[i])
        #TranslationalStuff
        for i in range(len(self.__baseGrid)):
            tempoGrid[i] = np.add(tempoGrid[i], self.__offset)
        #Reassign
        self.__renderedGrid = tempoGrid

    def getBaseGrid(self):
        return self.__baseGrid

    def getRenderedGrid(self):
        return self.__renderedGrid

    """
    Auxiliary functions
    """
    def __CenterOfMassOfBasegrid(self, whichEmitters = None):
        if whichEmitters == None:
            Emitters = self.__baseGrid
        else:
            Emitters = whichEmitters

        numberOfVectors = len(Emitters)
        summedVectors = np.zeros(3, dtype=np.float64)
        for i in range(len(Emitters)):
            emitterVal = Emitters[i]
            summedVectors = np.add(summedVectors, emitterVal)

        return np.divide(summedVectors, numberOfVectors)

    def __getEulerMatrix(self):
        #load empty matrix
        matrix = np.zeros((3,3), dtype= np.float64)

        #create helping values
        cosAlpha = np.cos(self.__angleOne)
        sinAlpha = np.sin(self.__angleOne)
        cosBeta = np.cos(self.__angleTwo)
        sinBeta = np.sin(self.__angleTwo)
        cosGamma = np.cos(self.__angleThree)
        sinGamma = np.sin(self.__angleThree)

        #assign values
        matrix = np.array([
            [(cosAlpha*cosGamma - sinAlpha*cosBeta*sinGamma), (-1*sinAlpha*cosGamma - cosAlpha*cosBeta*sinGamma), (sinBeta*sinGamma)],
            [(cosAlpha*sinGamma + sinAlpha*cosBeta*cosGamma), (-1*sinAlpha*sinGamma + cosAlpha*cosBeta*cosGamma), (-1*sinBeta*cosGamma)],
            [(sinAlpha*sinBeta), (cosAlpha*sinBeta), (cosBeta)]
        ])
        return matrix

if __name__ == "__main__":
    print('direct routines')

    params = {
        "Dimension": 3,
        "DistanceBetweenEmitters": 5e-6,
        "NumberOfEmitters": 10
    }
    tempoGrid = CrystalGrid()
    tempoGrid.setMode('regular')
    tempoGrid.setGridParameters(params)
    tempoGrid.createBaseGrid()
    tempoGrid.setOffset([0.1,0.0,0.0])
    tempoGrid.createRenderedGrid()
    baseGrid = tempoGrid.getRenderedGrid()
    print("hello")