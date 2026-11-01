# Latihan 3: Test case status kelulusan

def status_lulus(nilai):
    if nilai > 60:  # Bug: seharusnya >= 60
        return "Lulus"
    return "Tidak lulus"


test_cases = [
    (59, "Tidak lulus"),
    (60, "Lulus"),
    (61, "Lulus"),
]

for nilai, expected in test_cases:
    actual = status_lulus(nilai)
    status = "PASS" if actual == expected else "FAIL"
    print(f"Nilai={nilai} | Expected={expected} | Actual={actual} | {status}")
