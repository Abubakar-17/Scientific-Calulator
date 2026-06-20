import math

class ScientificCalculator:
    def evaluate(self, expression):
        try:
            allowed = {
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log10,
                "sqrt": math.sqrt,
                "pi": math.pi,
                "e": math.e
            }

            return eval(expression, {"__builtins__": None}, allowed)
        except:
            return "Error"
