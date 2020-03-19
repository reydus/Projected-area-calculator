import PIL
from PIL import Image
from math import floor
import multiprocessing
import time

time.sleep(5)
def counter():
    im = Image.open('something.png') # Can be many different formats.
    pix = im.load()

    x, y = im.size
    print(str(x)+" "+str(y))
    dpi = 500

    # number of lines to process (vert, horz = y, x if 1 line per pixel)
    vert = y
    horz = x

    threshold = 0.1
    start = time.time()
    yes = 0
    no = 0
    buf = im.getdata()
    px = 0
    lr = 0
    for i in buf:
        try:
            R, G, B, A = i
            if R < round(255*threshold) and G < round(255*threshold) and B < round(255*threshold) and A == 255:
                yes += 1
        except ValueError:
            R, G, B = i
            if R < round(255*threshold) and G < round(255*threshold) and B < round(255*threshold):
                yes += 1
        px += 1
        if px//x != lr:
            lr = px//x
            print("Passed row "+str(lr))

    print("Yes: "+str(yes)+", No: "+str(no))
    end = time.time()
    area = float(yes)/(1000**2)
    print("Area: "+str(area)+" square meters.")
    print("It took me %.2f seconds" % (end-start))
    reportTime = open("report.txt","a")
    reportTime.write("\n"+str(end-start))
    reportTime.write("\n"+str(area))
    reportTime.close()
    return area

def count_time():
    timer = open("report.txt","r")
    chrono = []
    for line in timer:
        chrono.append(float(line))
    total = sum(chrono[:-1])
    print("%.2f seconds decompiling model file\n%.2f seconds plotting model\n%.2f seconds calculating area\nTotal: %.2f seconds." % (chrono[0], chrono[1], chrono[2], total))


if __name__ ==  '__main__':
    area = counter()
    count_time()