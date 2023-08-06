import os.path
import pathlib
import filecmp

import pytest

import lifelib
import lifelib.projects.simplelife as simplelife
import lifelib.projects.nestedlife as nestedlife
import lifelib.projects.ifrs17sim as ifrs17sim

simplepath = simplelife.__path__[0]
nestedpath = nestedlife.__path__[0]
ifrs17simpath = ifrs17sim.__path__[0]

common_files = [('build_input.py', [simplepath, nestedpath, ifrs17simpath]),
                ('lifetable.py', [simplepath, nestedpath, ifrs17simpath]),
                ('policy.py', [simplepath, nestedpath, ifrs17simpath]),
                ('assumption.py', [simplepath, nestedpath, ifrs17simpath]),
                ('economic.py', [simplepath, nestedpath, ifrs17simpath]),
                ('projection.py', [simplepath, nestedpath, ifrs17simpath]),
                ('present_value.py', [simplepath, nestedpath, ifrs17simpath]),
                ('input.xlsm', [simplepath, nestedpath, ifrs17simpath])]


@pytest.mark.parametrize('filename, filepaths', common_files)
def test_filecomp(filename, filepaths):
    """Check equality of common files between simplelife and nestedlife"""

    for path1, path2 in zip(filepaths, filepaths[1:]):
        assert filecmp.cmp(os.path.join(path1, filename),
                           os.path.join(path2, filename))
