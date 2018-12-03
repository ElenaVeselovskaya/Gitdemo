def calculation_of_deposit_profitability_in_rub(sum_of_deposit_in_rub, time_of_deposit, rate_of_deposit):
    """

    :param sum_of_deposit_in_rub:
    :param time_of_deposit:
    :param rate_of_deposit:
    :return:
    """

    # time_of_deposit = 365 # количество дней по вкладу
    # rate_of_deposit = 0.08 # коэффициент ставки вклада 8%
    number_of_days_in_year = 365  # количество дней в году
    total_sum_of_deposit_in_rub = round(sum_of_deposit_in_rub + (
            (sum_of_deposit_in_rub * rate_of_deposit * time_of_deposit) / number_of_days_in_year))
    return total_sum_of_deposit_in_rub



