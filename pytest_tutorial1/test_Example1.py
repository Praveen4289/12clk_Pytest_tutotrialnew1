import pytest

@pytest.mark.smoke
def test_add(a=25,b=25):
    c=a+b
    print("Add result")
    assert c == 50

@pytest.mark.regression
def test_sub(a=50,b=40):
    c=a-b
    print("Sub result")
    assert c==10

@pytest.mark.smoke
def test_mul(a=25,b=4):
    c=a*b
    print("mul result")
    assert c==100

@pytest.mark.regression
def test_mul1(subname='python'):
    assert subname == "Python"

@pytest.mark.regression
def test_mul2():
    st="python"
    assert st.upper()=="PYTHON"