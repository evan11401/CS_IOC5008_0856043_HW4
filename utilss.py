import numpy as np
from itertools import groupby
from pycocotools import mask as maskutil

def binary_mask_to_rle(binary_mask):
    rle = {'counts': [], 'size': list(binary_mask.shape)}
    counts = rle.get('counts')
    print('mask shape',binary_mask.shape)
    
    for i, (value, elements) in enumerate(groupby(binary_mask.view(-1) )):
        #print(i, value, list(elements))
        if i == 0 and value == 1:
            counts.append(0)
        counts.append(len(list(elements)))
    #compressed_rle = maskutil.frPyObjects(rle, rle.get('size')[0], rle.get('size')[1])
    compressed_rle = maskutil.frPyObjects(rle, 1, 1)
    compressed_rle['counts'] = str(compressed_rle['counts'], encoding='utf-8')
    return compressed_rle