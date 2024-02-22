def process_numbers_and_find_extremes(items):
    numeric_values = set()

    # Attempt to parse each item as a number if it's a string
    for item in items:
        if item is None or item == "":  # Skip None and empty strings
            continue
        try:
            # Try converting to float first (to include integers and floats)
            numeric_value = float(item)
            numeric_values.add(numeric_value)
        except ValueError:
            # Skip items that cannot be converted to a number
            continue

    # Check if we have enough numeric values to find extremes
    if len(numeric_values) == 0:
        return {"smallest": None, "center": None, "largest": None}
    
    sorted_values = sorted(numeric_values)
    smallest = sorted_values[0]
    largest = sorted_values[-1]
    
    # Find the middle value
    middle_index = len(sorted_values) // 2
    middle = sorted_values[middle_index] if len(sorted_values) % 2 != 0 else sorted_values[middle_index - 1]

    return {"smallest": smallest, "center": middle, "largest": largest}

if __name__ == "__main__":
    # Example input
    items = [
        "30.7 °C",
        "FLIR",
        "30.5",
        "19.0",
        "30.7",
        "°",
        "C",
        "FLIR",
        "30.5",
        "19.0",
        "",
        None
    ]

    result = process_numbers_and_find_extremes(items)
    print(result)
