# okiti_cnt_to_cnt

Modify OKITI created cnt files to be readable by mne-python package.


OKITI - Országos Klinikai Idegtudományi IntézetOrszágos Klinikai Idegtudományi Intézet

mne-python - https://github.com/mne-tools/mne-python


## How to use
The function modify or create a new cnt file.

It returns only a flag which shows it did anything or not.

If you don't need the original cnt file just give your cnt file name to the function.

If you want to preserve the original file specify the _new_file_name_ argument as well.

If the input is a valid cnt file the function will return false value.


## Description
In OKITI the creation of cnt files done by a self-made Matlab script from trc files. This script is good enough to create cnt files which can be read by Matlab but they are not readable by mne-python package. We have to modify the cnt file to read by mna-python package.


**Modifications:**
1. Modify the event offset value. In OKITI cnt the event offset length is wrongly defined in the cnt file setup.
2. Add event type and event number to the end of the file. These are expected by mne-python but there are not in the OKITI cnt file.

