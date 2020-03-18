from PIL import Image
from math import floor
import multiprocessing
import time

def counter():
    im = Image.open('somethingveryhightimetest.png') # Can be many different formats.
    #im = Image.open('Untitled.png') # Can be many different formats.
    pix = im.load()

    x, y = im.size

    dpi = 500

    vert = y
    horz = x

    threshold = 0.1

    '''
    for i in range(0, vert):
        i *= floor(y/vert)
        row = ""
        for k in range(0, horz):
            k *= floor(x/horz)
            try:
                R, G, B, A = pix[k,i]
                if R < round(255*threshold) and G < round(255*threshold) and B < round(255*threshold) and A == 255:
                    row += "█"
                elif R > B and R > G:
                    row += "R"
                else:
                    row += "_"
            except ValueError:
                R, G, B = pix[k,i]
                if R < round(255*threshold) and G < round(255*threshold) and B < round(255*threshold):
                    row += "█"
                elif R > B and R > G:
                    row += "R"
                else:
                    row += "_"

        
        row +="\n"
        with open("test.txt", "a", encoding="utf-8") as myfile:
            myfile.write(row)
    '''

    yes = 0
    no = 0
    for i in range(0, vert):
        i *= floor(y/vert)
        for k in range(0, horz):
            k *= floor(x/horz)
            try:
                R, G, B, A = pix[k,i]
                if R < round(255*threshold) and G < round(255*threshold) and B < round(255*threshold) and A == 255:
                    yes += 1
                else:
                    no += 1
            except ValueError:
                R, G, B = pix[k,i]
                if R < round(255*threshold) and G < round(255*threshold) and B < round(255*threshold):
                    yes += 1
                else:
                    no += 1
        print("Passed row "+str(i))
    print("Yes: "+str(yes)+", No: "+str(no))

if __name__ ==  '__main__':
    counter()