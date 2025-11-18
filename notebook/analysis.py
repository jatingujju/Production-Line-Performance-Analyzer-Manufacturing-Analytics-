# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("data/production_line_data.csv", parse_dates=["timestamp"])

# Basic KPIs
kpis = {
    "total_production": int(df["production_count"].sum()),
    "total_defects": int(df["defective_count"].sum()),
    "average_yield_pct": float(df["yield_pct"].mean()),
    "average_downtime_min": float(df["downtime_minutes"].mean())
}
print("KPIs:", kpis)

# Machine-level summary
machine_summary = df.groupby("machine_id").agg({
    "production_count":"sum",
    "defective_count":"sum",
    "downtime_minutes":"mean",
    "yield_pct":"mean"
}).reset_index().sort_values("production_count", ascending=False)
print(machine_summary)

# Save machine summary
os.makedirs("outputs", exist_ok=True)
machine_summary.to_csv("outputs/machine_summary.csv", index=False)

# Simple visualization: Total production per machine
plt.figure(figsize=(8,5))
plt.bar(machine_summary["machine_id"], machine_summary["production_count"])
plt.title("Total Production per Machine")
plt.xlabel("Machine")
plt.ylabel("Production Count")
plt.tight_layout()
plt.savefig("outputs/figures/production_per_machine.png")
plt.close()

# Trend: daily total production
daily = df.groupby("date").production_count.sum().reset_index()
plt.figure(figsize=(10,4))
plt.plot(daily["date"], daily["production_count"])
plt.title("Daily Total Production (30 days)")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/figures/daily_production_trend.png")
plt.close()

print("Saved output files under outputs/figures and outputs/machine_summary.csv")

