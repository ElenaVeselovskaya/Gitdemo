import pytest

from bank_credit import calculation_of_monthly_payment_in_rub


@pytest.mark.parametrize('sum_of_credit_in_rub, rate_of_credit, time_of_credit_in_month, expected', [
    (300000, 0.2, 36, 11149),
    (450000, 0.15, 18, 28073),
    (75000, 0.18, 12, 6876)

])
def test_calculation_of_monthly_payment_in_rub(sum_of_credit_in_rub, rate_of_credit, time_of_credit_in_month, expected):
    actual = calculation_of_monthly_payment_in_rub(sum_of_credit_in_rub, rate_of_credit, time_of_credit_in_month)
    assert expected == actual


