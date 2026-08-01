import pandas as pd
import numpy as np
import re
import random

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("bank_customers_2023_2025.csv")

print("="*60)
print("ORIGINAL SHAPE :", df.shape)
print("="*60)

# =====================================================
# STANDARDIZE MISSING VALUES
# =====================================================

missing_values = [
    "",
    " ",
    "  ",
    "N/A",
    "NA",
    "NULL",
    "Null",
    "null",
    "Unknown",
    "UNKNOWN",
    "unknown"
]

df.replace(missing_values, np.nan, inplace=True)

# =====================================================
# REMOVE COMPLETE DUPLICATE ROWS
# =====================================================

duplicate_rows = df.duplicated().sum()

print(f"Duplicate Rows Found : {duplicate_rows}")

df.drop_duplicates(inplace=True)

print(f"Rows Removed : {duplicate_rows}")

# =====================================================
# REMOVE DUPLICATE CUSTOMER NUMBER
# =====================================================

duplicate_customer = df["Customer No"].duplicated().sum()

print(f"Duplicate Customer Numbers : {duplicate_customer}")

df.drop_duplicates(subset="Customer No", keep="first", inplace=True)

print(f"Customer Duplicate Rows Removed : {duplicate_customer}")

# =====================================================
# REMOVE DUPLICATE ACCOUNT NUMBER
# =====================================================

duplicate_account = df["Account Number"].duplicated().sum()

print(f"Duplicate Account Numbers : {duplicate_account}")

df.drop_duplicates(subset="Account Number", keep="first", inplace=True)

print(f"Account Duplicate Rows Removed : {duplicate_account}")

# =====================================================
# CLEAN CUSTOMER NAME
# =====================================================

df["Customer Name"] = (
    df["Customer Name"]
    .astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.title()
)

# =====================================================
# CLEAN CITY
# =====================================================

df["City"] = (
    df["City"]
    .astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.title()
)

# =====================================================
# STANDARDIZE GENDER
# =====================================================

gender_map = {
    "male":"Male",
    "MALE":"Male",
    "Male":"Male",
    "female":"Female",
    "FEMALE":"Female",
    "Female":"Female"
}

df["Gender"] = df["Gender"].replace(gender_map)

# =====================================================
# STANDARDIZE ACCOUNT TYPE
# =====================================================

