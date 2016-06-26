"""Run all the notebooks

Provide the path to a subfolders/project or by default all be run.

Usage:
  run_all [<project>...] [--timeout=<seconds>]
  run_all (-h | --help)
  run_all --version

Options:
  <project>            The name(s) of the project subfolder(s)
  --timeout=<seconds>  Timeout before execution is interrupted [default: 600]
  -h --help            Show this screen
  --version            Show version
"""
from docopt import docopt

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError

from menpo.io.input.base import glob_with_suffix


PROJECTS_WITH_NOTEBOOKS = ['menpo', 'menpofit', 'menpo3d', 'menpowidgets']


def execute_and_write_notebook(path):
    print('Executing {}'.format(path.relative_to(path.parents[1])))

    with open(str(path)) as f:
        nb = nbformat.read(f, 4)

    try:
        parent = path.parent
        PREPROCESSOR.preprocess(nb, {'metadata': {'path': str(parent)}})

        with open(str(path), 'wt') as f:
            nbformat.write(nb, f)
    except CellExecutionError as e:
        print(e)


if __name__ == '__main__':
    args = docopt(__doc__, version='1.0')

    projects_to_build = args['<project>'] or PROJECTS_WITH_NOTEBOOKS
    timeout = int(args['--timeout'])

    PREPROCESSOR = ExecutePreprocessor(timeout=timeout, kernel_name='python3')

    for project in projects_to_build:
        notebook_names = glob_with_suffix('{}/**/*.ipynb'.format(project),
                                          {'.ipynb': None})

        print(' Executing {} notebooks '.format(project).center(80, '*'))
        for path in notebook_names:
            if path.parent.name != '.ipynb_checkpoints':
                execute_and_write_notebook(path)
