import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_octagonal_inductor(turns):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    divider = 8
    for turn in range(turns):
        radius = 1 - (turn / turns)  # Adjust radius based on turn position
        orientation = np.pi / divider if (turn % 2 == 0) else -np.pi / divider  # Rotate alternate turns
        octagon = patches.RegularPolygon((0, 0), numVertices=8, radius=radius, orientation=orientation, edgecolor='black', facecolor='none')
        ax.add_patch(octagon)

    plt.show()



def draw_octagonal_inductorMine(turns, spacing=10):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    width, height = fig.get_size_inches()
    centerX = width / 2
    centerY = height / 2

    for turn in range(turns):
        radius = ((turns - turn)*spacing) * width / 2
        radiusY = ((turns - turn)*spacing) * height) / 2
        rotation = np.pi / 8
        if turn % 2 != 0:
            rotation = -rotation

        xPoints = np.zeros(9)
        yPoints = np.zeros(9)
        for i in range(9):
            angle = i * np.pi / 4 + rotation
            xPoints[i] = centerX + radius * np.cos(angle)
            yPoints[i] = centerY + radiusY * np.sin(angle)

        ax.plot(xPoints, yPoints, color='black')

    plt.show()


def draw_octagonal_inductor2(turns, spacing):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    width, height = fig.get_size_inches()
    centerX = width / 2
    centerY = height / 2
    original_x = np.zeros(9)
    original_y = np.zeros(9)
    for turn in range(turns):
        radius = (turns - turn) * (spacing) * width / (2 * turns)
        radius = (turns - turn) * (spacing) * height / (2 * turns)
        rotation = np.pi / 8
       # if turn % 2 != 0:
            #rotation = -rotation

        xPoints = np.zeros(9)
        yPoints = np.zeros(9)
        if ( turn > -1  ):
            for i in range(9):
                angle = i * np.pi / 4 + rotation
           
                xPoints[i] = centerX + radius * np.cos(angle)
                
                yPoints[i] = centerY + radiusY * np.sin(angle)
            print(xPoints)
            print(yPoints)
            print("##################")

            original_x = xPoints
            original_y = yPoints
        else:
            for i in range(9):
                if i == 0 or i >= 7:
                    xPoints[i] = original_x[i] + spacing*turn
                    yPoints[i] = original_y[i]
                elif i == 3 or i == 4:
                    xPoints[i] = original_x[i] - spacing*turn
                    yPoints[i] = original_y[i]
                elif i == 1 or i == 2:
                    yPoints[i] = original_y[i] + spacing*turn
                    xPoints[i] = original_x[i]
                else:
                    yPoints[i] = original_y[i] - spacing*turn
                    xPoints[i] = original_x[i]
                
        ax.plot(xPoints, yPoints, '*r')
        ax.plot(xPoints, yPoints, 'b')
        

    plt.show()



draw_octagonal_inductor2(3,1)  # Generate a 3-turn octagonal inductor
