'''
A package for verifying source code.
'''

from pedal.report import MAIN_REPORT, Feedback
import ast

NAME = 'Source'
SHORT_DESCRIPTION = "Verifies source code and attaches it to the report"
DESCRIPTION = '''
'''
REQUIRES = []
OPTIONALS = []

__all__ = ['NAME', 'DESCRIPTION', 'SHORT_DESCRIPTION',
           'REQUIRES', 'OPTIONALS',
           'set_source']

def set_source(code, filename='__main__.py', report=None):
    if report is None:
        report = MAIN_REPORT
    report['source']['code'] = code
    report['source']['filename'] = filename
    _check_issues(code, report)

def _check_issues(code, report):
    if code.strip() == '':
        report.attach('blank_source', category='Syntax', tool=NAME,
                      mistakes="Source code file is blank.")
    try:
        parsed = ast.parse(code)
    except Exception as e:
        report.attach('syntax_error', category='Syntax', tool=NAME,
                      mistakes={'message': "Failed to parse source code.",
                                'error': e})
    