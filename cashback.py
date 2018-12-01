def calculate_cashback_in_rub(purchase_amount_in_rub, rate_of_cashback):
    '''

    :param purchase_amount_in_rub:
    :param rate_of_cashback:
    :return:
    '''

    # rate_usual_cashback = 0.01  - коэффициет 1% кэшбэк
    # rate_increased_cashback = 0.05  - коэффициет 5% повышенный кэшбэк
    # rate_special_cashback = 0.3  - коэффициет 30% спецпредложение кэшбэк

    total_cashback_in_rub = purchase_amount_in_rub * rate_of_cashback
    return total_cashback_in_rub

print(calculate_cashback_in_rub(5000, 0.3))
