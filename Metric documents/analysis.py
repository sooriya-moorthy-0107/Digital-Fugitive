import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr, kendalltau

# ==========================================================
# DIGITAL FUGITIVE - SOFTWARE METRICS ANALYSIS
# ==========================================================

# Load CSV
df = pd.read_csv("Digital_Fugitive_128_Run_Dataset_with_Execution_Time.csv")

# ==========================================================
# PROJECT METRICS
# ==========================================================

metrics = [
    "Cells_Inspected",
    "Safe_Moves",
    "Fallback_Random_Moves",
    "Thieves_Identified",
    "Total_Moves",
    "Execution_Time"
]

# Check columns
for column in metrics:
    if column not in df.columns:
        print("Missing column:", column)
        print("Please add this column to your CSV:", column)
        exit()

# Total number of records
total_count = len(df)

print("\nDataset loaded successfully")
print("Total Count =", total_count)


# ==========================================================
# 1. BOX PLOT
# ==========================================================

plt.figure(figsize=(12, 6))

plt.boxplot(
    [df[column] for column in metrics],
    labels=[
        "Cells Inspected",
        "Safe Moves",
        "Fallback Moves",
        "Thieves Identified",
        "Total Moves",
        "Execution Time"
    ]
)

plt.title(
    "Digital Fugitive - Box Plot of Project Metrics",
    fontsize=15
)

plt.xlabel("Project Metrics")
plt.ylabel("Values")

plt.xticks(rotation=20)

plt.grid(axis="y")

plt.tight_layout()

plt.savefig(
    "01_Box_Plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Box Plot saved as: 01_Box_Plot.png")


# ==========================================================
# 2. CONTROL CHART - TOTAL MOVES
# ==========================================================

# Total Moves is the monitored metric

values = df["Total_Moves"]

# Mean
mean = values.mean()

# Standard deviation
std = values.std()

# Control limits
UCL = mean + (3 * std)
LCL = mean - (3 * std)

# LCL should not be negative
LCL = max(0, LCL)

# Count points outside control limits
out_of_control = (
    (values > UCL) |
    (values < LCL)
).sum()


# ==========================================================
# CREATE CONTROL CHART
# ==========================================================

plt.figure(figsize=(14, 7))

plt.plot(
    range(1, total_count + 1),
    values,
    marker="o",
    linewidth=1.5,
    label="Total Moves"
)

# ----------------------------------------------------------
# CENTER LINE
# ----------------------------------------------------------

plt.axhline(
    mean,
    linewidth=2,
    label=f"Center Line / Mean = {mean:.2f}"
)

# ----------------------------------------------------------
# UPPER CONTROL LIMIT
# ----------------------------------------------------------

plt.axhline(
    UCL,
    linestyle="--",
    linewidth=2,
    label=f"UCL = {UCL:.2f}"
)

# ----------------------------------------------------------
# LOWER CONTROL LIMIT
# ----------------------------------------------------------

plt.axhline(
    LCL,
    linestyle="--",
    linewidth=2,
    label=f"LCL = {LCL:.2f}"
)


# ==========================================================
# TITLE
# ==========================================================

