from sympy import *

def calculate_expression(expression):
    return float(eval(parse_expr(expression)))