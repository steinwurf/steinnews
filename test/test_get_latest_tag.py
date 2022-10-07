import pytest
import os
from steinnews import get_latest_tag
from steinnews.exceptions import NoChanges

def test_get_latest_tag(file_in, expected_version):
    with open(file_in, "r") as file:
        content = file.read()
        version = get_latest_tag(content)
        assert version == expected_version