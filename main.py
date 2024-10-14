import numpy as np

variants = [
    {"a": 10, "c": 2.0, "x1": 0, "x2": 10},
    {"a": 20, "c": 3.0, "x1": 10, "x2": 20},
    {"a": 50, "c": 0.1, "x1": 20, "x2": 30},
    {"a": 30, "c": 1.0, "x1": 5, "x2": 10},
    {"a": 45, "c": 0.5, "x1": 5, "x2": 20},
    {"a": 55, "c": 4.0, "x1": 5, "x2": 30},
    {"a": 25, "c": 0.25, "x1": 0, "x2": 10},
    {"a": 65, "c": 5.0, "x1": 10, "x2": 20},
    {"a": 75, "c": 0.4, "x1": 20, "x2": 30},
    {"a": 35, "c": 0.2, "x1": 0, "x2": 10},
    {"a": 95, "c": 1.2, "x1": 10, "x2": 20},
    {"a": 15, "c": 2.5, "x1": 20, "x2": 30},
    {"a": 15, "c": 0.6, "x1": 5, "x2": 10},
    {"a": 85, "c": 3.5, "x1": 5, "x2": 20}
]

# Функція для обчислення сподіваного виграшу
def expected_value(x1, x2):
    return (x1 + x2) / 2

# Функція корисності
def utility(a, x, c):
    return a * (x ** c)

def expected_utility(a, x1, x2, c):
    return (a / (x2 - x1)) * (1 / (c + 1)) * (x2 ** (c + 1) - x1 ** (c + 1))

def certainty_equivalent(a, eu, c):
    return (eu / a) ** (1 / c)

def risk_premium(ev, ce):
    return ev - ce

results = []
for variant in variants:
    a = variant["a"]
    c = variant["c"]
    x1 = variant["x1"]
    x2 = variant["x2"]

    ev = expected_value(x1, x2)
    eu = expected_utility(a, x1, x2, c)
    ce = certainty_equivalent(a, eu, c)
    rp = risk_premium(ev, ce)

    if c > 1:
        risk_attitude = "Схильність до ризику"
    elif 0 < c < 1:
        risk_attitude = "Уникнення ризику"
    else:
        risk_attitude = "Нейтральний до ризику"

    results.append({
        "Сподіваний виграш": ev,
        "Детермінований еквівалент": ce,
        "Премія за ризик": rp,
        "Ставлення до ризику": risk_attitude
    })

for i, result in enumerate(results, start=1):
    print(f"Варіант {i}:")
    print(f"Сподіваний виграш: {result['Сподіваний виграш']:.2f}")
    print(f"Детермінований еквівалент: {result['Детермінований еквівалент']:.2f}")
    print(f"Премія за ризик: {result['Премія за ризик']:.2f}")
    print(f"Ставлення до ризику: {result['Ставлення до ризику']}")
    print("-" * 40)
