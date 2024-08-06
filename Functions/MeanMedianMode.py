from collections import Counter
import statistics

def calculate_mean_median_mode(numbers):
    """
    Calculates the mean, median, and mode of a list of numbers.

    Parameters:
    - numbers: list of numbers

    Returns:
    - mean: mean of the numbers
    - median: median of the numbers
    - mode: mode of the numbers
    - explanation: step-by-step explanation of the calculations
    """
    explanation = []
    
    # Mean
    mean = sum(numbers) / len(numbers)
    explanation.append(f"Mean: Sum of numbers divided by count: {sum(numbers)}/{len(numbers)} = {mean}")
    
    # Median
    sorted_numbers = sorted(numbers)
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        explanation.append(f"Median: Average of middle two numbers: ({sorted_numbers[mid - 1]} + {sorted_numbers[mid]}) / 2 = {median}")
    else:
        median = sorted_numbers[mid]
        explanation.append(f"Median: Middle number in sorted list: {median}")
    
    # Mode
    mode_data = Counter(numbers)
    mode = statistics.multimode(numbers)
    explanation.append(f"Mode: Most frequent number(s): {mode}")
    
    return mean, median, mode, "\n".join(explanation)

# Example usage
# numbers = [4, 2, 5, 2, 3, 3, 1]
# mean, median, mode, explanation = calculate_mean_median_mode(numbers)
# print(explana