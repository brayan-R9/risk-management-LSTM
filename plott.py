import matplotlib.pyplot as plt

def strat_plot(profit1, profit2, profit3):
    fig, axs = plt.subplots(3, figsize=(10, 18))
    axs[0].plot(profit1, label='Equity Curve', color='red')
    axs[0].set_title('Equity Curve for High Risk High Reward Strategy')
    axs[0].set_xlabel('Trades')
    axs[0].set_ylabel('Profit/Loss')
    axs[0].legend()
    axs[0].grid(True)
    axs[1].plot(profit2, label='Equity Curve', color='blue')
    axs[1].set_title('Equity Curve for Medium Risk Medium Reward Strategy')
    axs[1].set_xlabel('Trades')
    axs[1].set_ylabel('Profit/Loss')
    axs[1].legend()
    axs[1].grid(True)
    axs[2].plot(profit3, label='Equity Curve', color='green')
    axs[2].set_title('Equity Curve for Low Risk Low Reward Strategy')
    axs[2].set_xlabel('Trades')
    axs[2].set_ylabel('Profit/Loss')
    axs[2].legend()
    axs[2].grid(True)
    
    plt.tight_layout()
    plt.show()