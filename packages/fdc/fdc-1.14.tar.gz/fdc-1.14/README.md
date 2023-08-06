# Fast density clustering (fdc)
Python package for clustering low-dimensional data using kernel density maps and density graph. Examples for gaussian mixtures and some benchmarks are provided. Our algorithm solves multiscale problems (multiple variances/densities and population sizes) and works for non-convex clusters. It uses cross-validation and is regularized by two main global parameters : a neighborhood
size and a noise threshold measure. The later detects spurious cluster centers while the former guarantees that only local information is used to infer cluster centers. 

The underlying code is based on fast KD-trees for nearest-neighbor searches. For low-dimensional spaces, the algorithm has a O(n log n), where n is the size of the dataset. Is also has a memory complexity of O(n).

# Installing
I suggest you install the code using ```pip``` from an [Anaconda](https://conda.io/docs/user-guide/tasks/manage-environments.html) Python 3 environment. From that environment:
```
git clone https://github.com/alexandreday/fast_density_clustering.git
cd fast_density_clustering
pip install .
```
That's it ! You can now import the package ```fdc``` from your Python scripts. Check out the examples
in the file ```example``` and see if you can run the scripts provided.
# Examples and comparison with other methods
Check out the example for gaussian mixtures (example.py). You should be able to run it directly. It
should produce a plot similar to this: ![alt tag](https://github.com/alexandreday/fast_density_clustering/blob/master/example/result.png)

In another example (example2.py), the algorithm is benchmarked against some sklearn datasets (note that the same parameters are used across all datasets). This is to be compared with other clustering methods easily accesible from [sklearn](http://scikit-learn.org/stable/modules/clustering.html).

![alt tag](https://github.com/alexandreday/fast_density_clustering/blob/master/example/sklearn_datasets.png)

# Citation
If you use this code in a scientific publication, I would appreciate citation/reference to this repository. Also, for further references on clustering
and machine learning check out our machine learning review:
```
@article{mehta2018high,
  title={A high-bias, low-variance introduction to Machine Learning for physicists},
  author={Mehta, Pankaj and Bukov, Marin and Wang, Ching-Hao and Day, Alexandre GR and Richardson, Clint and Fisher, Charles K and Schwab, David J},
  journal={arXiv preprint arXiv:1803.08823},
  year={2018}
}
```
