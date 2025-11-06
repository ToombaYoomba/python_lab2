from contextlib import nullcontext as does_not_raise

import pytest 

from src.rm import rm
from src.constants import FuncError
from src.find_path import find_path

cp_desting_dir_path = find_path("cp_testing")


@pytest.mark.parametrize(
        "ini, expectation",
        [
            ([cp_desting_dir_path, ["cp_dir2"]], pytest.raises(FuncError)),
            ([find_path("cp_dir2"), [cp_desting_dir_path]], pytest.raises(FuncError)),
        ]
)
def test_ls_error(ini, expectation):
    with expectation:
        rm(ini[0], ini[1])
        assert 1 == 1