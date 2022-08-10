import pytest

@pytest.mark.regression
def test_method1():
    assert 10 == 10

@pytest.mark.smoke
def test_method2():
    assert "Python" != "java"

@pytest.mark.sanity
def test_method3():
    assert 10+5 ==15

@pytest.mark.smoke
def test_method4():
    assert 10+5 !=20

@pytest.mark.sanity
def test_demo1():
    assert 25+5 !=30

@pytest.mark.smoke
def test_demo2():
    assert "Java" == 'Java'

