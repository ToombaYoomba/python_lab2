from contextlib import nullcontext as does_not_raise

import pytest 

from src.cat import cat
from src.constants import FuncError
from src.find_path import find_path

cd_desting_dir_path = find_path("text_testing")

@pytest.mark.parametrize(
        "ini, res, expectation",
        [
            (cat(cd_desting_dir_path, "cat1.txt"), open(find_path('cat1.txt'), 'r').read(), does_not_raise())
        ]
)
def test_ls_works(ini, res, expectation):
    with expectation:
        assert ini == res


@pytest.mark.parametrize(
        "ini, expectation",
        [
            ([cd_desting_dir_path, "dbd"], pytest.raises(FuncError)),
            ([cd_desting_dir_path, "text_dir"], pytest.raises(FuncError)),
            ([cd_desting_dir_path, ".."], pytest.raises(FuncError))
        ]
)
def test_ls_error(ini, expectation):
    with expectation:
        a = cat(ini[0], ini[1])
        assert 1 == 1