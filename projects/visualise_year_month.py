import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("./doc/fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
#here date is converted in date-time format and stored in index so it's easier for matplotlib to read it

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12, 5))
    plt.plot(df.index, df['value'], color='red', linewidth=1)  # Use df.index instead of df['date']
    plt.xlabel("Date")  # add X-axis label
    plt.ylabel("Page Views")  # add Y-axis label
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019") 

    # Save image and return fig (don't change this part)
    plt.show()
    fig.savefig('line_plot.png')
    return fig

draw_line_plot()

def draw_bar_plot():
    ##NOTE:
    # Creates a Figure (fig) → The entire image (canvas) that contains all plots.

    # Creates an Axes (ax) → The specific plotting area inside the figure where data is drawn.

    # Think of fig as a blank paper, and ax as a box on that paper where you draw your graph.

    # Why Use ax Instead of Just plt?
    # ✅ More Control: ax gives you direct control over specific plots within a figure.
    # ✅ Multiple Plots: You can create multiple ax objects for multiple subplots in the same figure.
    # ✅ Cleaner Code: It avoids conflicts when working with multiple plots.


    ##NOTE:
    # Output (Before unstack()):

    #                 page_views
    # Year  Month              
    # 2020  January         100
    #     February        150
    # 2021  January         120
    #     February        180
    # Here, Year and Month are in the index, which makes it harder to use for plotting.

    # Applying .unstack()
    # Now, if we apply .unstack(), the Month moves from the index to column headers, making it easier to read:


    # df_unstacked = df.unstack()
    # print(df_unstacked)
    # Output (After unstack()):

    #     page_views           
    # Month    January February
    # Year                      
    # 2020        100      150
    # 2021        120      180
    # Now, the months are column headers, and the years remain as row indices.
    # This format is better for plotting in a bar chart.
    
        # unstack() moves one level of the index into columns.
        # It helps in reshaping grouped data for analysis or plotting.
        # Useful for bar plots where you need categories (months) as columns.

    # Copy and modify data for monthly bar plot
    df['year'] = df.index.year
    df['month'] = df.index.month

    df_bar = df.groupby(['year','month'])['value'].mean().unstack()

    month_labels = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))  # Create figure and axis
    df_bar.plot(kind='bar', ax=ax)  # Plot the bar chart
    ax.set_xlabel("Years")  # Set x-axis label
    ax.set_ylabel("Average Page Views")  # Set y-axis label
    ax.set_title("Average Daily Page Views per Month")  # Set title
    ax.legend(title="Months", labels=month_labels)  # Add legend with month names

    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig
draw_bar_plot()



# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# from pandas.plotting import register_matplotlib_converters
# register_matplotlib_converters()

# # Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=['date'], index_col='date')
# # print(df)

# # Clean data
# df = df[
#     (df['value']>=df['value'].quantile(0.025))&
#     (df['value']<= df['value'].quantile(0.975))]


# def draw_line_plot():
#     # Draw line plot
#     fig = plt.figure(figsize=(12, 5))
#     plt.plot(df.index, df['value'], color='red', linewidth=1)  # Use df.index instead of df['date']
#     plt.xlabel("Date")  # add X-axis label
#     plt.ylabel("Page Views")  # add Y-axis label
#     plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019") 

#     # Save image and return fig (don't change this part)
#     plt.show()
#     fig.savefig('line_plot.png')
#     return fig
    

# def draw_bar_plot():
#     # Copy and modify data for monthly bar plot
#     df['year'] = df.index.year
#     df['month'] = df.index.month

#     df_bar = df.groupby(['year','month'])['value'].mean().unstack()

#     month_labels = ["January", "February", "March", "April", "May", "June",
#                     "July", "August", "September", "October", "November", "December"]
#     # Draw bar plot
#     fig, ax = plt.subplots(figsize=(12, 6))  # Create figure and axis
#     df_bar.plot(kind='bar', ax=ax)  # Plot the bar chart
#     ax.set_xlabel("Years")  # Set x-axis label
#     ax.set_ylabel("Average Page Views")  # Set y-axis label
#     ax.set_title("Average Daily Page Views per Month")  # Set title
#     ax.legend(title="Months", labels=month_labels)  # Add legend with month names

#     # Save image and return fig (don't change this part)
#     fig.savefig("bar_plot.png")
#     return fig
# # draw_bar_plot()

# def draw_box_plot():
#     # Prepare data for box plots (this part is done!)
#     df_box = df.copy()
#     df_box.reset_index(inplace=True)
#     df_box['year'] = [d.year for d in df_box.date]
#     df_box['month'] = [d.strftime('%b') for d in df_box.date]

#     month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
#                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

#     # Draw box plots (using Seaborn)
#     fig, axes = plt.subplots(1, 2, figsize=(15, 6))

#     # Year-wise Box Plot
#     ax=axes[0]
#     sns.boxplot(x="year", y="value", data=df_box, ax=ax)
#     ax.set_title("Year-wise Box Plot (Trend)")
#     ax.set_xlabel("Year")
#     ax.set_ylabel("Page Views")

#     # Month-wise Box Plot
#     ax=axes[1]
#     sns.boxplot(x="month", y="value", data=df_box, order=month_order,ax=ax)
#     ax.set_title("Month-wise Box Plot (Seasonality)")
#     ax.set_xlabel("Month")
#     ax.set_ylabel("Page Views") 
#     # ax.tick_params(axis='x', rotation=90)



#     # Save image and return fig (don't change this part)
#     fig.savefig('box_plot.png')
#     return fig
# # draw_box_plot()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data():
    global df
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
    df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]
    
    # Fix: Ensure count() returns a single integer
    global df_count
    df_count = df.count(numeric_only=True).sum()

# Load and clean data on import
load_and_clean_data()

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df["value"], color='red', linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.xticks(rotation=45)
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()
    
    fig = df_bar.plot(kind='bar', figsize=(12, 5)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.strftime('%b')
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1], order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    
    return fig
