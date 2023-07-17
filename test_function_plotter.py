import pytest
from unittest.mock import patch
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import Qt
from function_plotter_model import FunctionPlotterModel
from function_plotter_view import FunctionPlotterView
from function_plotter_controller import FunctionPlotterController


@pytest.fixture
def app(qtbot):
    model = FunctionPlotterModel()
    app = FunctionPlotterView(qtbot)
    controller = FunctionPlotterController(model, app)
    app.setup(controller)
    return controller


def test_valid_input(app, qtbot):
    app.view.function_input.setText("2*x + 5")
    app.view.min_x_input.setText("0")
    app.view.max_x_input.setText("10")
    
    qtbot.mouseClick(app.view.plot_button, Qt.LeftButton)
    
    # Assert that the plot is displayed correctly
    assert len(app.view.figure.axes) == 1
    assert app.view.figure.axes[0].get_title() == "Plot of 2*x + 5"

def test_trigonometric_functions(app , qtbot):
    app.view.function_input.setText("sin(x)")
    app.view.min_x_input.setText("0")
    app.view.max_x_input.setText("10")
    
    qtbot.mouseClick(app.view.plot_button, Qt.LeftButton)
    
    # Assert that the plot is displayed correctly
    assert len(app.view.figure.axes) == 1
    assert app.view.figure.axes[0].get_title() == "Plot of sin(x)"

def test_logarithmic_functions(app , qtbot):
    app.view.function_input.setText("log(x)")
    app.view.min_x_input.setText("5")
    app.view.max_x_input.setText("15")
    
    qtbot.mouseClick(app.view.plot_button, Qt.LeftButton)
    
    # Assert that the plot is displayed correctly
    assert len(app.view.figure.axes) == 1
    assert app.view.figure.axes[0].get_title() == "Plot of log(x)"

def test_exponential_functions(app , qtbot):
    app.view.function_input.setText("exp(2*x)")
    app.view.min_x_input.setText("0")
    app.view.max_x_input.setText("100")
    
    qtbot.mouseClick(app.view.plot_button, Qt.LeftButton)
    
    # Assert that the plot is displayed correctly
    assert len(app.view.figure.axes) == 1
    assert app.view.figure.axes[0].get_title() == "Plot of exp(2*x)"

def test_constant_functions(app , qtbot):
    app.view.function_input.setText("10")
    app.view.min_x_input.setText("-100")
    app.view.max_x_input.setText("100")
    
    qtbot.mouseClick(app.view.plot_button, Qt.LeftButton)
    
    # Assert that the plot is displayed correctly
    assert len(app.view.figure.axes) == 1
    assert app.view.figure.axes[0].get_title() == "Plot of 10"

def test_min_x_larger_than_max_x(app, qtbot):
    app.view.function_input.setText("x**2")
    app.view.min_x_input.setText("10")
    app.view.max_x_input.setText("0")
    
    with patch.object(QMessageBox, 'critical') as mock_critical_message_box:
        qtbot.mouseClick(app.view.plot_button, Qt.LeftButton)
        
        # Assert that QMessageBox.critical was called
        mock_critical_message_box.assert_called()
        assert mock_critical_message_box.call_args[0][2] == "Min x value must be less than Max x value"

def test_no_function_str(app , qtbot):
    app.view.function_input.setText("")
    app.view.min_x_input.setText("10")
    app.view.max_x_input.setText("0")

    with patch.object(QMessageBox , 'critical') as mock_critical_message_box:
        qtbot.mouseClick(app.view.plot_button , Qt.LeftButton)

        mock_critical_message_box.assert_called()
        assert mock_critical_message_box.call_args[0][2] == "Please Enter a function to plot"

def test_no_min_x(app , qtbot):
    app.view.function_input.setText("x**2 + 2*x + 1")
    app.view.min_x_input.setText("")
    app.view.max_x_input.setText("100")
    
    with patch.object(QMessageBox, 'critical') as mock_critical_message_box:
        qtbot.mouseClick(app.view.plot_button, Qt.LeftButton)
        
        # Assert that QMessageBox.critical was called
        mock_critical_message_box.assert_called()
        assert mock_critical_message_box.call_args[0][2] == "Please Enter a min x value"

def test_no_max_x(app , qtbot):
    app.view.function_input.setText("x**3")
    app.view.min_x_input.setText("-100")
    app.view.max_x_input.setText("")
    
    with patch.object(QMessageBox, 'critical') as mock_critical_message_box:
        qtbot.mouseClick(app.view.plot_button, Qt.LeftButton)
        
        # Assert that QMessageBox.critical was called
        mock_critical_message_box.assert_called()
        assert mock_critical_message_box.call_args[0][2] == "Please Enter a max x value"

def test_non_numeric_min_x(app , qtbot):
    app.view.function_input.setText("x**3 + sin(x)")
    app.view.min_x_input.setText("a")
    app.view.max_x_input.setText("200")
    
    with patch.object(QMessageBox, 'critical') as mock_critical_message_box:
        qtbot.mouseClick(app.view.plot_button, Qt.LeftButton)
        
        # Assert that QMessageBox.critical was called
        mock_critical_message_box.assert_called()
        assert mock_critical_message_box.call_args[0][2] == "Please Enter a numeric value for min x" 

def test_non_numeric_max_x(app , qtbot):
    app.view.function_input.setText("log(x)")
    app.view.min_x_input.setText("10")
    app.view.max_x_input.setText("b")
    
    with patch.object(QMessageBox, 'critical') as mock_critical_message_box:
        qtbot.mouseClick(app.view.plot_button, Qt.LeftButton)
        
        # Assert that QMessageBox.critical was called
        mock_critical_message_box.assert_called()
        assert mock_critical_message_box.call_args[0][2] == "Please Enter a numeric value for max x" 

def test_unbalanced_parentheses(app, qtbot):
    app.view.function_input.setText("sin(x")
    app.view.min_x_input.setText("0")
    app.view.max_x_input.setText("10")
    
    with patch.object(QMessageBox, 'critical') as mock_critical:
        qtbot.mouseClick(app.view.plot_button, Qt.LeftButton)
        
        # Assert that QMessageBox.critical was called
        mock_critical.assert_called()
        assert mock_critical.call_args[0][2] == "Unbalanced Parentheses"