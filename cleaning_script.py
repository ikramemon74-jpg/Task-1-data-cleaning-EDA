import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(0)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("Data cleaned successfully")
