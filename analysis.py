import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Compute average
average = df["MRR_Growth"].mean()
print(f"Average MRR Growth: {average:.2f}")

# Benchmark
industry_target = 15

# Visualization
plt.figure(figsize=(8,5))
plt.plot(df["Quarter"], df["MRR_Growth"], marker="o", label="Company MRR Growth")
plt.axhline(industry_target, color="red", linestyle="--", label="Industry Target (15%)")
plt.title("Quarterly MRR Growth vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")
plt.legend()
plt.tight_layout()
plt.savefig("mrr_growth.png")
plt.show()
