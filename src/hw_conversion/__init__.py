import nbformat
from traitlets.config import Config
from nbconvert.exporters import PythonExporter
from hw_conversion.HWPreprocessor import HomeworkPreproccessor

def convert_hw(pattern, hw_file):
    ''' Function to convert a ipynb to a script keeping cells with pattern

    Parameters
    ----------
    pattern: str
        pattern to match keeping cells
    hw_file: str
        Homework jupyter notebook filename
    '''
    c = Config()
    c.HomeworkPreproccessor.pattern = pattern
    c.PythonExporter.preprocessors = [HomeworkPreproccessor]
    output, _ = PythonExporter(config=c).from_filename(hw_file)

    with open('homework.py', 'w') as f:
        f.write(output)
