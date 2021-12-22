# latest_local_blast_installer_linux_fedora
This script allows you to easily install local blast on your fedora (linux) device.

This script is still work in progress!
in the future it will support functionality to install all the databases available on https://ftp.ncbi.nlm.nih.gov/blast/db/.
For now it is just the swissprot database.

## How to use:
Make sure you have the latest python version installed on your linux device,
and simply run the command: 
$ python3 install_blast_0.9.1.py

Modules needed are:
- os
- subprocess

If you want the latest version you need to change the blast version manually in the script corresponding to https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/
