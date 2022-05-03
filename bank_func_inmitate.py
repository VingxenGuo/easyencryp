class Bank():
    '''定義銀行類別'''
    bankname = 'Taipei Bank'
    def __init__(self, uname, money): # 定義屬性及參數、初始化方法
        self.name = uname
        self.balance = money

    def get_balance(self):
        return self.balance
    
    def save_money(self, money):                            # 設計存錢方法
        self.balance += money
        print('經存款', money, '後存款餘: ', self.balance)
        return self.balance

    def withdraw_money(self, money):                        # 設計領錢方法
        self.balance -= money
        print('經提領', money, '後存款餘: ', self.balance)
        return self.balance

JasonBank = Bank('Jason', 1000)      # 定義物件
JasonBank.save_money(int(input('請輸入存入金額: ')))
JasonBank.withdraw_money(int(input('請輸入提領金額: ')))