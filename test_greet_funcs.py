import pytest
from main import greeting


def test_greet():
    assert greeting("Nitesh") =="Hello,Nitesh"