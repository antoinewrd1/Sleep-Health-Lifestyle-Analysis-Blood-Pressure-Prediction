# 4. EXPLORATORY DATA ANALYSIS

print("\nDescriptive Statistics:")
print(df.describe())

if "Sleep Disorder" in df.columns and "Daily Steps" in df.columns:
    average_steps = (
        df.groupby("Sleep Disorder")["Daily Steps"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    print("\nAverage Daily Steps by Sleep Disorder Classification:")
    print(average_steps)

#Regression plot function
def regression_plot(data, x, y, title):
    if x in data.columns and y in data.columns:
        plt.figure(figsize=(8,5))
        sns.regplot(
            data=data,
            x=x,
            y=y,
            scatter_kws={"alpha": 0.65},
            line_kws={"color": "orange"}
        )
        plt.title(title)
        plt.tight_layout()
        plt.show()


regression_plot(df, "Daily Steps", "Sleep Duration", "Daily Steps vs. Sleep Duration")
regression_plot(df, "Sleep Duration", "Quality of Sleep", "Sleep Duration vs. Quality of Sleep")
regression_plot(df, "Physical Activity Level", "Stress Level", "Physical Activity Level vs. Stress Level")
regression_plot(df, "Physical Activity Level", "Heart Rate", "Physical Activity Level vs. Heart Rate")
regression_plot(df, "Age", "Heart Rate", "Age vs. Heart Rate")

if "Sleep Disorder" in df.columns and "Daily Steps" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=df,
        x="Sleep Disorder",
        y="Daily Steps",
        estimator="mean",
        errorbar=None
    )
    plt.title("Average Daily Steps by Sleep Disorder Classification")
    plt.tight_layout()
    plt.show()