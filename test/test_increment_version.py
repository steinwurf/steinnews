from src.steinnews import write_next_version

def test_increment_version():
    write_next_version('test/data/NEWS.rst', 'test/recordings/output.rst')
