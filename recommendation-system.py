import math

# Sample data: user ratings for different items (movies, books, products, etc.)
user_ratings = {
    'Alice': {'Item1': 5, 'Item2': 3, 'Item3': 4},
    'Bob': {'Item1': 3, 'Item2': 4, 'Item3': 2},
    'Charlie': {'Item1': 4, 'Item3': 5},
    'Dave': {'Item2': 4, 'Item3': 5}
}

# Calculate Pearson correlation coefficient between two users
def pearson_correlation(user1, user2):
    common_items = {item for item in user_ratings[user1] if item in user_ratings[user2]}
    
    n = len(common_items)
    if n == 0:
        return 0
    
    sum1 = sum(user_ratings[user1][item] for item in common_items)
    sum2 = sum(user_ratings[user2][item] for item in common_items)
    
    sum1_sq = sum(user_ratings[user1][item]**2 for item in common_items)
    sum2_sq = sum(user_ratings[user2][item]**2 for item in common_items)
    
    p_sum = sum(user_ratings[user1][item] * user_ratings[user2][item] for item in common_items)
    
    num = p_sum - (sum1 * sum2 / n)
    den = math.sqrt((sum1_sq - sum1**2 / n) * (sum2_sq - sum2**2 / n))
    if den == 0:
        return 0
    
    return num / den

# Get recommendations for a user
def get_recommendations(target_user):
    totals = {}
    sim_sums = {}
    
    for other_user in user_ratings:
        if other_user == target_user:
            continue
        sim = pearson_correlation(target_user, other_user)
        if sim <= 0:
            continue
        
        for item in user_ratings[other_user]:
            if item not in user_ratings[target_user] or user_ratings[target_user][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += user_ratings[other_user][item] * sim
                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim
    
    rankings = [(total / sim_sums[item], item) for item, total in totals.items()]
    rankings.sort(reverse=True)
    
    return rankings

# Main function to get and print recommendations for a user
def main():
    target_user = 'Alice'
    recommendations = get_recommendations(target_user)
    
    print(f"Recommendations for {target_user}:")
    for score, item in recommendations:
        print(f"{item}: {score:.2f}")

if __name__ == "__main__":
    main()
