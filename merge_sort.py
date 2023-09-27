import pandas as pd

def merge_sort(data):
  if len(data) <= 1:
    return data

  mid = len(data) // 2
  left = merge_sort(data.iloc[:mid])
  right = merge_sort(data.iloc[mid:])

  return merge(left, right)

def merge(left, right):
  final = pd.DataFrame()
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left.iloc[i][3] <= right.iloc[j][3]:
      final = final._append(left.iloc[i], ignore_index=True)
      i += 1
    else:
      final = final._append(right.iloc[j], ignore_index=True)
      j += 1

  # Handle the case where either left or right is empty.
  if i < len(left):
    final = final._append(left.iloc[i:], ignore_index=True)
  elif j < len(right):
    final = final._append(right.iloc[j:], ignore_index=True)

  return final

# Read the data from the CSV file.
data = pd.read_csv("./data.csv")

# Group the data by zone.
s = data.groupby('zone')

# Get the north and south dataframes.
north = s.get_group('north')
south = s.get_group('south')

# Sort the north and south dataframes.
north_out = merge_sort(north)
south_out = merge_sort(south)

print(north_out.iloc[-1])
print(south_out.iloc[-1])
