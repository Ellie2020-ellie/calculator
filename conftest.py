import pytest
import yaml

from pythoncode.calculator import Calculator

with open('./datas.yml') as f:
    datas = yaml.safe_load(f)
    add_data = datas["add_datas"]
    sub_data = datas["sub_datas"]
    mul_data = datas["mul_datas"]
    div_data = datas["div_datas"]


@pytest.fixture(scope="module", params=add_data)
def get_add_datas(request):
    return request.param


@pytest.fixture(scope="module", params=sub_data)
def get_sub_data(request):
    return request.param


@pytest.fixture(scope="module", params=mul_data)
def get_mul_data(request):
    return request.param


@pytest.fixture(scope="module", params=div_data)
def get_div_data(request):
    return request.param


@pytest.fixture(scope="module")
def get_calc():
    calc = Calculator()
    return calc


@pytest.fixture(scope="session")
def calc_info():
    print("开始计算")
    yield
    print("计算结束")
