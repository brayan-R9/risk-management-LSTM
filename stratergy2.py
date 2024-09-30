import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def strat2(combined_df, amount,global_stoploss):
    change = 3
    #global_stoploss = 5
    pos = 0
    pnl_actual = 0
    profits_real = [0]
    pnl_real=[]
    pnl=0
    trades = {"long": 0, "short": 0}
    
    for i in range(len(combined_df)):
        if not pos:  # If no current position
            initial_amount = combined_df['Close_pred'].iloc[i]
            qty = amount // initial_amount
            initial_amount_actual = combined_df['Close_actual'].iloc[i]
            qty_actual = amount // initial_amount_actual
            pos = 1  # Open a new position
            start=i #recording the entry index:

        # Calculate predicted change percentage
        s = ((combined_df['Close_pred'].iloc[i] - initial_amount) / combined_df['Close_pred'].iloc[i]) * 100

        # Check if change exceeds threshold or it's the last element
        if abs(s) >= change:
            if s < 0:
                trades['short'] += 1
                pnl_current=(initial_amount_actual-combined_df['Close_actual'].iloc[i])* qty_actual
            else:
                trades['long'] += 1
                pnl_current = (combined_df['Close_actual'].iloc[i] - initial_amount_actual) * qty_actual

            end = i  # Recording the exit index
            

            # Check for stop loss condition within the range from start to current index i
            stop_loss_triggered = False
            for j in range(start, end + 1):

                if s>0:
                    s_actual = ((combined_df['Close_actual'].iloc[j] - initial_amount_actual) / combined_df['Close_actual'].iloc[j]) * 100
                    if s_actual <= -global_stoploss:
                        pnl_actual = (combined_df['Close_actual'].iloc[j] - initial_amount_actual) * qty_actual
                        stop_loss_triggered = True
                        break
                else:
                    s_actual = ((initial_amount_actual-combined_df['Close_actual'].iloc[j])/initial_amount_actual)*100
                    if s_actual <= -global_stoploss:
                        pnl_actual = (initial_amount_actual-combined_df['Close_actual'].iloc[j]) * qty_actual
                        stop_loss_triggered = True
                        break
                    


            if not stop_loss_triggered:
                pnl_actual = pnl_current

            pnl+=pnl_actual
            profits_real.append(pnl)
            pos = 0 # Close position

    print(trades)
    print("profit_real={}".format(profits_real[-1]))
    return profits_real


def strat2_plot(profit):
    plt.figure(figsize=(10, 6))
    plt.plot(profit, label='Equity Curve', color='blue')
    plt.title('Equity Curve')
    plt.xlabel('Trades')
    plt.ylabel('Profit/Loss')
    plt.legend()
    plt.grid(True)
    plt.show()