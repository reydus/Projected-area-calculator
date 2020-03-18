import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import json
import time
import svgwrite
#from CairoSVG/cairosvg import "__init__.py"

def matchNodesFaces(nodes,faces):
    triangles = []
    for i in range(0, len(faces)):
        for k in range(0, len(faces[i])):
            faces[i][k] = nodes[faces[i][k]]
    triangles = faces
    return triangles

def getTriangles(model, target="all"):
    if target == "all":
        triangles = {}
        for i in range(0, len(model)):
            triangles[model[i]["name"]] = matchNodesFaces(nodes, faces)
        return triangles
    else:
        triangles = []
        for i in range(0, len(model)):
            if model[i]["name"] == target:
                nodes = model[i]["vertices"]
                faces = model[i]["faces"]
                triangles = matchNodesFaces(nodes, faces)
        return triangles
        
def make2D(triangles):
    newTrigs = []
    for i in range(0, len(triangles)):
        trig2D = []

        for k in [0,1,2]:
            newVertex = [triangles[i][k][0],triangles[i][k][2]]
            trig2D.append(newVertex)
        newTrigs.append(trig2D)

    return newTrigs


def draw_plot():
    resolution = 500 # dpi
    ax = plt.axes([0,0,1,1], frameon=False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    fig = plt.autoscale(tight=True)
    fig = plt.gcf()



    start = time.time()
    print("timer started")

    highlightedges = False
    
    model = json.load(open("./everything.json","r"))
 
    # DEMO MODE
    preconfig = 0
    for k in range(1, len(model)):
        if model[k]["noFaces"] != 0:
            print("Drawing "+model[k]["name"])
            triangles = getTriangles(model,model[k]["name"])
            triangles = make2D(triangles)


            #CONFIGURATE DIMENSIONS
            #CALCULATE MAXIMUM WIDTH = LEFTMOST VERTEX TO RIGHTMOST VERTEX
            
            if preconfig == 0:
                preconfig = 1
                minx = triangles[0][0][0]
                maxx = triangles[0][1][0]
                miny = triangles[0][0][1]
                maxy = triangles[0][1][1]

            for triangle in triangles:
                for point in triangle:
                    if point[0] < minx:
                        minx = point[0]
                        print("minx lowered to "+str(minx))
                    if point[0] > maxx:
                        maxx = point[0]
                        print("maxx raised to "+str(maxx))
                    if point[1] < miny:
                        miny = point[1]
                        print("miny lowered to "+str(miny))
                    if point[1] > maxy:
                        maxy = point[1]
                        print("maxy raised to "+str(maxy))
            
                
            #ax.set_xlim(-2000,11000)
            #ax.set_ylim(-2000,11000)

            for i in triangles:
                pts = i
                if highlightedges == True:
                    highlighter="b"
                else:
                    highlighter="k"
                 
                p = Polygon(pts, closed=False,facecolor="k", edgecolor=highlighter, linewidth=np.nextafter(0,1))
                ax = plt.gca()
                ax.add_patch(p)
                #fig.show()
        else:
            print("Skipping "+model[k]["name"]+" because it's got no faces.")
            
    print("Boundaries are:\n Min x:%.2f\nMax x:%.2f\nMin y:%.2f\nMax y:%.2f" % (minx,maxx,miny,maxy))
    ax.set_xlim(minx,maxx)
    ax.set_ylim(miny,maxy)
    
    end = time.time()

    #fig.show()
    print("Graph is %.2f by %.2f" % ((maxx-minx)/resolution,(maxy-miny)/resolution))

    fig.set_size_inches((maxx-minx)/resolution,(maxy-miny)/resolution)
    fig.savefig("somethingveryhightimetest.png", dpi=resolution)
    end = time.time()
    print("%.2f seconds" % (end - start))
    end = time.time()
    print("Line thickness was "+str(np.nextafter(0,1)))
    

def draw_vector():
    # SVG TRIALS
    dwg = svgwrite.Drawing('something.svg', debug=True)
    shapes = dwg.add(dwg.g(id='shapes', fill='black'))
    #shapes.add(dwg.polygon(points=[[200,300],[200,500],[500,300]], stroke_width=1,stroke="blue"))
    #dwg.save()
    print("aa!")


########################

    start = time.time()
    print("timer started")

    highlightedges = False
    
    model = json.load(open("./everything.json","r"))
    # DEMO MODE
    for k in range(1, len(model)):
        if model[k]["noFaces"] != 0:
            print("Drawing "+model[k]["name"])
            triangles = getTriangles(model,model[k]["name"])
            triangles = make2D(triangles)
            for i in triangles:
                pts = i
                if highlightedges == True:
                    highlighter="b"
                else:
                    highlighter="k"
                
                shapes.add(dwg.polygon(points=pts, stroke_width=1,stroke="blue"))
                
                #p = Polygon(pts, closed=False,facecolor="k", edgecolor=highlighter, linewidth=np.nextafter(0,1))
                #ax = plt.gca()
                #ax.add_patch(p)
                #fig.show()
        else:
            print("Skipping "+model[k]["name"]+" because it's got no faces.")
            
    dwg.save()
    end = time.time()

    #fig.show()
    
    #fig.savefig("somethingveryhightimetest.png", dpi=500)
    end = time.time()
    print("%.2f seconds" % (end - start))
    end = time.time()
    #print("Line thickness was "+str(np.nextafter(0,1)))

####################

if __name__ == "__main__":
    draw_plot()
    #draw_vector()
