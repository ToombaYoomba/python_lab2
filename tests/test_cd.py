from contextlib import nullcontext as does_not_raise

import pytest 

from src.cd import cd
from src.constants import FuncError
from src.find_path import find_path

cd_desting_dir_path = find_path("cd_testing")

@pytest.mark.parametrize(
        "ini, res, expectation",
        [
            (cd(cd_desting_dir_path, "dir1"), find_path("dir1"), does_not_raise())
        ]
)
def test_ls_works(ini, res, expectation):
    with expectation:
        assert ini == res


@pytest.mark.parametrize(
        "ini, expectation",
        [
            ([cd_desting_dir_path, "dbd"], pytest.raises(FuncError)),
            ([cd_desting_dir_path, "cd2.txt"], pytest.raises(FuncError))
        ]
)
def test_ls_error(ini, expectation):
    with expectation:
        a = cd(ini[0], ini[1])
        assert 1 == 1