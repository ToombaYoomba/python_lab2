from contextlib import nullcontext as does_not_raise

import pytest 

from src.ls import ls
from src.constants import FuncError
from src.find_path import find_path

ls_desting_dir_path = find_path("text_testing")

@pytest.mark.parametrize(
        "ini, res, expectation",
        [
            (ls(ls_desting_dir_path, None), ["cat1.txt", "cat2.txt", "cat3.txt", "text_dir"], does_not_raise())
        ]
)
def test_ls_works(ini, res, expectation):
    with expectation:
        assert ini == res


@pytest.mark.parametrize(
        "ini, expectation",
        [
            ([ls_desting_dir_path, ["dbd"]], pytest.raises(FuncError)),
            ([ls_desting_dir_path, ["cat1.txt"]], pytest.raises(FuncError))
        ]
)
def test_ls_error(ini, expectation):
    with expectation:
        a = ls(ini[0], ini[1])
        assert 1 == 1


