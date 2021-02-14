steinnews
=========

Helper library to ease news.rst writing


Usages
--------------------------------

Import the module. There is (atm) only a single function named::

    write_next_version(file_in, file_out)

This takes an input file and an output file (that does not have to exist yet). These 2 files **can** be the same.
For example, if you would call it with a 'NEWS.rst' file you cond::
    
    write_next_version('NEWS.rst', 'NEWS.rst')

The result will be that any future changes in that NEWS.rst will be collected into a new version sections.


Building wheel and running tests
--------------------------------

To build the wheel and run the unit tests::

    python waf configure
    python waf build --run_tests



