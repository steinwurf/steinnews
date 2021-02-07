from src.steinnews import write_next_version

import filecmp
import os

def test_increment_version(file_in):

    basename = os.path.basename(file_in)

    file_out = 'test/recordings/' + basename
    file_ref = 'test/recordings/' + basename + '.ref'

    write_next_version(file_in, file_out)
    assert filecmp.cmp(file_ref, file_out)

