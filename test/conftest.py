
import glob

from os.path import dirname, abspath, basename

def pytest_generate_tests(metafunc):
    testdir = dirname(abspath(__file__))
    datafilelist = glob.glob(testdir + '/data/*.rst')
    arguments = [(datafile, testdir + '/recording/' + metafunc.function.__name__ + '/' + basename(datafile) + '.txt') for datafile in datafilelist]
    metafunc.parametrize("file_in, recording_file", arguments)

