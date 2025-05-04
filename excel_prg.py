"""import pandas as pd
df = pd.read_excel('marks.xlsx')  # Replace with a real file path
df["Total"] = df[["mark1", "mark2", "mark3", "mark4", "mark5"]].sum(axis=1)
df["Average"] = df[["mark1", "mark2", "mark3", "mark4", "mark5"]].mean(axis=1)
#df["total"] = df["name"]
print(df.columns)

df.to_excel("marks.xlsx")

print(df.head())"""

import pandas as pd

# Step 1: Load the Excel file
df = pd.read_excel("marks.xlsx")

# Step 2: Automatically find columns starting with 'mark'
subjects=["Tamil", "English", "Maths", "Science", "Social"]
mark_columns = [col for col in df.columns if col in subjects]

#mark_columns = [col for col in df.columns if col.lower().startswith("mark")]

# Step 3: Calculate total and average marks
df["Total"] = df[mark_columns].sum(axis=1)
df["Average"] = df[mark_columns].mean(axis=1)
df["Pass"] = df[mark_columns].ge(35).all(axis=1)


# Step 4: Save the result
df.to_excel("marks.xlsx", index=False)

# Step 5: Print first few rows
print(df.head())


"""grade
def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(get_grade)

topper
topper = df.loc[df["Total"].idxmax()]
print(topper)

subject wise topper
english_topper = df.loc[df["English"].idxmax()]
for subject in mark_columns:
    topper = df.loc[df[subject].idxmax(), ["name", subject]]
    print(f"{subject} Topper: {topper['name']} - {topper[subject]} marks")
"""
    
