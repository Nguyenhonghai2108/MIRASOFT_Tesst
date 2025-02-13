import pandas as pd

def find_top_20_percent_largest_age_difference(file_path: str):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Ensure the age column exists
    if "age" not in df.columns:
        raise ValueError("The dataset must contain an 'age' column")

    # Convert to a list of ages
    ages = df["age"].tolist()
    
    # Compute the average age difference for each person
    avg_differences = []
    for i in range(len(ages)):
        age_diffs = [abs(ages[i] - ages[j]) for j in range(len(ages)) if i != j]
        avg_differences.append(sum(age_diffs) / len(age_diffs))

    # Add the results to the dataframe
    df["avg_age_diff"] = avg_differences
    
    # Sort by the age difference in descending order
    df_sorted = df.sort_values(by="avg_age_diff", ascending=False)
    
    # Select the top 20%
    top_20_percent_count = int(len(df) * 0.2)
    top_20_percent = df_sorted.head(top_20_percent_count)

    return top_20_percent

# Example usage
file_path = "city_population.csv"
top_people = find_top_20_percent_largest_age_difference(file_path)
print(top_people)
