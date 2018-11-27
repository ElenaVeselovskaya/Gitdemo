import pytest

from Bank_deposit import calculation_of_deposit_profitability_in_rub


@pytest.mark.parametrize('sum_of_deposit_in_rub, time_of_deposit, rate_of_deposit, expected',[
    (700000, 365, 0.08, 756000),
    (75000, 31, 0.12, 75764),
    (800000, 240, 0.1, 852603)
])
def test_calculation_of_deposit_profitability_in_rub(sum_of_deposit_in_rub, time_of_deposit, rate_of_deposit, expected):
    actual = calculation_of_deposit_profitability_in_rub(sum_of_deposit_in_rub, time_of_deposit, rate_of_deposit)
    assert expected == actual




