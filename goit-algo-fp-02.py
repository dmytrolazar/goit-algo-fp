import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_branch(depth, start_angle, skew_angle, size, ratio, x1, x2, y1, y2):
    plt.plot([x1, x2], [y1, y2], color = 'r')
    if depth > 1:
        draw_pythagoras_branch(depth-1, start_angle+skew_angle, skew_angle, size*ratio, ratio, x2, x2 + np.cos(start_angle+skew_angle)*size*ratio, y2, y2 + np.sin(start_angle+skew_angle)*size*ratio)
        draw_pythagoras_branch(depth-1, start_angle-skew_angle, skew_angle, size*ratio, ratio, x2, x2 + np.cos(start_angle-skew_angle)*size*ratio, y2, y2 + np.sin(start_angle-skew_angle)*size*ratio)

def draw_pythagoras_tree(depth, ratio=0.6, skew_angle=np.pi/4):
    draw_pythagoras_branch(depth, np.pi/2, skew_angle, 1, ratio, x1=0, x2=0, y1=0, y2=1)
    plt.gca().set_aspect('equal')
    plt.show()

depth = int(input("Вкажіть рівень рекурсії: "))
draw_pythagoras_tree(depth)
