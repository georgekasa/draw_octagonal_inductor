#import matplotlib.pyplot as plt
#import matplotlib.patches as patches
import numpy as np
import argparse



def draw_octagonal_inductor2(turns, spacing, width, height):
    #fig, ax = plt.subplots()
    #ax.set_aspect('equal')


    width = width
    height = height
    centerX = width / 2
    centerY = height / 2
    original_x = np.zeros(9)
    original_y = np.zeros(9)
    for turn in range(turns):
        radius = (turns - turn) * (spacing) * width/ (2 * turns)
	radiusY = (turns - turn) * (spacing) * height / (2 * turns)
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
            #print("##################")

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
	    print(xPoints)
            print(yPoints)
            print("##################")
                
        #ax.plot(xPoints, yPoints, '*r')
        #ax.plot(xPoints, yPoints, 'b')
        

    #plt.show()




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate an octagonal inductor.')
    parser.add_argument('--turns', type=int, help='Number of turns', default=1)
    parser.add_argument('--spacing', type=float, help='Spacing value', default=1)
    parser.add_argument('--width', type=float, help='Width of the inductor', default=120)
    parser.add_argument('--height', type=float, help='Height of the inductor', default=110)
    args = parser.parse_args()

    draw_octagonal_inductor2(args.turns, args.spacing, args.width, args.height)

#python spiralInd.py --turns 3 --spacing 2 --width 150 --height 130


