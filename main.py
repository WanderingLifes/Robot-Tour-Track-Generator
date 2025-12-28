import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random


#config
bottles = 3
gates = 3
walls = 3

rows, cols = 5, 4
vertical_midpoints = [
    [1, 0.5], [2, 0.5], [3, 0.5], 
    [1, 1.5], [2, 1.5], [3, 1.5], 
    [1, 2.5], [2, 2.5], [3, 2.5],
    [1, 3.5], [2, 3.5], [3, 3.5],
    [1, 4.5], [2, 4.5], [3, 4.5], 
]
horizontal_midpoints = [
    [0.5, 1], [0.5, 2], [0.5, 3], [0.5, 4],
    [1.5, 1], [1.5, 2], [1.5, 3], [1.5, 4],
    [2.5, 1], [2.5, 2], [2.5, 3], [2.5, 4],
    [3.5, 1], [3.5, 2], [3.5, 3], [3.5, 4],
]
grid_corners = [
    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
    [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
    [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
    [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],   
]
cell_centers = [
    [0.5, 0.5], [0.5, 1.5], [0.5, 2.5], [0.5, 3.5],[0.5, 4.5],
    [1.5, 0.5], [1.5, 1.5], [1.5, 2.5], [1.5, 3.5],[1.5, 4.5],
    [2.5, 0.5], [2.5, 1.5], [2.5, 2.5], [2.5, 3.5],[2.5, 4.5],
    [3.5, 0.5], [3.5, 1.5], [3.5, 2.5], [3.5, 3.5],[3.5, 4.5]
    
]
alphabet = [
    "A","B","C","D","E","F","G","H","I","J",
    "K","L","M","N","O","P","Q","R","S","T",
    "U","V","W","X","Y","Z"
]
edge_midpoints = [
    [0, 0.5], [0, 1.5], [0, 2.5], [0, 3.5],[0,4.5],
    [4, 0.5], [4, 1.5], [4, 2.5], [4, 3.5],[4,4.5],
    [0.5, 0], [1.5, 0], [2.5, 0], [3.5, 0],
    [0.5,5],  [1.5,5],  [2.5,5],  [3.5,5]
]



fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, cols)
ax.set_ylim(0, rows)
ax.set_aspect("equal")
ax.axis("off")

def add_gate(x, y, w, h,):
    ax.add_patch(patches.Rectangle(
        (x, y), w, h,
        linewidth=0,
        color="brown",
        zorder = 2
    ))

def add_wall(x, y, w, h,n):
    
    ax.add_patch(patches.Rectangle(
        (x, y), w, h,
        linewidth=3,
        fill = False,
        edgecolor = "green",
        zorder = 1  
    ))
    ax.text(x+0.4,y+0.4,
            alphabet[n], 
            horizontalalignment= 'center',
            fontsize = 20)
   
def add_point(x, y, color):
    ax.scatter(x, y, s=200, color=color, zorder=2)

for x in range(cols + 1):
    ax.plot([x, x], [0, rows], color="black", linewidth=1, zorder=0)

for y in range(rows + 1):
    ax.plot([0, cols], [y, y], color="black", linewidth=1,zorder=0)

for i in range(walls):
    HorV = random.randint(0,1)

    if HorV > 0:
        pos = random.choice(horizontal_midpoints)
        print(pos)
        horizontal_midpoints.remove(pos)
        print(horizontal_midpoints)
        x = pos[0]
        y = pos[1]
        add_gate(x -0.4,y - 0.05, 0.8, 0.1)   
        
    else:
        pos = random.choice(vertical_midpoints)
        vertical_midpoints.remove(pos)
        x = pos[0]
        y = pos[1]
        add_gate(x -0.05,y - 0.4, 0.1, 0.8)
        
    
bottlepos = vertical_midpoints + horizontal_midpoints

for i in range(bottles):
    pos = random.choice(bottlepos)
    x = pos[0]
    y = pos[1]
    print("x: ", x, "\ny: ",y ,"\n")
    add_point(x,y,"blue")
    bottlepos.remove(pos)
n = 0
for i in range(gates):
    pos = random.choice(grid_corners)
    x = pos[0]
    y = pos[1]
    
    add_wall(x,y,1,1,n)    
    grid_corners.remove(pos)
    n +=1

pos = random.choice(cell_centers)
add_point(pos[0],pos[1], 'red')
    
pos = random.choice(edge_midpoints)
add_point(pos[0],pos[1], 'green')


plt.show()