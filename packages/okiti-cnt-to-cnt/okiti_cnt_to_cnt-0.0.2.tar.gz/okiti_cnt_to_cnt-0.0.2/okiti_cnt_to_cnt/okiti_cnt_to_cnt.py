import os
import struct
from shutil import copyfile


def okiti_cnt_to_cnt(file_name, new_file_name=None):

    if not _is_it_okiti_cnt(file_name):
        return False

    if new_file_name is not None:
        copyfile(file_name, new_file_name)
        file_to_modify = new_file_name
    else:
        file_to_modify = file_name

    with open(file_to_modify, 'r+b') as f:
        f.seek(0, os.SEEK_END)
        file_size = f.tell()

        f.seek(886, 0)
        event_offset, = struct.unpack('i', f.read(4))

        f.seek(370, 0)
        channel_n, = struct.unpack('H', f.read(2))

        f.seek(886, 0)
        f.write(file_size.to_bytes(4, byteorder='little'))

        f.seek(file_size)
        event_type = 1
        event_size = 0
        f.write(event_type.to_bytes(1, byteorder='little'))
        f.write(event_size.to_bytes(4, byteorder='little'))

        print(str((event_offset-file_size)/channel_n) + ' data points are missing!')

    return True


def _is_it_okiti_cnt(file_name):
    with open(file_name, 'r+b') as f:
        f.seek(0, os.SEEK_END)
        file_size = f.tell()
        f.seek(886, 0)
        event_offset, = struct.unpack('i', f.read(4))

    if file_size > event_offset:
        return False

    return True
