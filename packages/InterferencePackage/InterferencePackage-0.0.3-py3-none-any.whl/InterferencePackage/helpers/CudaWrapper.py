import numpy as np
import math
import cmath
from numba import cuda
from numba import int32, float32, float64, complex128

class CudaWrapper:
    #RAM Handles
    outPutSet = []
    emitterArray = []
    detectorarray = []

    #VRAM Handles
    VramOutPut = []
    VramEmitter = []
    VramDetectors = []

    def __init__(self):
        pass

    def getOutputImages(self):
        return self.outPutSet

    def calculateImage(self, emitterArray, detectorArray):
        # create needed Stuff
        self.outPutSet = np.zeros(len(detectorArray), dtype=np.float64)
        self.emitterArray = emitterArray
        self.detectorarray = detectorArray

        # allocate VRAM
        self.VramOutPut = cuda.to_device(self.outPutSet)
        self.VramEmitter = cuda.to_device(self.emitterArray)
        self.VramDetectors = cuda.to_device(self.detectorarray)

        # threadpositioning
        threadsperblock = 256
        blockspergrid = len(detectorArray) // 256 + 1

        # Run CUDA Processs
        self.singleInterferenceKernel[blockspergrid, threadsperblock](self.VramEmitter, self.VramDetectors, self.VramOutPut)

        # Copy back to RAM
        self.outPutSet = self.VramOutPut.copy_to_host()



    @cuda.jit('void(float64[:,:], float64[:,:], float64[:])')
    def singleInterferenceKernel(Emitters, Detectors, Output):
        #get Detectorposition
        i = cuda.grid(1)
        #cancel thread if outside detector
        max_X = len(Output) - 1
        if (i > max_X):
            return
        # value needed for every calculation
        twoPiByLambda = (2 * cmath.pi / 0.194e-9)
        twoPiByLambda = (2 * cmath.pi / 500e-9)
        im = complex(0.0,1.0)
        # calculate Intesity for Pixel

        complexPhase = complex(0.0,0.0)
        accumulatedReal = 0.0
        accumulatedImaginary = 0.0
        for k in range(len(Emitters)):
            difference = cuda.local.array(3, float64)
            for j in range(3):
                difference[j] =(Detectors[i][j])
            distance = math.sqrt(math.pow(difference[0], 2) + math.pow(difference[1], 2) + math.pow(difference[2], 2))
            # calculate phase
            phase = twoPiByLambda * distance
            #complexPhase = cmath.exp(im * phase)*(1/distance)
            accumulatedReal += math.cos(phase)
            accumulatedImaginary += math.sin(phase)
        #add to output Array
        value = math.pow(accumulatedImaginary, 2) + math.pow(accumulatedReal.imag, 2)
        cuda.atomic.add(Output, i, value)

    def calculateImages(self, numberOfImages, emitterArray, detectorArray):

        #create needed Stuff
        self.outPutSet = np.zeros((numberOfImages, len(detectorArray)), dtype=np.float64)
        self.emitterArray = emitterArray
        self.detectorarray = detectorArray

        #allocate VRAM
        self.VramOutPut = cuda.to_device(self.outPutSet)
        self.VramEmitter = cuda.to_device(self.emitterArray)
        self.VramDetectors = cuda.to_device(self.detectorarray)

        #threadpositioning
        threadsperblock = (1, 256)
        blockspergrid = (numberOfImages, len(detectorArray) // 256 + 1)

        #Run CUDA Processs
        self.interferenceKernel[blockspergrid, threadsperblock](self.VramEmitter, self.VramDetectors, self.VramOutPut)

        #Copy back to RAM
        self.outPutSet = self.VramOutPut.copy_to_host()


    @cuda.jit
    def interferenceKernel(emitters, detectors, output):
        #get Thread position, i = Picture, j = pixel
        i, j = cuda.grid(2)

        # check if we are outside of allowed values
        max_dimx = output.shape[0] - 1
        max_dimy = output.shape[1] - 1
        # check if correlation is allowed
        if (i > max_dimx or j > max_dimy):
            return

        #value needed for every calculation
        twoPiByLambda = ((2*cmath.pi)/(0.194e-9))

        #calculate Intesity for Pixel
        temporal = complex(0.0, 0.0)
        for k in range(len(emitters)):
            #calculate distance between emitter and detector

            distanceSquared = 0.
            for l in range(3):
                distanceSquared = distanceSquared + (emitters[k][l] - detectors[j][l])**2
            distance = math.sqrt(distanceSquared)

            #calculate phase
            im = complex(0., 1.)
            phase = cmath.exp(im*twoPiByLambda*distance)
            #add phase to sum
            temporal = temporal + phase


        #add to output Array
        value = abs(temporal)**2
        #cuda.atomic.add(output, (i, j), value)
        #output[i][j] = abs(temporal)**2