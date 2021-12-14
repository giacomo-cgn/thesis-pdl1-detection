import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2lab, deltaE_ciede2000

def color_distance_max(tile, base_color, threshold, max_distance, num_tile_pixels, show_hist=False, hist_color='blue', hist_xlabel='delta from base color'):   
    rgb_tile = tile.convert('RGB')
    lab_tile = rgb2lab(rgb_tile)

    lab_base_color = rgb2lab(np.uint8(np.asarray([[base_color]])))
    
    delta = np.asarray(deltaE_ciede2000(lab_base_color, lab_tile))
    
    if (show_hist == True):
        flat_delta = delta.ravel()
        n, bins, patches = plt.hist(flat_delta, color = hist_color, bins = 100)
        plt.xlabel(hist_xlabel)
        plt.ylabel('number of pixels')
        plt.show()
    
    num_pixel_over_max = np.sum(delta>max_distance)
    if num_pixel_over_max/num_tile_pixels > 0.8:
        #returns that all tile pixels are close to white => outside ROI
        return num_tile_pixels
    
    else:
        num_close_pixel = np.sum(delta<threshold)
        return num_close_pixel