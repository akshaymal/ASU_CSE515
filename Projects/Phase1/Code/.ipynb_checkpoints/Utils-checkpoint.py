import csv

import numpy as np
import scipy as scipy


def create_windows(image=None):
    # Exceptions
    if image is None:
        raise Exception("create_windows: image input param missing")

    # Creating windows over the image
    windows = []
    step = 8
    for x in range(0, image.shape[0], step):
        for y in range(0, image.shape[1], step):
            window = image[x:x + step, y:y + step]
            windows.append(window)
    return np.array(windows)


# def calculate_color_moments(windows=None):
#     # Exceptions
#     if windows is None:
#         raise Exception('calculate_color_moments: windows input param missing')
#
#     # Calculating color moments over windows
#     means = []
#     stds = []
#     skews = []
#     for index in range(0, len(windows)):
#         # Extracting window
#         window = windows[index]
#         flatten_window = window.flatten()
#
#         # Calculating mean, std deviation and skewness for window
#         mean = np.mean(flatten_window)
#         std = np.std(flatten_window)
#         skew = scipy.stats.skew(flatten_window)
#
#         # Appending results of each window to a list
#         means.append(mean)
#         stds.append(std)
#         skews.append(skew)
#
#     return [means, stds, skews]
#
#
# def write_color_moments(data=None, path=None):
#     if data is None:
#         raise Exception("write_color_moments: means/stds/skews/windows input param missing")
#     if path is None:
#         raise Exception("write_color_moments: path input param missing")
#
#     with open(path, 'w') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerow(data)