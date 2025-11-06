from contextlib import nullcontext as does_not_raise

import pytest 

from src.untar import untar
from src.constants import FuncError
from src.find_path import find_path

cp_testing_dir_path = find_path("text_testing")

@pytest.mark.parametrize(
        "ini, expectation",
        [
            ([cp_testing_dir_path, ["none.tar.gz"]], pytest.raises(FuncError)),
        ]
)
def test_ls_error(ini, expectation):
    with expectation:
        untar(ini[0], ini[1])
        assert 1 == 1