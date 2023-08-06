# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 12:07:46 2018

@author: Stefan
"""
"""
Import Statements for submodules
"""
import helpers.CrystalGrid
import helpers.CameraGrid
import helpers.CudaWrapper

import numpy as np
import numba

import time
import matplotlib.pyplot as plt

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl

"""
Declarations of package class
"""
class InterferencePackage:
    __crystalGrid = []
    __cameraGrid = []
    __cudaWrapper = []

    output= []
    
    """ The main InterferenceStuff that handles everything """
    def __init__(self):
        self.__crystalGrid = helpers.CrystalGrid.CrystalGrid()
        self.__cameraGrid = helpers.CameraGrid.CameraGrid()
        self.__cudaWrapper = helpers.CudaWrapper.CudaWrapper()


    def LoadGrid(self):
        params = {
            "Dimension": 1,
            "DistanceBetweenEmitters": 10e-6,
            "NumberOfEmitters": 2
        }
        self.__crystalGrid.setMode('regular')
        self.__crystalGrid.setGridParameters(params)
        self.__crystalGrid.createBaseGrid()
        self.__crystalGrid.setAngles(0.5*np.pi, 0.0, 0.0)
        self.__crystalGrid.setOffset([0.0, 0.0, 0.0])
        self.__crystalGrid.createRenderedGrid()

    def LoadCamera(self):
        self.__cameraGrid.setPixelPitch(2.5e-6)
        self.__cameraGrid.setPixels(300)
        self.__cameraGrid.setAngles(0.0, 0.5*np.pi, 0.5*np.pi)
        self.__cameraGrid.setCenterPosition([0.1, 0.0, 0.0])
        self.__cameraGrid.createCameraGrid()

    def printTotalSetting(self):
        app = QtGui.QApplication([])
        w = gl.GLViewWidget()
        w.opts['distance'] = 5
        w.show()
        w.setWindowTitle('Emitter Crystal Geometry')
        g = gl.GLGridItem()
        w.addItem(g)
        posCrys = self.__crystalGrid.getRenderedGrid()
        crysHandle = gl.GLScatterPlotItem(pos=posCrys, color=(0, 1, 1, .7), size=5e-11, pxMode=False)
        w.addItem(crysHandle)

        posCam = self.__cameraGrid.getRenderedGrid()
        camHandle = gl.GLScatterPlotItem(pos=posCam, color=(1, 0, 1, .7), size=2e-6, pxMode=False)
        w.addItem(camHandle)

        QtGui.QApplication.instance().exec_()

    def printEmitters(self):
        app = QtGui.QApplication([])
        w = gl.GLViewWidget()
        w.opts['distance'] = 5
        w.show()
        w.setWindowTitle('Emitter Crystal Geometry')
        g = gl.GLGridItem()
        w.addItem(g)
        posCrys = self.__crystalGrid.getRenderedGrid()
        crysHandle = gl.GLScatterPlotItem(pos=posCrys, color=(0, 1, 1, .7), size=5e-11, pxMode=False)
        w.addItem(crysHandle)

        QtGui.QApplication.instance().exec_()

    def printDetectors(self):
        app = QtGui.QApplication([])
        w = gl.GLViewWidget()
        w.opts['distance'] = 1
        w.show()
        w.setWindowTitle('Emitter Crystal Geometry')
        g = gl.GLGridItem()
        w.addItem(g)
        posCam = self.__cameraGrid.getRenderedGrid()
        camHandle = gl.GLScatterPlotItem(pos=posCam, color=(1, 0, 1, .7), size=2e-6, pxMode=False)
        w.addItem(camHandle)

        QtGui.QApplication.instance().exec_()

    def doInterference(self):
        #self.__cudaWrapper.calculateImages(1, self.__crystalGrid.getRenderedGrid(), self.__cameraGrid.getRenderedGrid())
        self.__cudaWrapper.calculateImage(self.__crystalGrid.getRenderedGrid(), self.__cameraGrid.getRenderedGrid())
        self.output = self.__cudaWrapper.getOutputImages()


    """
    Helper Stuff
    """
    def getHalfCamDim(self):
        return self.__cameraGrid.getHalfCamDim()

"""
Testing and stuff, later it should be real tests
"""
if __name__ == "__main__":
    print("direct routines")
    interference = InterferencePackage()
    interference.LoadGrid()
    interference.LoadCamera()
    interference.printTotalSetting()
    timeOne = time.time()
    interference.doInterference()
    #print("needed " + str((time.time()-timeOne)/1000) + " seconds for 1 image. That is " + str(1/((time.time()-timeOne)/1000)) + " images per second")
    out = interference.output
    image = out.reshape((300,300))
    camDim = interference.getHalfCamDim()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(image, cmap='hot', interpolation='none', extent=[-camDim, camDim, -camDim, camDim], aspect=1)
    #plt.imshow(image)
    plt.show()
    print('finished')