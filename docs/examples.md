Examples
=======================

## Quick Start Example: Time-Series
<br>

First example is for quick start. This library can be directly used to for any time-series, to align elements of them iteratively:
```python
# time-series to be aligned with dynamic time warping "so far":
time_series_a = np.random.rand(100, 1)
time_series_b = np.random.rand(35,1)

final_path, dtw_matrix, onthefly_alignment, onthefly_path = dtwsofar.dtw_onthefly_classification(time_series_a, time_series_b)
```

<br>

## Multimodal Example: Vision and Language Alignment
This use case demonstrates performing dynamic time warping so-far on image and natural language embeddings from Open AI's CLIP Model, so as to align them.
```python
import importlib
import numpy as np
dtwsofar = importlib.import_module('dtw-sofar.dtw_sofar')

video_features = np.load('CLIP_video_embeddings_path')
text_features = np.load('CLIP_text_embeddings_path')

# iterates over each RGB frame's CLIP embeddings and classifies matching text embeddings on-the-fly:
final_path, dtw_matrix, onthefly_predictions, onthefly_path = dtwsofar.dtw_onthefly_classification(video_features, text_features)
```
<br>

## Dynamic Time Warping Matrices

If desired, the dynamic time warping cost and backpointer matrices can be retrieved standalone. This is the default behavior within dtw_onthefly_classification:

```python
# time-series to be aligned with dynamic time warping "so far":
video_features = np.load('CLIP_video_embeddings_path')
text_features = np.load('CLIP_text_embeddings_path')

get_initial_matrices(frame_features, text_features)
```
<br>

## Cost Metrics and Regular Dynamic Time Warping
For completeness, this package also provides the regular dynamic time warping algorithm implementation (where instead of iterative stimuli, the entirety of the time series are used for alignment). Here, any cost metric function (including the provided cosine similarity cost_metric) can be used:

```python
a = np.random.rand(100, 1)
b = np.random.rand(35,1)

alignment_path, dtw_matrix= dtw(a, b, cost_metric)
```