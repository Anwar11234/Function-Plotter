import numpy as np
from sympy import symbols , parse_expr , lambdify

class FunctionPlotterController:
    def __init__(self , model , view):
        self.model = model 
        self.view = view
    
    def run_app(self):
        self.view.setup(self)
        self.view.start_app()
    
    def get_user_input(self):
        self.model.set_function_str(self.view.function_input.text())
        self.model.set_min_x(self.view.min_x_input.text())
        self.model.set_max_x(self.view.max_x_input.text())

    def plot(self):
        self.get_user_input()
        valid_input , error_message = self.is_valid_input()
        if not valid_input:
            self.view.show_error_window("Invalid Input" , error_message)
            return

        x = np.linspace(int(self.model.min_x ), int(self.model.max_x) + 1)
        x_sym = symbols('x')
        function_expr = self.model.function_str.replace('^' , '**')
        try:
            expr = parse_expr(function_expr)
        except:
            self.view.show_error_window("Invalid Input" , "Enter a valid function expression")


        f = lambdify(x_sym, expr, modules=['numpy'])

        # plotting constants
        if function_expr.isnumeric() or (function_expr[0] == '-' and function_expr[1:].isnumeric()):
            y = np.full(x.shape , int(function_expr))
        else:
            # Evaluate the function for x values
            y = f(x)
        
        self.view.show_plot(x , y , title="Plot of " + self.model.function_str)

    def is_valid_input(self):
        min_x , max_x , function_str = self.model.get_min_x() , self.model.get_max_x() , self.model.get_function_str()
        if not min_x:
            return False , "Please Enter a min x value"
        
        if not max_x:
            return False , "Please Enter a max x value"
        
        if not function_str:
            return False , "Please Enter a function to plot"

        if not (min_x.isnumeric() or (min_x[0] == '-' and min_x[1:].isnumeric())):
            return False , "Please Enter a numeric value for min x"
        
        if not (max_x.isnumeric() or (max_x[0] == '-' and max_x[1:].isnumeric())):
            return False , "Please Enter a numeric value for max x"
        
        if int(min_x) >= int(max_x):
            return False ,  "Min x value must be less than Max x value"
        
        if function_str.count("(") != function_str.count(")"):
            return False , "Unbalanced Parentheses"

        return True , ""