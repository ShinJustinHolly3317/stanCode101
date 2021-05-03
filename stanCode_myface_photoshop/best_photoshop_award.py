"""
File: best_photoshop_award.py
Name: Justin Kao(discussed with Tina)
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.15

BLACK_PIXEL = 100

MAN_H_PERCENTAGE = 1.05/10

MAN_H_PERCENTAGE2 = 4/10

MAN_H_SCALE = 5.3/10

MAN_V_PERCENTAGE = 1.7/10

MAN_V_PERCENTAGE2 = 6.7/10

MAN_V_SCALE = 5.3/10

RED_FILTER = 1.2

BLACK_FILTER = 1

WHITE_FILTER = 0.9


def main():
    """
    TODO: replace "Shining" killer's face with my face.
    """
    fig_me = SimpleImage("image_contest/me.jpg")
    background = SimpleImage("image_contest/shining.jpg")
    new_fig = blank_img(fig_me, background)
    # new_fig.show()
    new_fig = more_contrast(new_fig)
    result = combine(new_fig, background)
    result.show()


def blank_img(fig_me, background):
    """
    todo: This function create a blank image, shrink my face, and put it on the right place.
    :param fig_me: my photo, already loaded
    :param background: "Shining" poster, already loaded
    :return img: shrunk photo of my face

    Concept: try and error to find out correct scale and position.
    """
    blank = SimpleImage.blank(background.width, background.height)
    for x in range(background.width):
        for y in range(background.height):
            if (((x + 20) * 1/MAN_H_SCALE) < background.width and (x > background.width * MAN_H_PERCENTAGE and x < background.width * MAN_H_PERCENTAGE2)) and (y > background.height*MAN_V_PERCENTAGE and y<fig_me.height*MAN_V_PERCENTAGE2):
                fig_p = fig_me.get_pixel((x +20) * 1/MAN_H_SCALE, (y - fig_me.height*MAN_V_PERCENTAGE)*1/MAN_V_SCALE)
                avg = (fig_p.red + fig_p.green + fig_p.blue) // 3
                total = fig_p.red + fig_p.green + fig_p.blue
                rg = fig_p.red/(fig_p.green+1)
                rb = fig_p.red/(fig_p.blue+1)
                if rg > 1 and y > background.height * 0.4:
                    blank_p = blank.get_pixel(x, y)
                    blank_p.red = fig_p.red * RED_FILTER
                    blank_p.green = fig_p.green
                    blank_p.blue = fig_p.blue
                elif y < background.height * 0.45:
                    blank_p = blank.get_pixel(x, y)
                    blank_p.red = fig_p.red * RED_FILTER
                    blank_p.green = fig_p.green
                    blank_p.blue = fig_p.blue
                else:
                    blank_p = blank.get_pixel(x, y)
                    blank_p.green = 255
                    blank_p.red = 0
                    blank_p.blue = 0
            else:
                blank_p = blank.get_pixel(x, y)
                blank_p.green = 255
                blank_p.red = 0
                blank_p.blue = 0
    return blank


def combine(fig_me, background):
    """
    :param fig_me: new_fig which scale and relocate my face.
    :param background: "Shining"
    :return img: combine new_fig with "Shining" poster.
    """
    # fig_me.make_as_big_as(background)
    for x in range(fig_me.width):
        for y in range(fig_me.height):
            fig_p = fig_me.get_pixel(x, y)
            bg_p = background.get_pixel(x, y)
            avg = (fig_p.red + fig_p.green + fig_p.blue) // 3
            total = fig_p.red + fig_p.green + fig_p.blue
            bigger = max(fig_p.red, fig_p.blue)
            if fig_p.green > avg * THRESHOLD and total > BLACK_PIXEL:
                fig_p.red = bg_p.red
                fig_p.green = bg_p.green
                fig_p.blue = bg_p.blue
    return fig_me


def more_contrast(fig_img):
    """
    todo: Adjust the color of my face.
    :param fig_img: new_fig which scale and relocate my face.
    Concept: Each pixel RGB multiply by a factor
    """
    for x in range(fig_img.width):
        for y in range(fig_img.height):
            pixel = fig_img.get_pixel(x, y)
            total = pixel.red+pixel.blue+pixel.green
            avg = total//3
            if total < 300:
                pixel.red *= BLACK_FILTER
                pixel.green *= BLACK_FILTER
                pixel.blue *= BLACK_FILTER
            elif pixel.red > avg:
                pixel.red *= WHITE_FILTER
                pixel.green *= WHITE_FILTER
                pixel.blue *= WHITE_FILTER
    return fig_img


if __name__ == '__main__':
    main()
