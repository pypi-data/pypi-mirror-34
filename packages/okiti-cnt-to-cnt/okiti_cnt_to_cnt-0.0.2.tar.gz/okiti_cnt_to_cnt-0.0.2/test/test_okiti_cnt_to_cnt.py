import os

from mne.io.cnt import read_raw_cnt

from okiti_cnt_to_cnt.okiti_cnt_to_cnt import okiti_cnt_to_cnt
from okiti_cnt_to_cnt.okiti_cnt_to_cnt import _is_it_okiti_cnt


def test_okito_cnt_to_cnt__not_okiti_cnt_input():
    # given
    file_name = "./data/mne_compatible.cnt"

    expected_return_value = False

    # when
    actual_return_value = okiti_cnt_to_cnt(file_name)

    # that
    assert actual_return_value == expected_return_value


def test_okito_cnt_to_cnt__preserve_original_cnt_file():
    # given
    file_name = "./data/okiti_cnt.cnt"
    new_file_name = "./data/temp.cnt"

    expected_flag = True
    expected_test_can_run_till_there = True

    # when
    actual_flag = okiti_cnt_to_cnt(file_name, new_file_name)
    raw_cnt = read_raw_cnt(new_file_name, montage=None)
    print(raw_cnt.get_data())
    os.remove(new_file_name)

    # that
    assert actual_flag == expected_flag
    assert expected_test_can_run_till_there


def test_is_it_okiti_cnt__false():
    # given
    file_name = "./data/mne_compatible.cnt"

    expected_flag = False

    # when
    actual_flag = _is_it_okiti_cnt(file_name)

    # that
    assert actual_flag == expected_flag


def test_is_it_okiti_cnt__true():
    # given
    file_name = "./data/okiti_cnt.cnt"

    expected_flag = True

    # when
    actual_flag = _is_it_okiti_cnt(file_name)

    # that
    assert actual_flag == expected_flag
