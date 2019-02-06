import RasterHandler
import matplotlib.pyplot as plt

if __name__ == "__main__":
    raster = RasterHandler.readRaster("RasterExample1.txt")
    plt.imshow(raster.getData(), cmap="RdYlBu")
    plt.colorbar()
    plt.show()
