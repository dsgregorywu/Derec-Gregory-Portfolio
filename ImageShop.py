######################################################################
# Name: Derec
# Collaborators (Ben and Sam from QUAD Center):
# Section leader's name: Dash
# GenAI transcript (if used):
# List of extensions made (if any):
######################################################################

"""
This program is the starter file for the ImageShop application, which
implements the "Load" and "Flip Vertical" buttons.
"""

from filechooser import choose_input_file
from pgl import GWindow, GImage, GRect
from button import GButton
import random

# Constants

GWINDOW_WIDTH = 900
GWINDOW_HEIGHT = 500
BUTTON_WIDTH = 125
BUTTON_HEIGHT = 20
BUTTON_MARGIN = 10
BUTTON_BACKGROUND = "#CCCCCC"

# Derived constants

BUTTON_AREA_WIDTH = 2 * BUTTON_MARGIN + BUTTON_WIDTH
IMAGE_AREA_WIDTH = GWINDOW_WIDTH - BUTTON_AREA_WIDTH

# The image_shop application

def image_shop():
    def add_button(label, action):
        """
        Adds a button to the region on the left side of the window
        label is the text that will be displayed on the button and
        action is the callback function that will be run when the
        button is clicked.
        """
        x = BUTTON_MARGIN
        y = gw.next_button_y
        button = GButton(label, action)
        button.set_size(BUTTON_WIDTH, BUTTON_HEIGHT)
        gw.add(button, x, y)
        gw.next_button_y += BUTTON_HEIGHT + BUTTON_MARGIN

    def set_image(image):
        """
        Sets image as the current image after removing the old one.
        """
        if gw.current_image is not None:
            gw.remove(gw.current_image)
        gw.current_image = image
        x = BUTTON_AREA_WIDTH + (IMAGE_AREA_WIDTH - image.get_width()) / 2
        y = (gw.get_height() - image.get_height()) / 2
        gw.add(image, x, y)

    def load_button_action():
        """Callback function for the Load button"""
        filename = choose_input_file()
        if filename != "":
            set_image(GImage(filename))

    def flip_vertical_action():
        """Callback function for the Flip Vertical button"""
        if gw.current_image is not None:
            set_image(flip_vertical(gw.current_image))

    def flip_horizontal_action():
        """Callback function for the Flip Horizontal button"""
        if gw.current_image is not None:
            set_image(flip_horizontal(gw.current_image))

    def rotate_left_action():
        """Callback functon for the Rotate Left button"""
        if gw.current_image is not None:
            set_image(rotate_left(gw.current_image))

    def rotate_right_action():
        """Callback function for the Rotate Right button"""
        if gw.current_image is not None:
            set_image(rotate_right(gw.current_image))

    def grayscale_action():
        """Callback function for the Grayscale button"""
        if gw.current_image is not None:
            set_image(create_grayscale_image(gw.current_image))

    def greenscreen_action():    
        """Callback function for the Greenscreen button"""
        if gw.current_image is not None:
            set_image(greenscreen(gw.current_image))

    def equalizer_action():
        """Callback function for the Equalizer button"""
        if gw.current_image is not None:
            set_image(equalizer(gw.current_image))

    def randomizer_action():
        """Callback function for the Randomizer button"""
        if gw.current_image is not None:
            set_image(randomizer(gw.current_image))

    def color_changer_action():
        """Callback function for the Color Changer button"""
        if gw.current_image is not None:
            set_image(colorchanger(gw.current_image))
    
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    button_area = GRect(0, 0, BUTTON_AREA_WIDTH, GWINDOW_HEIGHT)    
    button_area.set_filled(True)
    button_area.set_color(BUTTON_BACKGROUND)
    gw.add(button_area)
    gw.next_button_y = BUTTON_MARGIN
    gw.current_image = None
    add_button("Load", load_button_action)
    add_button("Flip Vertical", flip_vertical_action)
    add_button("Flip Horizontal", flip_horizontal_action)
    add_button("Rotate Right", rotate_right_action)
    add_button("Rotate Left", rotate_left_action)
    add_button("Grayscale", grayscale_action)
    add_button("Green Screen", greenscreen_action)
    add_button("Equalizer", equalizer_action)
    add_button("Randomizer", randomizer_action)
    add_button("Color Changer", color_changer_action)

def create_grayscale_image(image):
    """
    Creates a grayscale image based on the luminance of each pixel
    """
    array = image.get_pixel_array()
    height = len(array)
    width = len(array[0])
    for i in range(height):
        for j in range(width):
            gray = luminance(array[i][j])
            array[i][j] = GImage.create_rgb_pixel(gray, gray, gray)
    return GImage(array)

def luminance(pixel):
    """
    Returns the luminance of a pixel, which indicates its subjective
    brightness.  This implementation uses the NTSC formula.
    """
    r = GImage.get_red(pixel)
    g = GImage.get_green(pixel)
    b = GImage.get_blue(pixel)
    return round(0.299 * r + 0.587 * g + 0.114 * b)

def flip_vertical(image): # Creates a new GImage from the original one by flipping it vertically.

    array = image.get_pixel_array()
    return GImage(array[::-1])

