"""
File: blur.py
Name: Justin
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage

BLUR_TIMES = 99


def blur(img):
    """
    :param img: original photo
    :return: blurred photo

    Concept:
     2 nested loop:
        1st: find out each pixel represented by (x,y)
        2ed: find out the neighbor pixels around (x,y), which is a 3x3 matrix.
    """
    blur_blank = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            total_r = 0
            total_g = 0
            total_b = 0
            avg_count = 0
            for i in range(x-1, x+2):  # upper limit should add extra 1 because the real range is [x-1, x, x+1]
                for j in range(y-1, y+2):
                    if 0 <= i < img.width and 0 <= j < img.height:
                        pixel = img.get_pixel(i, j)
                        avg_count += 1
                        total_r += pixel.red
                        total_g += pixel.green
                        total_b += pixel.blue

            avg_r = total_r / avg_count
            avg_g = total_g / avg_count
            avg_b = total_b / avg_count

            blur_blank_p = blur_blank.get_pixel(x, y)
            blur_blank_p.red = avg_r
            blur_blank_p.green = avg_g
            blur_blank_p.blue = avg_b
    return blur_blank


def main():
    """
    TODO: import a photo, and show a blurred version
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(BLUR_TIMES):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
