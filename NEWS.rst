News for steinnews
==================

This file lists the major changes between versions. For a more detailed list of
every change, see the Git log.

Latest
------
* Minor: Added an extra validation step to handle cases where the user has forgotten to add ``*`` sign in front of the change level
* Minor: Restructured the way tests are parametrised and added more tests
* Patch: ``get_latest_tag()`` now returns ``String`` instead of ``Tuple``

1.4.0
-----
* Minor: ```Write_next_version``` now returns the new version number.

1.3.0
-----
* Minor: Test for get_latest_tag method.

1.2.0
-----
* Minor: Move getting the latest tag to a separate function.

1.1.0
-----
* Minor: Now raising custom ``NoChanges`` exception when latest section is empty

1.0.0
-----
* Major: Tool has been created

