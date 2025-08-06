def flattenArray(nestedArray: list) -> list:
    """
    Flattens a deeply nested list of integers into a single, flat list,
    preserving the original order of elements.

    This function uses a recursive approach to traverse through the nested structure.
    It does NOT use the built-in .flat() method.

    Args:
        nestedArray: A list that may contain integers or other lists (nested arrays)
                     of integers.

    Returns:
        A single, flat list containing all integers from the nestedArray
        in their original order.
    """
    flat_list = [] # Initialize an empty list to store the flattened elements

    # Iterate through each element in the input nestedArray
    for element in nestedArray:
        # Check if the current element is an instance of a list.
        # This handles the problem's context where elements are either
        # integers or nested lists of integers.
        if isinstance(element, list):
            # If it's a nested list, recursively call flattenArray on this nested list.
            # Extend the current flat_list with the result of the recursive call.
            # Using extend() adds all elements from the returned list individually.
            flat_list.extend(flattenArray(element))
        else:
            # If the element is not a list (i.e., it's an integer according to problem description),
            # add it directly to our flat_list.
            flat_list.append(element)

    return flat_list

# Main execution block with a hardcoded example input

    # Example input as a hardcoded Python list literal.
    # This replaces the need for dynamic input reading from sys.stdin and parsing with ast.
    nested_array_example = [1, [2, 3], [4, [5, 6, 7]]]

    print(f"Input: {nested_array_example}")

    # Call the flattenArray function with the example input
    result = flattenArray(nested_array_example)

    # Print the flattened result
    print(f"Flattened: {result}")


