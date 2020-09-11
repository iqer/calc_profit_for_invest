# -*- coding: utf-8 -*-

# BOND_PROFIT = 0.07
# INDEX_PROFIT = 0.15

BOND_PROFIT = 0.14
INDEX_PROFIT = 0.25

def calc_one_year_profit():
    bond_sum = 0
    index_sum = 0
    for i in range(1, 361):
        bond_sum = (0.5 + bond_sum) * (1 + BOND_PROFIT / 12)
        index_sum = (0.5 + index_sum) * (1 + INDEX_PROFIT / 12)
        if i % 12 == 0:
            print("债券基金年化收益: %s, %s年每年投资0.5w*12=6w的资金总和为: %s万" % (BOND_PROFIT, i / 12, bond_sum))
            print("指数基金年化收益: %s, %s年每年投资0.5w*12=6w的资金总和为: %s万" % (INDEX_PROFIT, i / 12, index_sum))

if __name__ == "__main__":
    calc_one_year_profit()