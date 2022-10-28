import pytest
import os
from steinnews import write_next_version
from steinnews.exceptions import InvalidChanges, NoChanges


def test_valid(file_in, recording_file, datarecorder, tmpdir):
    file_out = tmpdir.join("output.rst")
    write_next_version(file_in, file_out)

    with open(file_out, "r") as file:
        output = file.read()

    # suggestion: that the fixture library should attempt to create any 'intermediate' directories (it already handles creating the file part)
    recording_dir = os.path.dirname(recording_file)
    if not os.path.exists(recording_dir):
        os.makedirs(recording_dir)
    datarecorder.record_data(data=output, recording_file=recording_file)


def test_invalid(file_in, invalid_changes_file):
    invalid_changes = open(invalid_changes_file, "r").readlines()
    with pytest.raises(InvalidChanges) as excinfo:
        write_next_version(file_in, "testpath123")

    import logging

    logging.warning(excinfo.value)
    for line in invalid_changes:
        logging.warning(line)
    assert all(change.rstrip() in str(excinfo.value) for change in invalid_changes)


def test_no_changes(file_in):
    with pytest.raises(NoChanges):
        write_next_version(file_in, "testpath123")
