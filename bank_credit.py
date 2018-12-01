def calculation_of_monthly_payment_in_rub(sum_of_credit_in_rub, rate_of_credit, time_of_credit_in_month):
    """
    >>> calculation_of_monthly_payment_in_rub(300000, 0.2, 36)
    11149.075007922165

    :param sum_of_credit_in_rub:
    :return:
    """

    # rate_of_credit = 20 / 100  # расчет коэффициента, где 20 - ставка в %
    number_of_months_per_year = 12  # количество месяцев в году
    interest_rate_per_month = rate_of_credit / number_of_months_per_year  # процентная ставка в месяц

    total_monthly_payment_of_credit_in_rub = round(sum_of_credit_in_rub * (
            interest_rate_per_month / (
            1 - (1 + interest_rate_per_month) ** - time_of_credit_in_month)))  # расчет ежемесячного платежа
    return total_monthly_payment_of_credit_in_rub


print(calculation_of_monthly_payment_in_rub(75000, 0.18, 12))


