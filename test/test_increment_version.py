import pytest
import os
from steinnews import write_next_version
from steinnews.exceptions import NoChanges

def test_increment_version(file_in, recording_file, datarecorder, tmpdir):
    file_out = tmpdir.join("output.rst")
    write_next_version(file_in, file_out)

    with open(file_out, "r") as file:
        output = file.read()

    # suggestion: that the fixture library should attempt to create any 'intermediate' directories (it already handles creating the file part)
    recording_dir = os.path.dirname(recording_file)
    if not os.path.exists(recording_dir):
        os.makedirs(recording_dir)
    datarecorder.record_data(data=output, recording_file=recording_file)


def test_no_changes(no_changes_file_in):
    test_path = "testpath123"
    with pytest.raises(NoChanges):
        write_next_version(no_changes_file_in, test_path)
