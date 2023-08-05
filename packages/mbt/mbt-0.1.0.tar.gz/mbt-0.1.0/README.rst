.. These are the Travis-CI and Coveralls badges for your repository. Replace
   your *github_repository* and uncomment these lines by removing the leading
   two dots.

.. image:: https://travis-ci.org/lparolari/micro-backup-tool.svg?branch=master
    :target: https://travis-ci.org/lparolari/micro-backup-tool

.. image:: https://coveralls.io/repos/github/lparolari/micro-backup-tool/badge.svg?branch=master
    :target: https://coveralls.io/github/lparolari/micro-backup-tool?branch=master


*Note:* this specs are a draft, might change.

=================
Micro Backup Tool
=================
Micro Backup Tool (shorted from here with *mbt*) is a light-weighted,
cross-platform and very simple project for backing-up files.

It is made with python to allows portability on different operative system,
and it's main goal is to make is work done without hand-waving.

The project is at very being, so for now the main implementation will be
rude and straight to the objective.


***************
Features
***************
- multiple dirctory trees backup
- common compressions
- logs keeping
- easy configuration and schedule
- files ignore with regular expression
- easy customization
- ready to go


***************
How it works
***************
*mbt* backup files and directories compressing it in a **.tar.gz** or
**.zip** file, setting the starting point equals to the launcher path.
If the directory option is specified *mbt* backups all the directories
listed in the option, excluding (if not explicitly specified) the
launcher path.

If something goes wrong?
========================
If something goes wrong the backup process **continues**, but the error
is written on logs (see logs section).
Unbacked-up list
^^^^^^^^^^^^^^^^^^^^^^^^
At the end of every backup a list containing "unbacked" up files is written,
and with the right option *mbt* automatically tries to backup again those
files (see options section). [TODO: define better]

Logs
===============
History logs
^^^^^^^^^^^^^^^
During the backup process logs are keeped and if something fails it
will be written on logs.
Error logs
^^^^^^^^^^^^^^^
If something goes wrong while backing up, the process continues but the
error log file will be written with error details.


***************
Guide
***************

Installation
===============
Coming soon...

Usage
===============
Define your own .mbtignore if needed to include or exclude certain files or
directories based on their names.

Coming soon...
