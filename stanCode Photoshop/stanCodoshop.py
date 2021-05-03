"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: Create a simple photoshop tool which can remove people in a photo.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    dist = math.sqrt((pixel.red - red) ** 2 + (pixel.green - green) ** 2 + (pixel.blue - blue) ** 2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_total = 0
    green_total = 0
    blue_total = 0

    for pixel in pixels:
        red_total += pixel.red
        green_total += pixel.green
        blue_total += pixel.blue

    red_average = red_total // len(pixels)
    green_average = green_total // len(pixels)
    blue_average = blue_total // len(pixels)

    return [red_average, green_average, blue_average]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    average_pixel = get_average(pixels)  # 0:red, 1:green, 2:blue
    dist_lst = []

    for i in range(len(pixels)):
        dist_lst.append(get_pixel_dist(pixels[i], average_pixel[0], average_pixel[1], average_pixel[2]))
    shortest_dist = min(dist_lst)
    shortest_index = dist_lst.index(shortest_dist)

    return pixels[shortest_index]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # loop over all the pixels
    for x in range(width):
        for y in range(height):
            # reset pixels
            pixels = []
            # import all images into this 'images' list
            for image in images:
                pixels.append(image.get_pixel(x, y))

            best_pixel = get_best_pixel(pixels)
            result_pixel = result.get_pixel(x, y)
            # print(best_pixel, result_pixel)  # Testing purpose
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)



if __name__ == '__main__':
    main()
