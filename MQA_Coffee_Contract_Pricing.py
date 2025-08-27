""" Coffee Option Contract Analysis:
    The purpose of this program is to calculate a Cost of Carry futures price, a Black-Scholes model options price and a Monte-Carlo simulation 
    to determine the fair price of a coffee option contract.

    Market Data:
        Current spot price (S_t): $1.20 per pound
        Risk-free rate (r): 2% per annum
        Storage cost (d): 1% per annum
        Time to maturity (T): 6 months (0.5 years)
        Strike price (X): $1.25
        Volatility (sigma): 25%

    Note:
        As mentioned in the README document, the program is simply calculating and printing the result as per the Forage task documentation and requirements. Typically, I would 
        have wrapped the pricing calculations in functions for code modularity and re-usability, as well as providing a summary block for the print statements.
"""

from scipy.stats import norm
import numpy as np

# Given Values

S_t = 1.20                  # spot price
r = 0.02                    # risk-free rate
d = 0.01                    # storage cost
T = 0.5                     # time to maturity
X = 1.25                    # strike price
sigma = 0.25                # volatility



# Calculate futures price - cost of carry 
    # futures price represented as F_t

F_t = S_t * np.exp((r+d) * T)

print(f"The fair price of the coffee futures contract is: ${F_t:.3f} per pound.\n")         # F_t = $1.2181 per pound



# Black-Scholes model for option price

# calculate d1 & d2

d1 = (np.log(S_t / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

d2 = d1 - sigma * np.sqrt(T)

# Calculate the call option price

co_price = S_t * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)

print(f"The price of the call option is: ${co_price:.3f}.\n")                         # co_price = $0.068




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
    price_pathways[t] = price_pathways[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)

    # where:
        # t = the current time step in the simulation loop
        # z = a vector of random numbers from the standard normal distribution

# calculating the average price simulated at maturity

average_simulated_price = np.mean(price_pathways[-1])

print(f"The average simulated price of the coffee futures contract at maturity is ${average_simulated_price:.3f}\n")              # average simulated price = $1.213



