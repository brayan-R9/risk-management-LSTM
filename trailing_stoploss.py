import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def strat3(combined_df, amount):
    change = 3
    target=change
    global_stoploss =change/2
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
            target_achieved=False
            stop_loss_adjusted=False

            for j in range(start, end + 1):

                if s>0:
                    #calculating the current pnl
                    s_actual = ((combined_df['Close_actual'].iloc[j] - initial_amount_actual) / combined_df['Close_actual'].iloc[j]) * 100
                    s_actual_value=(combined_df['Close_actual'].iloc[j] - initial_amount_actual) * qty_actual

                    #chaning stoploss to initial_amount to prevent losses
                    if s_actual>=target/2:
                        stoploss_value=initial_amount_actual
                        stop_loss_adjusted=True

                    #exit condition for initial stoploss
                    if s_actual<=-global_stoploss and not stop_loss_adjusted:
                        pnl_actual = (combined_df['Close_actual'].iloc[j] - initial_amount_actual) * qty_actual
                        stop_loss_triggered = True
                        break
                    
                    #exit condition for target
                    if s_actual>=target:
                        pnl_actual = (combined_df['Close_actual'].iloc[j] - initial_amount_actual) * qty_actual
                        target_achieved=True
                        break
                    
                    #exit condition for the new adjusted stoploss
                    if stop_loss_adjusted:
                        if s_actual_value<=stoploss_value:
                            pnl_actual=0
                            break

                else:
                     #calculating the current pnl
                    s_actual = ((initial_amount_actual-combined_df['Close_actual'].iloc[j])/initial_amount_actual)*100
                    s_actual_value=(initial_amount_actual-combined_df['Close_actual'].iloc[j]) * qty_actual

                    #chaning stoploss to initial_amount to prevent losses
                    if s_actual>=target/2:
                        stoploss_value=initial_amount_actual
                        stop_loss_adjusted=True

                    #exit condition for initial stoploss
                    if s_actual<=-global_stoploss and not stop_loss_adjusted:
                        pnl_actual = (initial_amount_actual-combined_df['Close_actual'].iloc[j]) * qty_actual
                        stop_loss_triggered = True
                        break
                    
                    #exit condition for target
                    if s_actual>=target:
                        pnl_actual = (initial_amount_actual-combined_df['Close_actual'].iloc[j]) * qty_actual
                        target_achieved=True
                        break
                    
                    #exit condition for the new adjusted stoploss
                    if stop_loss_adjusted:
                        if s_actual_value<=stoploss_value:
                            pnl_actual=0
                            break




            if not stop_loss_triggered and not target_achieved:
                pnl_actual = pnl_current

            pnl+=pnl_actual
            profits_real.append(pnl)
            pos = 0 # Close position

    print(trades)
    print("profit_real={}".format(profits_real[-1]))
    return profits_real

def strat3_plot(profit):
    plt.figure(figsize=(10, 6))
    plt.plot(profit, label='Equity Curve', color='blue')
    plt.title('Equity Curve')
    plt.xlabel('Trades')
    plt.ylabel('Profit/Loss')
    plt.legend()
    plt.grid(True)
    plt.show()

