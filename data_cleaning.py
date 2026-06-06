import pandas as pd
print("Script started")
# Load dataset
df = pd.read_csv("superstore.csv")

# Original shape
print("Original Shape:", df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicates
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

# Remove duplicates
df = df.drop_duplicates()

# Convert date columns
df["Order.Date"] = pd.to_datetime(df["Order.Date"])
df["Ship.Date"] = pd.to_datetime(df["Ship.Date"])

# Check data types
print("\nData Types:")
print(df.dtypes)

# Remove missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv("superstore_cleaned.csv", index=False)

print("\nCleaning Completed Successfully!")
print("Final Shape:", df.shape)