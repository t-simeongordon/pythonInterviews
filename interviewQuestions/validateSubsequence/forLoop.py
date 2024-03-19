def isValidSubsequence(array, sequence):
  """
  Checks if a sequence is a subsequence of another array.

  Args:
      array: The main array.
      sequence: The subsequence to check.

  Returns:
      True if the sequence is a subsequence of the array, False otherwise.
  """

  seq_idx = 0

  # Loop through the array using a for loop
  for num in array:
    # Check if current element matches
    if num == sequence[seq_idx]:
      seq_idx += 1  # Move to the next element in the sequence
      # Check if all elements in sequence are found
      if seq_idx == len(sequence):
        return True  # Early return if all elements found

  # If the loop finishes without finding all elements, it's not a subsequence
  return False

# Example usage
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

result = isValidSubsequence(array, sequence)
print(result)  # Output: True
