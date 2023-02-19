'''
regular dynamic time warping algorithm
''' 
def dtw(x, y, cost_metric):
  n = x.shape[0] # points in series x
  m = y.shape[0] # points in series y

  # cost matrix (n+1, m+1): 
  dtw_matrix = np.zeros((n+1, m+1)) # ensures dtw_matrix[0,0] == 0
  for i in range(1, n+1): 
    dtw_matrix[i,0]  = np.inf
  for i in range(1,m+1):
    dtw_matrix[0, i]  = np.inf
  print(dtw_matrix)
  
  # backpointer matrix (n, m):
  backpointers = np.zeros((n, m)) 

  for i in range(0, n):
    for j in range(0,m):
      temporal_neighbors = [dtw_matrix[i, j], dtw_matrix[i, j+1], dtw_matrix[i+1, j]]
      backptr_idx = np.argmin(temporal_neighbors)
      temporal_penalty = temporal_neighbors[backptr_idx]

      dtw_matrix[i+1, j+1] = cost_metric(x[i], y[j]) + temporal_penalty
      backpointers[i,j] = backptr_idx
  
  # get alignment: trace back from dtw_matrix[n,m] to dtw_matrix[0,0]:
  i = n-1
  j = m-1 
  alignment_path = [(i,j)] # dtw_matrix[n,m] has x[n-1] and y[m-1] aligned.
  while i > 0 or j > 0:
    backptr_type = backpointers[i,j]

    if backptr_type == 0: # "match"
      i -= 1
      j -= 1
    if backptr_type == 1: # "insertion"
      i -= 1
    elif backptr_type == 2:
      j -=1 # "deletion"
    alignment_path.append((i,j))

  # return alignment path and cost_matrix:
  return alignment_path[::-1], dtw_matrix[1:, 1:]
