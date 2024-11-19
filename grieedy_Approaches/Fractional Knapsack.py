def fractional_knapsack(capacity, items):
    # Sort items by value-to-weight ratio
    items.sort(key=lambda x: x[1] / x[2], reverse=True)

    total_value = 0
    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break

    return total_value

# Example
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50
print("Maximum Value:", fractional_knapsack(capacity, items))
