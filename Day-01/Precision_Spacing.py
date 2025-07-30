import numpy as np

print("\nTesting Precision:")
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3?", (0.1 + 0.2) == 0.3)

gap_at_one = np.spacing(1)
print(f"\nGap at 1.0: {gap_at_one}")
print(f"Is 1.0 == (1.0 + gap_at_one/2)? {1.0 == (1.0 + gap_at_one/2)}")
print(f"Is 1.0 == (1.0 + gap_at_one)? {1.0 == (1.0 + gap_at_one)}")

num = 1e9
gap_at_one = np.spacing(num)
print(f"\nGap at {num}: {gap_at_one}")
print(f"Is {num} == ({num} + {gap_at_one}/3)? {num == (num + gap_at_one/3)}")
print(f"Is {num} == ({num} + {gap_at_one})? {num == (num + gap_at_one)}")
