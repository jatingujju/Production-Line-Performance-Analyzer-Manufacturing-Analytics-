# data_generation.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

random.seed(42)
np.random.seed(42)

num_machines = 5
days = 30
start_date = datetime(2025,10,15)
records = []
machine_ids = [f"MCH_{i+1:02d}" for i in range(num_machines)]
operators = [f"OP_{i+1:02d}" for i in range(8)]
shifts = ["Morning","Afternoon","Night"]

for day in range(days):
    current_date = start_date + timedelta(days=day)
    for m in machine_ids:
        for shift in shifts:
            timestamp = current_date + timedelta(hours={"Morning":8,"Afternoon":16,"Night":0}[shift])
            base_prod = np.random.randint(80,150)
            shift_modifier = {"Morning":1.05,"Afternoon":0.95,"Night":0.85}[shift]
            production_count = int(base_prod * shift_modifier + np.random.normal(0,8))
            defective_rate = np.clip(np.random.normal(0.03,0.01),0.005,0.10)
            defective_count = int(production_count * defective_rate)
            downtime_minutes = max(0, int(np.random.exponential(15)))
            temperature = round(np.random.normal(65,3) + (0.02 * downtime_minutes),2)
            vibration = round(np.random.normal(0.35,0.08) + (0.001 * downtime_minutes),3)
            operator = random.choice(operators)
            maintenance_flag = 1 if downtime_minutes > 60 or np.random.rand() < 0.01 else 0
            records.append({
                "date": current_date.strftime("%Y-%m-%d"),
                "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "machine_id": m,
                "shift": shift,
                "operator_id": operator,
                "production_count": production_count,
                "defective_count": defective_count,
                "downtime_minutes": downtime_minutes,
                "temperature_C": temperature,
                "vibration_g": vibration,
                "maintenance_required": maintenance_flag
            })

df = pd.DataFrame(records)
df["yield_pct"] = round((df["production_count"] - df["defective_count"]) / df["production_count"] * 100,2)

os.makedirs("data", exist_ok=True)
df.to_csv("data/production_line_data.csv", index=False)
print("Saved data/production_line_data.csv")
