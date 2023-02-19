import numpy as np
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


# prepare initial cost_matrix and backpointers matrix
def get_initial_matrices(frame_features, text_features):
  n = frame_features.shape[0] 
  m = text_features.shape[0] 
  
  # cost matrix (n+1, m+1): 
  cost_matrix = np.zeros((n+1, m+1)) # ensures dtw_matrix[0,0] == 0
  for i in range(1, n+1): 
    cost_matrix[i,0]  = np.inf
  for i in range(1,m+1):
    cost_matrix[0, i]  = np.inf

  # backpointer matrix (n, m):
  backpointers = np.zeros((n, m)) 
  return cost_matrix, backpointers

def dtw_cost(features_a, features_b):
    cos_similarity = np.dot(features_a, features_b) / (np.linalg.norm(features_a) * np.linalg.norm(features_b))
    return 1 - cos_similarity

def dtw_onthefly_classification(image_features, text_features):
  cost_matrix, backpointers = get_initial_matrices(image_features, text_features)
  
  onthefly_predictions = list() # "on the fly" predictions
  onthefly_path = list()
  for i in range(len(image_features)): # iterate across all video frames

    # retrieve alignment path (i elements long) "so far":
    path_sofar, cost_matrix, backpointers, current_predicted_idx = dtw_sofar(image_features[i], text_features, i, cost_matrix, backpointers, dtw_cost)
    # print(cost_matrix[i+1])

    # retrieve matching text prediction for the ith video frame, based on temporal knowledge
    # on the previous i-1 video frames' similarities with the text_features
    onthefly_predictions.append(current_predicted_idx)
    onthefly_path.append(path_sofar[i])
  
  final_path = path_sofar
  return final_path, cost_matrix[1:, 1:], onthefly_predictions, onthefly_path



'''
dynamic time warping that examines the series seen "so far"
'''
def dtw_sofar(current_image_features, text_features, current_frame_idx, cost_matrix_sofar, 
                        backpointers, dtw_cost_fn, matching_model = None, device = None):
  m = text_features.shape[0] # number of text annotations
  i = current_frame_idx 

  # examine all rows of the current row (that corresponds to the current video frame: i+1st row)
  for j in range(0,m):
    temporal_neighbors = [cost_matrix_sofar[i, j], cost_matrix_sofar[i, j+1], cost_matrix_sofar[i+1, j]]
    backptr_idx = np.argmin(temporal_neighbors)

    temporal_penalty = temporal_neighbors[backptr_idx]
    
    backpointers[i,j] = backptr_idx
    # cost based on matching_function:
    if matching_model:
      cost_matrix_sofar[i+1, j+1] = dtw_cost_fn(current_image_features, text_features[j], matching_model, device) + temporal_penalty
      continue
    # cost based on cosine similarity:
    cost_matrix_sofar[i+1, j+1] = dtw_cost_fn(current_image_features, text_features[j]) + temporal_penalty
    

  #####
  # Trace back to get alignment path (operating in backpointers matrix coordinate frame (n x m)):
  #####
  # get argmin of the current (i+1 st) row: best matching text feature's idx for the current video frame (text feature that minimizes alignment cost)
  cost_matrix = cost_matrix_sofar[1:, 1:] # strip off infs
  j = np.argmin(cost_matrix[i]) 
  current_predicted_idx = j 

  i = current_frame_idx
  # TODO: think about whether you should require j to = m (when i == n-1)? regular DTW traces back from [n-1, m-1].
  # this ensures for the last video frame is aligned with last text instruction (however, only for last step)
  # how would final predictions be different without setting this constraint?
  # (always tracing back from cost[i, argmin[dtw_matrix[i]]] to cost[0,0], including last iteration)
  # if i == cost_matrix_sofar.shape[0]-2:
    # cost_matrix_sofar.shape[0] is n+1, so n-1 is cost_matrix_sofar.shape[0]-2
    # j = m - 1

  # get alignment: trace back from dtw_matrix[i, argmin[dtw_matrix[i]]] to dtw_matrix[0,0]:
  alignment_path = [(i,j)] 
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

  return alignment_path[::-1], cost_matrix_sofar, backpointers, current_predicted_idx

