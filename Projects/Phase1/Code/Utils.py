import csv
import numpy as np
import scipy as scipy

from skimage.feature import hog, local_binary_pattern


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


def calculate_color_moments(windows=None):
    # Exceptions
    if windows is None:
        raise Exception('calculate_color_moments: windows input param missing')

    # Calculating color moments over windows
    means = []
    stds = []
    skews = []
    for index in range(0, len(windows)):
        # Extracting window
        window = windows[index]
        flatten_window = window.flatten()

        # Calculating mean, std deviation and skewness for window
        mean = np.mean(window)
        std = np.std(window)
        skew = scipy.stats.skew(flatten_window)

        # Appending results of each window to a list
        means.append(mean)
        stds.append(std)
        skews.append(skew)

    color_moments = []
    color_moments.extend(means)
    color_moments.extend(stds)
    color_moments.extend(skews)
    return color_moments


def write_color_moments(data=None, path=None):
    if data is None:
        raise Exception("write_color_moments: means/stds/skews/windows input param missing")
    if path is None:
        raise Exception("write_color_moments: path input param missing")

    with open(path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)


def calculate_elbp(image=None, points=None, radius=None, method=None):
    if image is None or points is None or radius is None or method is None:
        raise Exception("calculate_elbp: image/points/radius/method input param missing")

    elbp = local_binary_pattern(image, P=points, R=radius, method=method)

    # Bining the results of ELBP
    bins = 2 ** points
    bining_results = np.histogram(elbp, bins=bins, range=(0.0, float(bins)))

    return bins, bining_results


def write_elbp(bining_results=None, path=None):
    if bining_results is None:
        raise Exception("write_elbp: bining_results input param missing")
    if path is None:
        raise Exception("write_elbp: path input param missing")

    # Writing results into a file
    with open(path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(bining_results[0])


def calculate_hog(image=None, orientations=None, pixels_per_cell=None, cells_per_block=None):
    if image is None or orientations is None or pixels_per_cell is None or cells_per_block is None:
        raise Exception("calculate_hog: image/orientationspixels_per_cell/pixels_per_cell/cells_per_block input param "
                        "missing")

    fd, hog_image = hog(image,
                        orientations=orientations,
                        pixels_per_cell=pixels_per_cell,
                        cells_per_block=cells_per_block,
                        visualize=True)

    return fd, hog_image


def write_hog(path=None, feature_values=None):
    if feature_values is None:
        raise Exception("write_elbp: feature_values input param missing")
    if path is None:
        raise Exception("write_hog: path input param missing")

    with open(path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(feature_values)
