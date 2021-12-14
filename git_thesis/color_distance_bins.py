import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2lab, deltaE_ciede2000

def color_distance_bins(tile, base_color, num_bins=100, show_hist=False, hist_color='blue', hist_xlabel='delta from base color'):   
    rgb_tile = tile.convert('RGB')
    lab_tile = rgb2lab(rgb_tile)

    lab_base_color = rgb2lab(np.uint8(np.asarray([[base_color]])))
    
    delta = np.asarray(deltaE_ciede2000(lab_base_color, lab_tile))
    
    #flat_delta = delta.ravel()
    #n, bins, patches = plt.hist(flat_delta, color = hist_color, bins = num_bins)
    hist = np.histogram(delta, bins=num_bins, range =(0,100))[0]
    if (show_hist == True):
        plt.xlabel(hist_xlabel)
        plt.ylabel('number of pixels')
        plt.show()
    
    #returns array number of elements of each bin
    #return np.asarray(n)
    return hist