import pandas as pd

df = pd.read_csv("dataset.csv")

print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna(0)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nData cleaned successfully!")
