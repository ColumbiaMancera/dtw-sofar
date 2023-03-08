# dtw-sofar

[![License](https://img.shields.io/github/license/egeozguroglu/dtw-sofar.svg)](https://github.com/egeozguroglu/dtw-sofar)
![GitHub issues](https://img.shields.io/github/issues/egeozguroglu/dtw-sofar)

[![Build Status](https://github.com/egeozguroglu/dtw-sofar/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/egeozguroglu/dtw-sofar/actions?query=workflow%3A%22Build+Status%22)

[![codecov](https://codecov.io/gh/egeozguroglu/dtw-sofar/branch/main/graph/badge.svg)](https://codecov.io/gh/egeozguroglu/dtw-sofar)


# Overview

This library implements the "Dynamic Time Warping Algorithm" for multimodal research in a way it can warp the time series received "so far." In other words, it modifies the algorithm to be compatible with 'iterative stimuli' (when future points in the time series are received one by one). 

One motivating application is aligning natural language annotations and video frames for research on Visual Language Models (e.g. CLIP), when the latter's embeddings are received frame by frame (e.g. we're making observations and don't have access to future frames). With "dtw-sofar," we can predict optimally matching annotations to new video frames on the fly - by relying on temporal information available "so far."
