import pandas as pd

df = pd.read_csv("talentscope_candidates_5000.csv")

print(df.shape)  # (5000, 11)

# Count candidates by job role
print(df["job_role"].value_counts())

# Average expected salary by job role
print(df.groupby("job_role")["expected_salary"].mean())

# Find experienced Python developers
result = df[
    (df["job_role"] == "Python Developer") &
    (df["experience_years"] >= 3)
]

print(result)

# Count application statuses
print(df["status"].value_counts())