plt.title(
    "Digital Fugitive - Control Chart for Total Moves",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel(
    "Run Number",
    fontsize=12
)

plt.ylabel(
    "Total Moves",
    fontsize=12
)


# ==========================================================
# TOTAL COUNT DISPLAY
# ==========================================================

plt.text(
    0.98,
    0.95,
    f"Total Moves = {total_count}",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    fontsize=12,
    fontweight="bold",
    bbox=dict(
        boxstyle="round,pad=0.4",
        facecolor="white",
        edgecolor="black"
    )
)


# ==========================================================
# GRAPH SETTINGS
# ==========================================================

plt.xticks(
    range(
        0,
        total_count + 1,
        max(1, total_count // 8)
    )
)

plt.legend()

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()


# ==========================================================
# SAVE CONTROL CHART
# ==========================================================

plt.savefig(
    "02_Control_Chart_Total_Moves.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================================
# PRINT CONTROL CHART RESULTS
# ==========================================================

print("\n======================================")
print("CONTROL CHART - TOTAL MOVES")
print("======================================")

print(f"Total Count = {total_count}")
print(f"Mean        = {mean:.2f}")
print(f"UCL         = {UCL:.2f}")
print(f"LCL         = {LCL:.2f}")
print(f"Out of Control Points = {out_of_control}")

print("\nControl Chart saved as:")
print("02_Control_Chart_Total_Moves.png")


# ==========================================================
# CORRELATION FUNCTION
# ==========================================================

def create_correlation_matrix(method, filename, title):

    correlation = df[metrics].corr(
        method=method
    )

    print("\n======================================")
    print(title)
    print("======================================")

    print(
        correlation.round(3)
    )

    plt.figure(
        figsize=(10, 8)
    )

    plt.imshow(
        correlation,
        aspect="auto"
    )

    plt.colorbar(
        label="Correlation Coefficient"
    )

    # Short names for graph
    short_names = [
        "Cells",
        "Safe",
        "Fallback",
        "Thieves",
        "Total Moves",
        "Execution Time"
    ]

    # X-axis
    plt.xticks(
        range(len(metrics)),
        short_names,
        rotation=35,
        ha="right"
    )

    # Y-axis
    plt.yticks(
        range(len(metrics)),
        short_names
    )

    # ------------------------------------------------------
    # WRITE CORRELATION VALUES
    # ------------------------------------------------------

    for i in range(len(metrics)):

        for j in range(len(metrics)):

            value = correlation.iloc[i, j]

            plt.text(
                j,
                i,
                f"{value:.2f}",
                ha="center",
                va="center",
                fontsize=9
            )

    plt.title(
        title,
        fontsize=15
    )

    plt.tight_layout()

    plt.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    print(
        "Saved as:",
        filename
    )

    return correlation


# ==========================================================
# 3. PEARSON CORRELATION
# ==========================================================

pearson = create_correlation_matrix(
    "pearson",
    "03_Pearson_Correlation.png",
    "Digital Fugitive - Pearson Correlation"
)


# ==========================================================
# 4. SPEARMAN CORRELATION
# ==========================================================

spearman = create_correlation_matrix(
    "spearman",
    "04_Spearman_Correlation.png",
    "Digital Fugitive - Spearman Correlation"
)


# ==========================================================
# 5. KENDALL CORRELATION
# ==========================================================

kendall = create_correlation_matrix(
    "kendall",
    "05_Kendall_Correlation.png",
    "Digital Fugitive - Kendall Correlation"
)


# ==========================================================
# SAVE CORRELATION TABLES
# ==========================================================

pearson.to_csv(
    "Pearson_Correlation.csv"
)

spearman.to_csv(
    "Spearman_Correlation.csv"
)

kendall.to_csv(
    "Kendall_Correlation.csv"
)

print(
    "\nCorrelation CSV files saved successfully."
)


# ==========================================================
# 6. DESCRIPTIVE STATISTICS
# ==========================================================

statistics = df[metrics].describe().T

# Variance
statistics["Variance"] = df[metrics].var()

# Coefficient of Variation
statistics["CV_Percentage"] = (
    df[metrics].std()
    / df[metrics].mean()
    * 100
)

# Save statistics
statistics.to_csv(
    "Digital_Fugitive_Statistics.csv"
)

print("\n======================================")
print("DESCRIPTIVE STATISTICS")
print("======================================")

print(
    statistics.round(3)
)


# ==========================================================
# 7. EXECUTION TIME STATISTICS
# ==========================================================

execution_time = df["Execution_Time"]

print("\n======================================")
print("EXECUTION TIME ANALYSIS")
print("======================================")

print(
    f"Total Runs             : {total_count}"
)

print(
    f"Average Execution Time : "
    f"{execution_time.mean():.4f} seconds"
)

print(
    f"Median Execution Time  : "
    f"{execution_time.median():.4f} seconds"
)

print(
    f"Minimum Execution Time : "
    f"{execution_time.min():.4f} seconds"
)

print(
    f"Maximum Execution Time : "
    f"{execution_time.max():.4f} seconds"
)

print(
    f"Std Deviation          : "
    f"{execution_time.std():.4f} seconds"
)


# ==========================================================
# 8. SAVE EXECUTION TIME SUMMARY
# ==========================================================

execution_summary = pd.DataFrame({

    "Metric": [
        "Total Runs",
        "Average Execution Time",
        "Median Execution Time",
        "Minimum Execution Time",
        "Maximum Execution Time",
        "Standard Deviation"
    ],

    "Value": [
        total_count,
        execution_time.mean(),
        execution_time.median(),
        execution_time.min(),
        execution_time.max(),
        execution_time.std()
    ]
})

execution_summary.to_csv(
    "Execution_Time_Statistics.csv",
    index=False
)


# ==========================================================
# 9. FINAL SUMMARY
# ==========================================================

print("\n======================================")
print("ALL ANALYSIS COMPLETED")
print("======================================")

print(
    f"\nTotal Count = {total_count}"
)

print("""
Generated files:

01_Box_Plot.png

02_Control_Chart_Total_Moves.png

03_Pearson_Correlation.png

04_Spearman_Correlation.png

05_Kendall_Correlation.png

Pearson_Correlation.csv

Spearman_Correlation.csv

Kendall_Correlation.csv

Digital_Fugitive_Statistics.csv

Execution_Time_Statistics.csv
""")