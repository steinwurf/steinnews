import glob
import os


def pytest_generate_tests(metafunc):
    testdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test")

    if metafunc.function.__name__ == "test_increment_version":
        datafilelist = glob.glob(os.path.join(testdir, "data") + "/*.rst")
        arguments = [
            (
                datafile,
                os.path.join(
                    testdir,
                    "recording",
                    metafunc.function.__name__,
                    os.path.basename(datafile) + ".txt",
                ),
            )
            for datafile in datafilelist
        ]
        metafunc.parametrize("file_in, recording_file", arguments)

    elif metafunc.function.__name__ == "test_no_changes":
        no_changes_datafilelist = glob.glob(
            os.path.join(testdir, "data", "no_changes") + "/*.rst"
        )
        metafunc.parametrize("no_changes_file_in", no_changes_datafilelist)
