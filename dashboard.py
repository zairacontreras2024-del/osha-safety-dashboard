print("OSHA Safety Dashboard")

metrics = {
    "TRIR": 1.2,
    "DART": 0.8,
    "Near Miss Reports": 12,
    "Open Corrective Actions": 5
}

for metric, value in metrics.items():
    print(f"{metric}: {value}")
