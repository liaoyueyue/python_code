""""
6.	设计一个简单的购房商贷月供计算器类，按照以下公式计算总利息和每月还款金额：总利息=贷款金额*利率
每月还款金额 = （贷款金额+总利息）/贷款年限
贷款年限不同利率也不同，这里规定只有如下表所示的3种年限、利率。
年限	           利率
3年（36个月）	   6.03%
5年（60个月）	   6.12%
20年（240个月）  4.39%
"""

class MortgageCalculator:
    def __init__(self, loan_amount, loan_years):
        self.loan_amount = loan_amount
        self.loan_years = loan_years
        self.interest_rate = self.get_interest_rate()

    def get_interest_rate(self):
        if self.loan_years == 3:
            return 0.0603
        elif self.loan_years == 5:
            return 0.0612
        elif self.loan_years == 20:
            return 0.0439
        else:
            raise ValueError("不支持的贷款年限")

    def calculate_total_interest(self):
        return self.loan_amount * self.interest_rate

    def calculate_monthly_payment(self):
        total_interest = self.calculate_total_interest()
        return (self.loan_amount + total_interest) / (self.loan_years * 12)

loan_amount = 1000000
loan_years = 3
mortgage_calculator = MortgageCalculator(loan_amount, loan_years)
print("总利息：", mortgage_calculator.calculate_total_interest())
print("每月还款金额：", mortgage_calculator.calculate_monthly_payment())
