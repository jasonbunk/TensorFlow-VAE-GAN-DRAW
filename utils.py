import numpy as np
from scipy.misc import imsave

def floatToPixel(X):
    X[X<0.0] = 0.0
    X[X>1.0] = 1.0
    return np.round(X*255.0).astype(np.uint8)

def color_grid_vis(X, show=False, savename=None, transform=floatToPixel):
    ngrid = int(np.ceil(np.sqrt(len(X))))
    npxs = int(round(np.sqrt(X[0].size/3)))
    img = np.zeros((npxs * ngrid + ngrid - 1,
                    npxs * ngrid + ngrid - 1, 3))
    for i, x in enumerate(X):
        j = i % ngrid
        i = i / ngrid
        if transform is not None:
            x = transform(x)
        img[i*npxs+i:(i*npxs)+npxs+i, j*npxs+j:(j*npxs)+npxs+j] = x
    if show:
        import matplotlib.pyplot as plt
        plt.imshow(img, interpolation='nearest')
        plt.show()
    if savename is not None:
        imsave(savename, img)
    return img

def bw_grid_vis(X, show=False, savename=None, transform=floatToPixel):
    ngrid = int(np.ceil(np.sqrt(len(X))))
    npxs = int(round(np.sqrt(X[0].size)))
    img = np.zeros((npxs * ngrid + ngrid - 1,
                    npxs * ngrid + ngrid - 1))
    for i, x in enumerate(X):
        j = i % ngrid
        i = i / ngrid
        if transform is not None:
            x = transform(x)
        img[i*npxs+i:(i*npxs)+npxs+i, j*npxs+j:(j*npxs)+npxs+j] = x
    if show:
        import matplotlib.pyplot as plt
        plt.imshow(img, interpolation='nearest')
        plt.show()
    if savename is not None:
        imsave(savename, img)
    return img
