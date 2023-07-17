from function_plotter_controller import FunctionPlotterController
from function_plotter_model import FunctionPlotterModel
from function_plotter_view import FunctionPlotterView
from PySide2.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    controller = FunctionPlotterController(FunctionPlotterModel() , FunctionPlotterView(app))
    controller.run_app()