df["Account Type"] = (
    df["Account Type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# =====================================================
# STANDARDIZE DEBIT CARD COMPANY
# =====================================================

df["Debit Card Company"] = (
    df["Debit Card Company"]
    .astype(str)
    .str.strip()
    .str.title()
)

# =====================================================
# STANDARDIZE DEBIT CARD TYPE
# =====================================================

df["Debit Card Type"] = (
    df["Debit Card Type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# =====================================================
# CONVERT AGE WORDS TO NUMBERS
# =====================================================

age_words = {
"Zero":0,
"One":1,
"Two":2,
"Three":3,
"Four":4,
"Five":5,
"Six":6,
"Seven":7,
"Eight":8,
"Nine":9,
"Ten":10,
"Eleven":11,
"Twelve":12,
"Thirteen":13,
"Fourteen":14,
"Fifteen":15,
"Sixteen":16,
"Seventeen":17,
"Eighteen":18,
"Nineteen":19,
"Twenty":20,
"Twenty One":21,
"Twenty Two":22,
"Twenty Three":23,
"Twenty Four":24,
"Twenty Five":25,
"Twenty Six":26,
"Twenty Seven":27,
"Twenty Eight":28,
"Twenty Nine":29,
"Thirty":30,
"Thirty One":31,
"Thirty Two":32,
"Thirty Three":33,
"Thirty Four":34,
"Thirty Five":35,
"Thirty Six":36,
"Thirty Seven":37,
"Thirty Eight":38,
"Thirty Nine":39,
"Forty":40,
"Forty One":41,
"Forty Two":42,
"Forty Three":43,
"Forty Four":44,
"Forty Five":45,
"Forty Six":46,
"Forty Seven":47,
"Forty Eight":48,
"Forty Nine":49,
"Fifty":50,
"Fifty One":51,
"Fifty Two":52,
"Fifty Three":53,
"Fifty Four":54,
"Fifty Five":55,
"Fifty Six":56,
"Fifty Seven":57,
"Fifty Eight":58,
"Fifty Nine":59,
"Sixty":60,
"Sixty One":61,
"Sixty Two":62,
"Sixty Three":63,
"Sixty Four":64,
"Sixty Five":65,
"Sixty Six":66,
"Sixty Seven":67,
"Sixty Eight":68,
"Sixty Nine":69,
"Seventy":70
}

df["Age"] = df["Age"].replace(age_words)

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# =====================================================
# CLEAN CUSTOMER NUMBER
# =====================================================


# Make Customer No string
df["Customer No"] = df["Customer No"].astype(str).str.strip()

# Find invalid Customer Numbers
invalid_customer = ~df["Customer No"].str.fullmatch(r"\d{6}")

print(f"Invalid Customer Numbers Found : {invalid_customer.sum()}")

# Existing valid customer numbers
existing_numbers = set(df.loc[~invalid_customer, "Customer No"])

# Function to generate unique 6-digit number
def generate_customer_no():

    while True:

        number = str(random.randint(100000,999999))

        if number not in existing_numbers:

            existing_numbers.add(number)

            return number

# Replace invalid IDs
df.loc[invalid_customer, "Customer No"] = [
    generate_customer_no()
    for _ in range(invalid_customer.sum())
]

print("Invalid Customer Numbers Replaced Successfully.")

# =====================================================
# CLEAN BRANCH CODE
# =====================================================

df["Branch Code"] = pd.to_numeric(
    df["Branch Code"],
    errors="coerce"
)

# =====================================================
# CLEAN ACCOUNT BALANCE COLUMNS
# =====================================================

balance_cols = [
    c for c in df.columns
    if "Year End Balance" in c
]

for col in balance_cols:

    df[col] = (
        df[col]
        .astype(str)
        .str.replace("PKR","",regex=False)
        .str.replace(",","",regex=False)
        .str.strip()
    )

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# =====================================================
# CLEAN TRANSACTION COUNT COLUMNS
# =====================================================

txn_cols = [
    c for c in df.columns
    if "Transactions Count" in c
]

for col in txn_cols:

    df[col] = (
        df[col]
        .astype(str)
        .str.replace("txns","",regex=False)
        .str.replace("txn","",regex=False)
        .str.strip()
    )

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# =====================================================
# CLEAN DATES
# =====================================================

# =====================================================
# CLEAN DATES
# =====================================================

date_col = "Account Opening Date"

df[date_col] = (
    df[date_col]
    .astype(str)
    .str.strip()
)


def fix_date(value):

    if value in ["nan", "NaN", "", "None"]:
        return pd.NaT

    formats = [
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%d.%m.%Y",
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%m-%d-%Y",
        "%m/%d/%Y",
        "%d %B %Y",
        "%B %d, %Y"
    ]

    for fmt in formats:
        try:
            return pd.to_datetime(value, format=fmt)
        except:
            pass

    try:
        return pd.to_datetime(value, dayfirst=True)
    except:
        return pd.NaT


df[date_col] = df[date_col].apply(fix_date)


invalid_dates = df[date_col].isna().sum()

print(f"Invalid Dates Found: {invalid_dates}")


def generate_random_date():

    start = pd.Timestamp("2023-01-01")
    end = pd.Timestamp("2025-12-31")

    days = random.randint(
        0,
        (end - start).days
    )

    return start + pd.Timedelta(days=days)


df.loc[
    df[date_col].isna(),
    date_col
] = [
    generate_random_date()
    for _ in range(invalid_dates)
]
# =====================================================
# FILL MISSING VALUES
# =====================================================

# Numeric columns -> Median

numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Categorical columns -> Mode

categorical_cols = df.select_dtypes(include="object").columns

for col in categorical_cols:

    if df[col].isna().sum() > 0:

        df[col] = df[col].fillna(df[col].mode()[0])

# =====================================================
# DATE FORMAT
# =====================================================

df["Account Opening Date"] = (
    df["Account Opening Date"]
    .dt.strftime("%Y-%m-%d")
)

# =====================================================
# REPORT
# =====================================================

print("\n")

print("="*60)
print("FINAL SHAPE :", df.shape)
print("="*60)

print("\nRemaining Missing Values\n")

print(df.isna().sum())

print("\nData Types\n")

print(df.dtypes)

# =====================================================
# SAVE CLEAN FILE
# =====================================================

df.to_csv(
    "bank_customers_2023_2025_cleaned.csv",
    index=False
)

print("\nCleaning Completed Successfully.")
print("\n" + "="*70)
print("               DATA CLEANING REPORT")
print("="*70)


print(f"Final Rows                    : {len(df)}")

print(f"Duplicate Rows Removed        : {duplicate_rows}")
print(f"Duplicate Customer Removed    : {duplicate_customer}")
print(f"Duplicate Account Removed     : {duplicate_account}")
print(f"Invalid Customer IDs Fixed    : {invalid_customer.sum()}")

print(f"Missing Values Remaining      : {df.isna().sum().sum()}")

print("="*70)