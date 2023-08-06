from . import CrystalGrid

import numpy as np

class CameraGrid(CrystalGrid.CrystalGrid):
    __pixelPitch = 1
    __pixels = 100

    def setPixelPitch(self, pixelPitch):
        self.__pixelPitch = pixelPitch

    def setPixels(self, pixels):
        self.__pixels = pixels

    def setCenterPosition(self, centerPosition):
        self.setOffset(centerPosition)

    def createCameraGrid(self):
        self.setMode('regular')
        params = {
            "Dimension": 2,
            "DistanceBetweenEmitters": self.__pixelPitch,
            "NumberOfEmitters": self.__pixels
        }
        self.setGridParameters(params)
        self.createBaseGrid()
        self.createRenderedGrid()

    def getCameraGrid(self):
        return self.getRenderedGrid()

    def getPixelPitch(self):
        return self.__pixelPitch

    def getPixels(self):
        return self.__pixels

    def getFullCamDim(self):
        return self.__pixels * self.__pixelPitch

    def getHalfCamDim(self):
        return self.getFullCamDim() * 0.5


if __name__ == "__main__":
    tempoCamera = CameraGrid()
    tempoCamera.setPixelPitch(5e-6)
    tempoCamera.setPixels(768)
    tempoCamera.setAngles(0.0, 0.5*np.pi, 0.0)
    tempoCamera.setCenterPosition([0.19,0.0,0.0])
    tempoCamera.createCameraGrid()
    temporalPositions = tempoCamera.getCameraGrid()
    print("hello")