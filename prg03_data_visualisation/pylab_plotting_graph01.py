#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

# data setup
x  = np.arange(-5.0, 20.0, 1)
y1 = (2.5*x)          - 200 # linear equation
y2 = (2.5*x * x)      - 200 # non linear equation
y3 = (0.06*x * x * x) + 310 # non linear equation
y4 = (9*x)            - 310 # linear equation


''' pylab simple line chart '''
import pylab as plb    
plb.plot(x, y1) # individual plot
plb.xlabel('x values')
plb.ylabel('y values')
plb.title('Pylab - line chart - single ')
plb.grid(True)
plb.show()


''' pylab simple and combined line chart '''
import pylab as plb    
plb.plot(x, y1) # individual plot
plb.plot(x, y2) # individual plot
plb.plot(x, y3) # individual plot
plb.xlabel('x values')
plb.ylabel('y values')
plb.title('Pylab - line chart - multiple')
plb.grid(True)
plb.show()


''' pylab subplot and line chart '''
subplot_row     = 3
subplot_col     = 1
subplot_fig_num = 1
plb.subplot(subplot_row, subplot_col, subplot_fig_num)
plb.plot(x, y1)
plb.xlabel('x values')
plb.ylabel('y values')
plb.title('First line chart')
plb.grid(True)

subplot_row     = 3
subplot_col     = 1
subplot_fig_num = 2
plb.subplot(subplot_row, subplot_col, subplot_fig_num)
plb.plot(x, y2)
plb.xlabel('x values')
plb.ylabel('y values')
plb.title('Second line chart')
plb.grid(True)

subplot_row     = 3
subplot_col     = 1
subplot_fig_num = 3
plb.subplot(subplot_row, subplot_col, subplot_fig_num)
plb.plot(x, y3)
plb.xlabel('x values')
plb.ylabel('y values')
plb.title('Third line chart')
plb.grid(True)
plb.show()



''' pylab styling the plot 
    color - r,g,b, m magenta, y yellow, c cyan, k, w white
    linewidth - 0 to 9.9
    linestyle - (: or -- or -)
'''
import pylab as plb
plb.plot(x, y1,color="r", linewidth=1.1, linestyle="-")
plb.plot(x, y2,color="g", linewidth=1.1, linestyle="--")
plb.plot(x, y3,color="b", linewidth=9.1, linestyle=":")
plb.xlabel('x values')
plb.ylabel('y values')
plb.title('Pylab - line chart - multiple')
plb.grid(False)
plb.show()


''' pylab bar chart 
    index - sequence of index of x axis values
    y axis values
    bar alignment style
    bar transparancy - 0.0 to 1.0
'''
x_subjects   = ('English', 'History', 'Maths', 'Science', 'Algebra', 'Geography')
index        = np.arange(len(x_subjects))
y_exam_score = [94,55,78,89,20,11]

plb.bar(index, 
        y_exam_score,
        align='center', 
        alpha=0.88)
plb.xticks(index, x_subjects)
plb.xlabel('Subject name')
plb.ylabel('Marks')
plb.title('Exam marks average')
plb.show()



''' scatter plot
    It is a type of plot that shows 
    the data as a collection of points
'''
plb.scatter(x,y1)
plb.show()


''' styling scatter plot '''
dot_colors = (1,0,0)
dot_area   = 12.3
plb.scatter(x,y1,
            s=dot_area, 
            c=dot_colors, 
            alpha=0.9)
plb.show()



''' to set x and y axis limits '''
plb.scatter(x,y1)
axis = plb.gca()
axis.set_xlim(-25,25)
axis.set_ylim(-300,20)
plb.show()



# http://mple.m-artwork.eu
# https://www.python-course.eu/matplotlib.php
