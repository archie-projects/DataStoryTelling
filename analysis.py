import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
mrr_growth = [8.86, 9.8, 5.71, 14.87]
industry_target = 15

# Calculate average (confirming)
average_growth = np.mean(mrr_growth)
print(f"Calculated Average MRR Growth: {average_growth:.2f}")

# Plot
plt.figure(figsize=(8,5))
plt.plot(quarters, mrr_growth, marker='o', label='MRR Growth')
plt.axhline(y=industry_target, color='r', linestyle='--', label='Industry Target (15)')
plt.title('2024 Quarterly MRR Growth vs Industry Benchmark')
plt.xlabel('Quarter')
plt.ylabel('MRR Growth (%)')
plt.ylim(0, 20)
plt.grid(True)
plt.legend()

# Save figure
plt.savefig('mrr_growth_trend.png')
plt.show()
