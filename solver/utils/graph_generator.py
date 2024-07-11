import matplotlib.pyplot as plt
import numpy as np
import re
from matplotlib.font_manager import FontProperties

def parse_equation(equation):
    equation = equation.replace(" ", "")
    match = re.match(r"([y|f\(x\)]?=)?([\+\-]?\d*\.?\d*)?([x|sin|cos|tan]*)([\+\-]?\d*\.?\d*)?", equation)
    if match:
        groups = match.groups()
        left_side = groups[0]
        coefficient = groups[1]
        variable = groups[2]
        constant = groups[3]
        return left_side, coefficient, variable, constant
    return None, None, None, None

def generate_graph(equation, output_path, font_path="NanumPenScript-Regular.ttf"):
    left_side, coefficient, variable, constant = parse_equation(equation)
    
    try:
        font_properties = FontProperties(fname=font_path, size=14)

        if variable == "x":
            # Linear equation y = mx + b
            m = float(coefficient) if coefficient else 1.0
            b = float(constant) if constant else 0.0
            x = np.linspace(-10, 10, 400)
            y = m * x + b
            plt.figure(figsize=(5, 5))
            plt.plot(x, y, label=equation)
        
        elif variable == "x^2":
            # Quadratic equation y = ax^2 + bx + c
            a = float(coefficient) if coefficient else 1.0
            b = float(constant) if constant else 0.0
            c = 0.0  # For simplicity, assume c = 0
            x = np.linspace(-10, 10, 400)
            y = a * x**2 + b * x + c
            plt.figure(figsize=(5, 5))
            plt.plot(x, y, label=equation)
        
        elif variable in ["sin", "cos", "tan"]:
            # Trigonometric functions
            x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
            if variable == "sin":
                y = np.sin(x)
            elif variable == "cos":
                y = np.cos(x)
            elif variable == "tan":
                y = np.tan(x)
            plt.figure(figsize=(5, 5))
            plt.plot(x, y, label=equation)
            plt.ylim(-2, 2)  # Limit y-axis for better visualization

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend(prop=font_properties)
        plt.title(equation, fontproperties=font_properties)
        plt.xlabel('x', fontproperties=font_properties)
        plt.ylabel('y', fontproperties=font_properties)
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()
    except Exception as e:
        print(f"Error generating graph for equation '{equation}': {e}")
