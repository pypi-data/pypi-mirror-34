import numpy as np
from scipy.ndimage import filters
from scipy.ndimage import gaussian_filter
from scipy import ndimage
import math
import utils
from matplotlib.colors import hsv_to_rgb

def boundary(ypix,xpix):
    ''' returns pixels of mask that are on the exterior of the mask '''
    ypix = np.expand_dims(ypix.flatten(),axis=1)
    xpix = np.expand_dims(xpix.flatten(),axis=1)
    npix = ypix.shape[0]
    idist = ((ypix - ypix.transpose())**2 + (xpix - xpix.transpose())**2)
    idist[np.arange(0,npix),np.arange(0,npix)] = 500
    nneigh = (idist==1).sum(axis=1) # number of neighbors of each point
    iext = (nneigh<4).flatten()
    return iext


def draw_masks(ops, stat, ops_plot, iscell, ichosen):
    '''creates RGB masks using stat and puts them in M1 or M2 depending on
    whether or not iscell is True for a given ROI
    args:
        ops: mean_image, Vcorr
        stat: xpix,ypix
        iscell: vector with True if ROI is cell
        ops_plot: plotROI, view, color, randcols
    outputs:
        M1: ROIs that are True in iscell
        M2: ROIs that are False in iscell
    '''
    ncells = iscell.shape[0]
    plotROI = ops_plot[0]
    view    = ops_plot[1]
    color   = ops_plot[2]
    cols    = ops_plot[3][:,color]

    Ly = ops['Ly']
    Lx = ops['Lx']
    Lam = np.zeros((2,Ly,Lx,1))
    H = np.zeros((2,Ly,Lx,1))
    S  = np.zeros((2,Ly,Lx,1))
    for n in range(0,ncells):
        lam     = stat[n]['lam']
        ypix    = stat[n]['ypix'].astype(np.int32)
        if view>0:
            ypix = ypix[stat[n]['iext']]
            lam = lam[stat[n]['iext']]
            lam = lam / lam.max()
        if ypix is not None:
            xpix = stat[n]['xpix'].astype(np.int32)
            if view>0:
                xpix = xpix[stat[n]['iext']]
            wmap = (1-int(iscell[n]))*np.ones(ypix.shape,dtype=np.int32)
            Lam[wmap,ypix,xpix]    = np.expand_dims(lam, axis=2)
            H[wmap,ypix,xpix]      = cols[n]*np.expand_dims(np.ones(ypix.shape), axis=2)
            S[wmap,ypix,xpix]      = np.expand_dims(np.ones(ypix.shape), axis=2)
            if n==ichosen:
                S[wmap,ypix,xpix] = np.expand_dims(np.zeros(ypix.shape), axis=2)

    V  = np.maximum(0, np.minimum(1, 0.75 * Lam / Lam[Lam>1e-10].mean()))
    #V  = np.expand_dims(V,axis=2)
    M = []
    if view>=0:
        if view == 0:
            mimg = ops['meanImg']
            #S = V
        else:
            vcorr = ops['Vcorr']
            mimg = np.zeros((ops['Ly'],ops['Lx']),np.float32)
            mimg[ops['yrange'][0]:ops['yrange'][1],
                ops['xrange'][0]:ops['xrange'][1]] = vcorr
        mimg = mimg - mimg.min()
        mimg = mimg / mimg.max()
        V[0,:,:,:] = np.expand_dims(mimg,axis=2)
        V[1,:,:,:] = np.expand_dims(mimg,axis=2)
        if view==1 and plotROI:
            V = np.minimum(1, V + S)

        if not plotROI:
            S = np.zeros((2,Ly,Lx,1))
    for j in range(0,2):
        hsv = np.concatenate((H[j,:,:],S[j,:,:],V[j,:,:]),axis=2)
        rgb = hsv_to_rgb(hsv)
        M.append(rgb)
    return M

def ROI_index(ops, stat):
    '''matrix Ly x Lx where each pixel is an ROI index (-1 if no ROI present)'''
    ncells = len(stat)-1
    Ly = ops['Ly']
    Lx = ops['Lx']
    iROI = -1 * np.ones((Ly,Lx), dtype=np.int32)
    for n in range(ncells):
        ypix = stat[n]['ypix']
        if ypix is not None:
            xpix = stat[n]['xpix']
            iROI[ypix,xpix] = n
    return iROI

def make_colorbar():
    H = np.arange(0,100).astype(np.float32)
    H = H / (100*1.3)
    H = H + 0.1
    H = 1 - H
    H = np.expand_dims(H,axis=1)
    S = np.ones((100,1))
    V = np.ones((100,1))
    hsv = np.concatenate((H,S,V), axis=1)
    colormat = hsv_to_rgb(hsv)
    colormat = np.expand_dims(colormat, axis=0)
    colormat = np.tile(colormat,(20,1,1))
    return colormat
