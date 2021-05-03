"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This file gets the dictionary 'name_data' from babynames.py, and creates a UI window, displaying a Line Plot,
which showing the relation between Name and Year-Rank.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000

# Plot element offset
LINE_Y_OFFSET = 20
DOT_R = 5


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    return ((width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)) * year_index


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Draw 4 outlines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, width=LINE_WIDTH)
    canvas.create_line(CANVAS_WIDTH - GRAPH_MARGIN_SIZE, 0, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, width=LINE_WIDTH)

    # Create x axis label: years
    grid = (CANVAS_WIDTH - GRAPH_MARGIN_SIZE * 2) / len(YEARS)
    for i in range(len(YEARS)):
        nw_x = get_x_coordinate(CANVAS_WIDTH, i) + GRAPH_MARGIN_SIZE + TEXT_DX
        canvas.create_text(nw_x, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW, font='times 10')
        if i < len(YEARS) - 1:
            canvas.create_line(nw_x + grid, 0, nw_x + grid, CANVAS_HEIGHT, width=LINE_WIDTH)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    for i in range(len(lookup_names)):
        #  start again if run through 4 colors
        color = COLORS[i % len(COLORS)]
        # start looping all the year rank of the Names Input
        if lookup_names[i] in name_data:

            # print out all the year-rank of this name
            for j in range(len(YEARS)):
                nw_x = get_x_coordinate(CANVAS_WIDTH, j) + GRAPH_MARGIN_SIZE + TEXT_DX
                year = str(YEARS[j])

                # if the name ranks higher than 1000
                if year in name_data[lookup_names[i]]:
                    # Draw the point, print out name and rank
                    name_rank = int(name_data[lookup_names[i]][year])
                    nw_y = (name_rank / 1000) * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) + GRAPH_MARGIN_SIZE
                    canvas.create_text(nw_x + 2*TEXT_DX, nw_y, text=f'{lookup_names[i]}, {name_data[lookup_names[i]][year]}', anchor=tkinter.NW, font='times 10', fill=color)

                # if the name ranks lower than 1000
                else:
                    nw_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2
                    canvas.create_text(nw_x + 2*TEXT_DX, nw_y, text=f'{lookup_names[i]}, *',
                                       anchor=tkinter.NW, font='times 10', fill=color)

                # Draw dot on the line
                canvas.create_oval(nw_x - DOT_R, nw_y + LINE_Y_OFFSET - DOT_R, nw_x + DOT_R, nw_y + LINE_Y_OFFSET + DOT_R, fill=color, width=0)

                # Draw line plot, start drawing the line from second point(j == 1)
                if j > 0:
                    # first point comes from previous coordinate
                    # second point of the line(line_x2, line_y2)
                    line_x2 = nw_x
                    line_y2 = nw_y + LINE_Y_OFFSET  # +20 is to make the line not overlap on the text
                    # will call the previous coordinate from below(line_x1, line_y1)
                    canvas.create_line(line_x1, line_y1, line_x2, line_y2, width=LINE_WIDTH, fill=color)

                # record the previous coordinate
                line_x1 = nw_x
                line_y1 = nw_y + LINE_Y_OFFSET  # +20 is to make the line not overlap on the text


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)
    # print(name_data)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
