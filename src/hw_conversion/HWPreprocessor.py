'''
Module containing a preprocessor that keeps cells if they match given
expression.
'''

# Author: Juan M. Barrios <j.m.barrios@gmail.com>

import re
from typing import Pattern
from traitlets import Unicode
from nbconvert.preprocessors import Preprocessor


class HomeworkPreproccessor(Preprocessor):
    '''Keeps cells form a notebook that match a regular expression'''
    pattern = Unicode().tag(config=True)
    
    def check_conditions(self, cell):
        '''Checks that a cell matches the pattern.
        
        Returns: Boolean.
        True means cell should be kept.
        '''
        regexp_compiled = re.compile(self.pattern)
    
        return regexp_compiled.match(cell.source)

    def preprocess(self, nb, resources):
        '''Preprocessing to apply to each notebook.'''
        if not self.pattern:
            return nb, resources

        nb.cells = [cell for cell in nb.cells if self.check_conditions(cell)]

        return nb, resources