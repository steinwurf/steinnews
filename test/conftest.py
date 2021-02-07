
import glob

def pytest_generate_tests(metafunc):
    filelist = glob.glob('test/data/*.rst')
    metafunc.parametrize("file_in", filelist )

