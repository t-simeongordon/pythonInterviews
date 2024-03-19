def isValidSubsequence(array, sequence):
  """
  Checks if a sequence is a subsequence of another array.

  Args:
      array: The main array.
      sequence: The subsequence to check.

  Returns:
      True if the sequence is a subsequence of the array, False otherwise.
  """

  arr_idx = 0
  seq_idx = 0

  # Loop through the array using a while loop
  while arr_idx < len(array) and seq_idx < len(sequence):
    # Check if current elements match
    if array[arr_idx] == sequence[seq_idx]:
      seq_idx += 1  # Move to the next element in the sequence
    arr_idx += 1  # Always move to the next element in the array

  # If we've found all elements in the sequence, return True
  return seq_idx == len(sequence)

# Example usage
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

result = isValidSubsequence(array, sequence)
print(result)  # Output: True
