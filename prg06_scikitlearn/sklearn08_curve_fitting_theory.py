#!/usr/bin/env python3
# -*- coding: utf-8 -*-



'''
In Curve Fitting, we have all the data available to us at the time of fitting the curve. 
We want to fit the curve as best as we can.
Curve fitting is quite general ambiguously defined. It could refer to polynomial curve fitting. 
But some curve fitting can also fit functions like sin, 1/x, ln x.
Curve fitting can try to fit as accurate possible, in which case you could need up to a 
n-degree polynomial to fit n points, or curve fitting can have dimension control involved which
essentially avoids “over-fitting”.

Regression on the other hand, is pretty unambiguously defined from the statistics perspective. 
In a sense, regression is not a mathematics concept, it’s a statistics concept, while curve fitting 
is a mathematical concept. (think thermodynamics and combustion). Regression is curve fitting 
under context: the goal is to understand how one variable depends on another variable. 
Because the data is usually noisy and we usually want high-level understanding, 
dimension control is usually used to filter out the noise.

Curve fitting encompasses methods used in regression, and regression is not necessarily fitting a curve.

The relationship between variables has to be a function in the case of a regression 
dependent_variables = f(independent_variables)  
while in curve fitting it needs not be the case, e.g. fitting a circle, which cannot be expressed as a function

Curve fitting is one particular case in regression , where we take hypothesis 
in terms of polynomials (essentially polynomials are curves) .

'''
