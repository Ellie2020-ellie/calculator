import pytest


class TestCalc:

    @pytest.mark.run(order=1, )
    def test_add(self, get_calc, get_add_datas, calc_info):
        # 调用add函数,返回的结果保存在result里面
        result = get_calc.add(get_add_datas[0], get_add_datas[1])
        # 判断result结果是否等于期望的值
        assert result == get_add_datas[2]

    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_div_data):
        result = get_calc.div(get_div_data[0], get_div_data[1])
        assert result == get_div_data[2]

    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_sub_data):
        result = get_calc.sub(get_sub_data[0], get_sub_data[1])
        assert result == get_sub_data[2]

    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_mul_data):
        result = get_calc.mul(get_mul_data[0], get_mul_data[1])
        assert result == get_mul_data[2]

#     pytest --alluredir=./result test_cal.py
#     allure serve ./result