def flip_horizontal(image):  #Flips the image horizontally
    array2 = [row[::-1] for row in image.getPixelArray()]
    return GImage(array2)

def rotate_right(image):   #Rotates the image 90 degrees to the left
    arrayleft = image.get_pixel_array()
    leftheight = len(arrayleft[0])
    leftwidth = len(arrayleft)
    arrayleft2 = [[None for _ in range(leftwidth)] for _ in range(leftheight)]
    for row in range(leftwidth):
        for col in range(leftheight):
            arrayleft2[leftheight - col - 1][row] = arrayleft[row][col]
    return GImage(arrayleft2)

def rotate_left(image):  #Rotates the image to the right by 90 degrees
    arrayright = image.get_pixel_array()
    rightheight = len(arrayright[0])
    rightwidth = len(arrayright)
    arrayright2 = [[None for _ in range(rightwidth)] for _ in range(rightheight)]
    for row in range(rightwidth):
        for col in range(rightheight):
            arrayright2[col][rightwidth - row - 1] = arrayright[row][col]
    return GImage(arrayright2)
            
def greenscreen(image):   #Creates a greenscreen effect
    image1array = image.get_pixel_array()
    file = choose_input_file(image)
    if file == "":
        return image
    gsimage = GImage(file)
    image2array = gsimage.get_pixel_array()
    background_height = len(image1array)
    background_width = len(image1array[0])
    green_height = len(image2array)
    green_width = len(image2array[0])
    for i in range(min(background_height, green_height)):
        for j in range(min(background_width, green_width)):
            pixel = image2array[i][j]
            r = GImage.get_red(pixel)
            g = GImage.get_green(pixel)
            b = GImage.get_blue(pixel)
            if g < 2 * max(r, b): 
                image1array[i][j] = pixel
    return GImage(image1array)


def equalizer(image):
    """Equalizes image"""
    eqarray = image.get_pixel_array()
    arraywidth = len(eqarray[0])
    arrayheight = len(eqarray)
    lumhistdata = list()
    lumhistdata += [0] * 256
    for i in range(arrayheight):    #Finds luminance of each pixel and adds one to histogram of that luminanc
        for j in range(arraywidth):
            pixel = eqarray[i][j]
            pixellum = luminance(pixel)
            lumhistdata[pixellum] += 1
    chistint = 0
    lumlength = len(lumhistdata)
    cumulativehistogram = list()
    cumulativehistogram += [0] * lumlength
    for i in range (lumlength):    #Creates a cumulative histogram
        cumulativehistogram[chistint] = sum(lumhistdata[0:chistint])
        chistint += 1
    totalpixels = sum(lumhistdata)
    newarray = list()
    for i in range(arrayheight): #Finds the luminance of each pixel and increases it and replaces the pixel
        newrow = list()
        for j in range(arraywidth):
            pixel = eqarray[i][j]
            pixlum = luminance(pixel)
            newlum = ((255 * cumulativehistogram[pixlum]) // totalpixels)
            r = GImage.get_red(pixel)
            g = GImage.get_green(pixel)
            b = GImage.get_blue(pixel)
            if pixlum != 0:
                scalefactor = newlum / pixlum
            else: scalefactor = 1
            newr = min(255, int(r * scalefactor))
            newg = min(255, int(g * scalefactor))
            newb = min(255, int(b * scalefactor))
            newpixel = GImage.create_rgb_pixel(newr, newb, newg)
            newrow.append(newpixel)
        newarray.append(newrow)
    return GImage(newarray)

def randomizer(image):
    randomarray = image.get_pixel_array()
    arraywidth = len(randomarray)
    arrayheight = len(randomarray[0])
    randompixels = [pixel for row in randomarray for pixel in row]
    random.shuffle(randompixels) #Randomizes pixel order
    generatedarray = []
    arraynumber = 0
    for i in range(arraywidth): #Puts randomized pixels into lists, then adds those lists to a new array
        newrow = []
        for j in range(arrayheight):
            newrow.append(randompixels[arraynumber])
            arraynumber += 1
        generatedarray.append(newrow)
    return GImage(generatedarray)

def colorchanger(image):
    colorarray = image.get_pixel_array()
    arraywidth = len(colorarray)
    arrayheight = len(colorarray[0])
    colors = dict()
    for i in range(arraywidth):
        for j in range(arrayheight): #Finds each individual color and creates a new, randomized color
            pixelcol = colorarray[i][j]
            if pixelcol not in colors:  
                newr = random.randint(0, 255)
                newg = random.randint(0, 255)
                newb = random.randint(0, 255)
                newpixel = GImage.create_rgb_pixel(newr, newg, newb)
                colors[pixelcol] = newpixel  
    finalarray = list()
    for i in range(arraywidth): #Replaces old color with new, randomized color
        newrow = list()
        for j in range(arrayheight):
            pixelcol = colorarray[i][j]
            newrow.append(colors[pixelcol])
        finalarray.append(newrow)
    return GImage(finalarray)



# Startup code

if __name__ == "__main__":
    image_shop()
