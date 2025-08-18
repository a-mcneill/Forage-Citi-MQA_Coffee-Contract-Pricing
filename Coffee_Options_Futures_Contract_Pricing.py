""" Coffee Option Contract Analysis:
    The puprose of this program is to calculate a Cost of Carry futures price, a Black-Scholes model options price and a Monte-Carlo simulation 
    to determine the fair price of a coffee option contract.

    Market Data:
        Current spot price (S_t): $1.20 per pound
        Risk-free rate (r): 2% per anum
        Storage cost (d): 1% per anum
        Time to maturity (T): 6 months (0.5 years)
        Strike price (X): $1.25
        Volatility (sigma): 25%

    Note:
        While I would typically define functions for these calculations and provide greater functionality to the program, this program has been designed in alignment with the
        requirements and layout provided in the virtual experience task documentation. As such, print statements have been utilised rather than the return values of functions.
"""

from scipy.stats import norm
import numpy as np

# Given Values

S_t = 1.20
r = 0.02
d = 0.01
T = 0.5
X = 1.25
sigma = 0.25



# Calculate futures price - cost of carry 
""" Futures price represented as Ft"""

F_t = S_t * np.exp((r+d) * T)

print(f"The fair price of the coffee futures contract is: ${F_t:.3f} per pound.")         # F_t = $1.2181 per pound



# Black-Scholes model for option price

# calculate d1 & d2

d1 = (np.log(S_t / X) + (r + T * sigma ** 2) * T) / (sigma * np.sqrt(T))

d2 = d1 - sigma * np.sqrt(T)

# Calculate the call option price

co_price = S_t * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)

print(f"The price of the call option is: ${co_price:.3f}.")                         # co_price = $0.068




# Monte-Carlo simulation

# additional simulation parameters
    # num_simulations -> number of simulations
    # num_steps -> number of steps (intervals) (daily) -> as per task documentation; more steps provides a smoother and more realistic path

num_simulations = 1000
num_steps = 252

# time increment

dt = T / num_steps

# simulating price pathways

np.random.seed(42)
price_pathways = np.zeros((num_steps, num_simulations))
price_pathways[0] = S_t

for t in range(1, num_steps):
    z = np.random.standard_normal(num_simulations)
    price_pathways[t] = price_pathways[t - 1] * np.exp((r - T * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)

    # where:
        # t = the current time step in the simulation loop
        # z = a vector of random numbers from the standard normal distribution

# calculating the average price simulated at maturity

average_simulated_price = np.mean(price_pathways[-1])

print(f"The average simulated price of the coffee futures contract at maturity is ${average_simulated_price:.3f}")              # average simulated price = $1.213




""" 
How changes in supply, demand, weather, and geopolitical factors might impact pricing?

    Supply shocks, such as drought or extreme weather conditions, would increase the price of the future and raise the options premium, as reduced supply drives
    higher prices and increases the volatility of the option, and therefore the value.

    Demand surges, whether seasonal or driven by economic growth, would also increase the futures price and increase the option premium, 
    as increased demand without an increase in supply leads to higher prices and volatility/uncertainty.

    Weather events can have both positive and negative impacts on the futures price, depending on the region and the impact of the event.
    Weather events can increase the options premium as they add greater uncertainty and potential for sudden price swings.

    Geopolitical tensions, such as disrupted trade routes, will increase the futures price and option premium due to impact of introducing risk and unpredictability,
    which markets price in through higher premiums.

    Improved geopolitical tensions, logisitics, or storage, will lower the futures price due to lowering the cost of carry and lower the option premium by reducing risk
    and smoothing supply chains.

"""