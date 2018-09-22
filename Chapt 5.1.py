def main():
    month_balance = monthly()
    month_total = monthly()
    yearly(month_balance)
    yearly_total = yearly(month_balance)
    m_name = monthly_balance(monthly())
    y_name = yearly_total(monthly_balance())
def monthly():
        month = print(int(input("car loan month? ")))
        car_month = print(int(input("insurance? ")))
        car_gas = print(int(input("Gas? ")))
        car_main = print(int(input("Maintanance? ")))

        monthly_total = format(str(month) + str(car_gas) + str(car_main) + str(car_month))

        return monthly_total

def yearly (monthly_balance):
    yearly_add = monthly_balance * 12
    return yearly_add

def monthly_balance (monthly):
    print(' Your monthly costs would be ' + str(monthly_balance(monthly)))
    return monthly_balance (monthly())
def yearly_total (month_balance):
      print(' your, yearly costs would be ' + str(yearly_total()))
      return yearly_total
main()
