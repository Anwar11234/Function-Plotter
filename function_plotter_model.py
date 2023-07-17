class FunctionPlotterModel:
    def __init__(self):
        self.function_str = ""
        self.min_x = ""
        self.max_x = ""
    
    def get_function_str(self):
        return self.function_str
    
    def set_function_str(self , new_function_str):
        self.function_str = new_function_str

    def get_min_x(self):
        return self.min_x
    
    def set_min_x(self , new_min_x):
        self.min_x = new_min_x

    def get_max_x(self):
        return self.max_x
    
    def set_max_x(self , new_max_x):
        self.max_x = new_max_x