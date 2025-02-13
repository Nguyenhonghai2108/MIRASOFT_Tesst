import numpy as np
import pandas as pd
from scipy.spatial import distance_matrix

def find_top_10_percent_furthest_people(people_positions):
    """
    Finds the 10% of people who are the furthest away from others.

    :param people_positions: List of (x, y) positions of people.
    :return: DataFrame of the top 10% people who are the furthest.
    """
    # Convert positions to a NumPy array
    people_positions = np.array(people_positions)

    # Compute pairwise distances
    dist_matrix = distance_matrix(people_positions, people_positions)

    # Replace diagonal (self-distance) with a large value to avoid zero minimums
    np.fill_diagonal(dist_matrix, np.inf)

    # Find the nearest neighbor distance for each person
    min_distances = np.min(dist_matrix, axis=1)

    # Create a DataFrame
    df = pd.DataFrame(people_positions, columns=['x', 'y'])
    df['nearest_neighbor_distance'] = min_distances

    # Sort by distance in descending order
    df_sorted = df.sort_values(by='nearest_neighbor_distance', ascending=False)

    # Select top 10%
    top_10_percent_count = max(1, int(len(df) * 0.1))  # Ensure at least one person is selected
    top_10_percent = df_sorted.head(top_10_percent_count)

    return top_10_percent

# Example usage with random people positions
people_positions = [(1, 2), (3, 4), (10, 10), (8, 7), (2, 2), (20, 20), (30, 30), (40, 40)]
top_people = find_top_10_percent_furthest_people(people_positions)
print(top_people)
