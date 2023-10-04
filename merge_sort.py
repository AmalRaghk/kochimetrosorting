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

  if i < len(left):
    final = final._append(left.iloc[i:], ignore_index=True)
  elif j < len(right):
    final = final._append(right.iloc[j:], ignore_index=True)

  return final


data = pd.read_csv("./data.csv")


s = data.groupby('zone')


north = s.get_group('North')
south = s.get_group('South')
east=s.get_group('East')
west=s.get_group('West')


north_out = merge_sort(north)
south_out = merge_sort(south)
west_out  = merge_sort(west)
east_out = merge_sort(east)

print(north_out.iloc[-1])
print(south_out.iloc[-1])
north_out.to_csv('north.csv',index=False)
south_out.to_csv('south.csv',index=False)
west_out.to_csv('east.csv',index=False)
east_out.to_csv('west.csv',index=False)