import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load data
df = pd.read_csv('medical_examination.csv')

# 2. Add overweight column
df['overweight'] = ((df["weight"] / ((df["height"] / 100) ** 2)) > 25).astype(int)

# 3. Normalize cholesterol and gluc values (1 → 0, >1 → 1)
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

# 4. Function to draw categorical plot
def draw_cat_plot():
    # 5. Convert data to long format
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and count occurrences
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Create the categorical plot
    catplot = sns.catplot(x="variable", y="total", hue="value", col="cardio", kind="bar", data=df_cat)

    # 8. Assign the figure
    fig = catplot.fig

    # 9. Return the figure
    return fig

# 10. Function to draw heat map
def draw_heat_map():
    # 11. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Compute the correlation matrix
    corr = df_heat.corr()
    # Near +1: Strong positive relationship (when one increases, the other increases).
    # Near -1: Strong negative relationship (when one increases, the other decreases).

    # 13. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # A correlation matrix is symmetrical (same values appear twice).
    # The mask hides one half to avoid redundancy.

    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15. Draw the heatmap
    sns.heatmap(corr, annot=True, fmt=".1f", cmap="coolwarm", linewidths=0.5, mask=mask, square=True)

    # corr: The correlation matrix (our data).

    # annot=True: Shows the correlation numbers inside the heatmap cells.

    # fmt=".1f": Displays the numbers with one decimal place.

    # cmap="coolwarm": Uses a blue-red color scale:

    # 🔵 Blue for negative correlation.

    # 🔴 Red for positive correlation.

    # linewidths=0.5: Draws thin white lines between cells for better visibility.

    # mask=mask: Hides the upper triangle of the heatmap.

    # square=True: Ensures that each cell in the heatmap is a perfect square.

    # 16. Return the figure
    return fig
