import pytest
from io import StringIO
from contextlib import redirect_stdout
from q8 import lerCaractere, elevarAoCubo

def test_elevarAoCubo():
    assert elevarAoCubo(2) == 8
    assert elevarAoCubo(-3) == -27
    assert elevarAoCubo(0) == 0
    assert elevarAoCubo(1.5) == 3.375

@pytest.mark.parametrize("inputs, expected", [
    (["s"], "S"),
    (["n"], "N"),
    (["S"], "S"),
    (["N"], "N"),
    (["x", "s"], "S"),
    ([" ", "N"], "N"),
])
def test_lerCaractere(inputs, expected):
    input_iter = iter(inputs)
    def mock_input(prompt):
        return next(input_iter)

    f = StringIO()
    with redirect_stdout(f):
        result = lerCaractere(input_fn=mock_input)

    assert result == expected
