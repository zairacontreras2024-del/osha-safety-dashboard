# OSHA Safety Dashboard
# Author: Zaira Contreras

print("=" * 40)
print("       OSHA SAFETY DASHBOARD")
print("=" * 40)

metrics = {
    "TRIR": 1.2,
    "DART": 0.8,
    "Near Miss Reports": 12,
    "Open Corrective Actions": 5,
    "Safety Observations": 24,
    "Inspection Completion Rate": "96%"
}

for metric, value in metrics.items():
    print(f"{metric}: {value}")

print("\nDashboard generated successfully.")
