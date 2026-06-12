"""
Assignment 1 — AI System Specification
PEAS Framework & Task Environment Analysis

Student : Sumair Ahmed
Roll No : 2k24/AIE/62
Course  : Introduction to Artificial Intelligence
University: University of Sindh
"""

import json


def load_peas(filepath="fraud_detection_peas.json"):
    with open(filepath, "r") as f:
        return json.load(f)


def display_peas(data):
    print("=" * 65)
    print(f"  SYSTEM : {data['system_name']}")
    print(f"  STUDENT: {data['student']['name']}  |  {data['student']['roll_number']}")
    print("=" * 65)

    peas = data["peas"]

    # ── Performance Measures ──────────────────────────────────────
    print("\n📊  PERFORMANCE MEASURES")
    print("-" * 40)
    for i, pm in enumerate(peas["performance_measures"], 1):
        print(f"  {i}. {pm}")

    # ── Environment ───────────────────────────────────────────────
    print("\n🌐  ENVIRONMENT")
    print("-" * 40)
    print(f"  Description : {peas['environment']['description']}")
    print("  Channels    :")
    for ch in peas["environment"]["channels"]:
        print(f"    • {ch}")

    # ── Actuators ─────────────────────────────────────────────────
    print("\n⚙️   ACTUATORS")
    print("-" * 40)
    for act in peas["actuators"]:
        print(f"  • {act}")

    # ── Sensors ───────────────────────────────────────────────────
    print("\n🔍  SENSORS")
    print("-" * 40)
    for sen in peas["sensors"]:
        print(f"  • {sen}")

    # ── Environment Classification ────────────────────────────────
    print("\n🗂️   ENVIRONMENT CLASSIFICATION")
    print("-" * 40)
    ec = data["environment_classification"]
    for dimension, details in ec.items():
        print(f"  {dimension.upper():<22} → {details['choice']}")
        print(f"  {'':22}   {details['justification']}")
        print()

    # ── Utility Function ──────────────────────────────────────────
    print("⚖️   UTILITY FUNCTION")
    print("-" * 40)
    uf = data["utility_function"]
    print(f"  Formula   : {uf['formula']}")
    weights = uf["default_weights"]
    print(f"  Weights   : alpha={weights['alpha']}, beta={weights['beta']}, gamma={weights['gamma']}")
    print(f"  Trade-off : {uf['trade_off']}")
    print("=" * 65)


def simulate_utility(recall, fpr, latency, alpha=0.6, beta=0.3, gamma=0.1):
    """Calculate utility score for given inputs."""
    return alpha * recall - beta * fpr - gamma * latency


def demo_utility_tradeoff():
    print("\n🔬  UTILITY FUNCTION DEMO — Effect of Doubling Alpha")
    print("-" * 55)

    scenarios = [
        {"label": "Normal transaction (low risk)",  "recall": 0.80, "fpr": 0.05, "latency": 0.10},
        {"label": "Suspicious transaction (medium)", "recall": 0.92, "fpr": 0.12, "latency": 0.15},
        {"label": "High-risk transaction",           "recall": 0.99, "fpr": 0.30, "latency": 0.20},
    ]

    for s in scenarios:
        u_default = simulate_utility(s["recall"], s["fpr"], s["latency"], alpha=0.6)
        u_doubled = simulate_utility(s["recall"], s["fpr"], s["latency"], alpha=1.2)
        print(f"\n  Scenario : {s['label']}")
        print(f"    Recall={s['recall']}, FPR={s['fpr']}, Latency={s['latency']}")
        print(f"    U (alpha=0.6) = {u_default:.4f}")
        print(f"    U (alpha=1.2) = {u_doubled:.4f}  ← security-first mode")

    print()


if __name__ == "__main__":
    data = load_peas("fraud_detection_peas.json")
    display_peas(data)
    demo_utility_tradeoff()
