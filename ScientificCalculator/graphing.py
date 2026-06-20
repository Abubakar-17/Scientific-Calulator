import numpy as np
import matplotlib.pyplot as plt
import math

class GraphPlotter:
    def plot(self, expression):
        x = np.linspace(-10, 10, 400)

        allowed = {
            "sin": np.sin,
            "cos": np.cos,
            "tan": np.tan,
            "log": np.log10,
            "sqrt": np.sqrt,
            "x": x,
            "pi": math.pi,
            "e": math.e
        }

        y = eval(expression, {"__builtins__": None}, allowed)

        plt.figure()
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"y = {expression}")
        plt.grid(True)
        plt.show()
