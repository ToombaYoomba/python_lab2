from contextlib import nullcontext as does_not_raise

import pytest 

from src.cp import cp
from src.constants import FuncError
from src.find_path import find_path

cp_desting_dir_path = find_path("cp_testing")


@pytest.mark.parametrize(
        "ini, expectation",
        [
            ([cp_desting_dir_path, ["cp1.txt", "dbd/dbd"]], pytest.raises(Exception)),
            ([cp_desting_dir_path, ["cp_dir2", "cp_dir1"]], pytest.raises(FuncError)),
            ([cp_desting_dir_path, ["cp_dir2", "cp1.txt"]], pytest.raises(FuncError)),
        ]
)
def test_ls_error(ini, expectation):
    with expectation:
        a = cp(ini[0], ini[1])
        assert 1 == 1