import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "Number Divider.py"
spec = importlib.util.spec_from_file_location("number_divider", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)
precise_round = module.precise_round


def test_zero():
    assert precise_round(0.0) == 0


def test_integer_float():
    assert precise_round(5.0) == 5.0


def test_single_decimal():
    assert precise_round(2.5) == 2.0


def test_multiple_decimals():
    assert precise_round(12.3456) == 12.346


def test_small_positive_not_collapse():
    assert precise_round(9e-12) == 1e-10


def test_small_negative_not_collapse():
    assert precise_round(-7e-12) == -1e-10
