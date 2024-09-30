def bh_stats(bh_pnl):
    maximum_drawdown=0
    maximum_profit=0

    for i in range(len(bh_pnl)):
        maximum_drawdown=min(bh_pnl.iloc[i],maximum_drawdown)
        maximum_profit=max(bh_pnl.iloc[i],maximum_drawdown)

    final_pnl=bh_pnl.iloc[-1]


    print("THE MAXIMUM DRAWDOWN IS: {:.2f}".format(maximum_drawdown))
    print("THE FINAL PNL IS: {:.2f}".format(final_pnl))
    print("THE MAXIMUM PROFIT IS: {:.2f}".format(maximum_profit))

def strategy_stats(strategy1_pnl):
    maximum_drawdown=0
    maximum_profit=0
    losing_trade=0
    winning_trade=0

    slow,fast=0,1

    while fast<len(strategy1_pnl):
        if strategy1_pnl[fast]<strategy1_pnl[slow]:
            losing_trade+=1
        else:
            winning_trade+=1
        slow+=1
        fast+=1

    for values in strategy1_pnl:
        maximum_drawdown=min(values,maximum_drawdown)
        maximum_profit=max(values,maximum_drawdown)
    
    final_pnl=strategy1_pnl[-1]

    print("THE MAXIMUM DRAWDOWN IS: {:.2f}".format(maximum_drawdown))
    print("THE MAXIMUM PROFIT IS: {:.2f}".format(maximum_profit))
    print("THE FINAL PNL IS: {:.2f}".format(final_pnl))
    print("NUMBER OF WINNING TRADES: {}".format(winning_trade))
    print("NUMBER OF LOSING TRADES: {}".format(losing_trade))
    print("ACCURACY: {:.2f}%".format((winning_trade)/(winning_trade+losing_trade)*100))



