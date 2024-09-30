import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def combine(test_predict,data,df_dummy):
    data1=np.ravel(test_predict)
    df_pred=pd.DataFrame(data1, columns=['Close_pred'])
    df_actual=data.iloc[len(data)-len(df_pred):]
    df_actual=df_actual.copy()
    df_actual.rename(columns={'Close': 'Close_actual'},inplace=True)
    df_pred.reset_index(drop=True,inplace=True)
    df_actual.reset_index(drop=True,inplace=True)
    combined_df=df_pred.join(df_actual)
    combined_df.index =df_dummy.index
    return combined_df


def strat1(combined_df,amount):
    change=3
    start = 0
    pos = 0
    pnl = 0
    pnl_actual = 0
    profits_real = [0]
    trades = {"long": 0, "short": 0}
    
    for i in range(len(combined_df)):
        if not pos:
            initial_amount = combined_df['Close_pred'].iloc[i]
            qty = amount // initial_amount
            pos = 1

            initial_amount_actual = combined_df['Close_actual'].iloc[i]
            qty_actual = amount // initial_amount_actual

        s = ((combined_df['Close_pred'].iloc[i] - initial_amount) / combined_df['Close_pred'].iloc[i]) * 100

        if abs(s) >= change:
            if s < 0:
                trades['short'] += 1
            else:
                trades['long'] += 1

            pos = 0

            if s < 0:
                pnl_actual += (initial_amount_actual - combined_df['Close_actual'].iloc[i]) * qty_actual
            else:
                pnl_actual += (combined_df['Close_actual'].iloc[i] - initial_amount_actual) * qty_actual

            profits_real.append(pnl_actual)


            
    print(trades)
    print("profit_real={}".format(profits_real[-1]))
    
    return profits_real

def strat1_plot(profit):
    plt.figure(figsize=(10, 6))
    plt.plot(profit, label='Equity Curve', color='blue')
    plt.title('Equity Curve')
    plt.xlabel('Trades')
    plt.ylabel('Profit/Loss')
    plt.legend()
    plt.grid(True)
    plt.show()




