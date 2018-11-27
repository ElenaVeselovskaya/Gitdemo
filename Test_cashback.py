import pytest

from cashback import calculate_cashback_in_rub


@pytest.mark.parametrize('purchase_amount_in_rub, rate_of_cashback, expected',[
                         (6000, 0.05, 300),
                         (3800, 0.01, 38),
                         (5000, 0.3, 1500)
])

def test_calculate_cashback_in_rub(purchase_amount_in_rub, rate_of_cashback, expected):
    actual = calculate_cashback_in_rub(purchase_amount_in_rub, rate_of_cashback)
    assert expected == actual
