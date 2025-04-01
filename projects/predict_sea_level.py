import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("./doc/epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="red", label="Sea Level Data")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Perform linear regression on all data
    slope_all, intercept_all, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    
#     Uses linear regression on the entire dataset to get:

#     slope_all → The slope of the trend line (how much sea level rises per year).

#     intercept_all → The y-intercept (starting sea level at Year = 0).

# _ (underscores) are used to ignore unnecessary returned values (r-value, p-value, std-error).

    # Generate x values from min year to 2050 for first regression line
    x_pred_all = np.arange(df["Year"].min(), 2051)
    y_pred_all = slope_all * x_pred_all + intercept_all ## linear equation for slop => y=mx+c

    # Plot first line of best fit (all data)
    plt.plot(x_pred_all, y_pred_all, color="blue", linestyle="--", label="Best Fit (All Data)")

    # Filter data from 2000 onward
    df_recent = df[df["Year"] >= 2000]

    # Perform linear regression on data from 2000 onward
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])

    # Generate x values from 2000 to 2050 for second regression line
    x_pred_recent = np.arange(2000, 2051)
    y_pred_recent = slope_recent * x_pred_recent + intercept_recent

    # Plot second line of best fit (2000 onward)
    plt.plot(x_pred_recent, y_pred_recent, color="green", linestyle="--", label="Best Fit (2000-Present)")

    # Add legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()

# Run function to generate the plot
draw_plot()
