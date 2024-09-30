from test_main import Bot
import pandas as pd
import numpy as np
from strategy1 import *
from stats import *
from plott import *
from stratergy2 import *
from trailing_stoploss import *


stock_name=input("Enter the name of the stock")
start_date=input("Enter the start date")
end_date=input("Enter the end date")
amount=int(input("Enter the amount"))

a=Bot(stock_name,start_date,end_date,amount)
print("------B&H EQUITY CURVE------")

a.bh_plot()
df_dummy=a.dummy_df()

print("--------CREATING MODEL-------")
test_predict,data=a.model()
combined_df=combine(test_predict=test_predict,data=data,df_dummy=df_dummy)
combined_df = combined_df.loc[start_date:end_date]
profits_real=strat1(combined_df,amount)
print("-------EQUITY CURVE OF MODEL 1-------")
strat1_plot(profit=profits_real)

profits_real2=strat2(combined_df,amount,global_stoploss=5)

print("-------EQUITY CURVE OF MODEL 2-------")
strat2_plot(profit=profits_real2)

print("STATS OF STRAT 1")
strategy_stats(profits_real)

print("STATS OF STRAT 2")
strategy_stats(profits_real2)

profits_real3=strat3(combined_df,amount)
print("-------EQUITY CURVE OF MODEL 2-------")
strat3_plot(profit=profits_real3)

print("STATS OF STRAT 3")
strategy_stats(profits_real3)






