# tf\_decompose

CP and Tucker tensor decompositions implemented in TensorFlow.

### Usage

```python
import tensorflow as tf
import numpy as np
from tf_decompose import KruskalTensor

X = np.array([[1, 2], [3, 4]], dtype=np.float32)
KT_X = KruskalTensor(X.shape, rank=2, dtype=tf.float32)
opt = tf.train.AdadeltaOptimizer(0.05)
X_predict = KT_X.train_als_early(X, opt, epochs=10000)
print(X_predict)
```

## Kruskal tensors

### Notes on ALS gradient computation

- For CP decomposition we use alternating least squares (ALS) over component matrices, but do not compute the exact solution as in Kolda & Bader (2009) due to the computational demands of computing large matrix inversions.
- In our tests we find inferior results to the exact solution descent method (requires inverting potentially huge matrices) implemented in `scikit-tensor` with ~.80 vs. ~.90 fit with decomposed rank-3 tensors on the Sensory Bread dataset.
- `tf-decompose` parallelized on GPU was approximately 20 times faster than `scikit-tensor` for a rank-200 decomposition of a random tensor with 60 million parameters.

## Tucker tensors

Preliminary results: with sensory bread data, `TuckerTensor.hosvd` seems to perform quite poorly, while `TuckerTensor.hooi` and `DecomposedTensor.train_als` learn reconstructions with fit ~0.70.

## References

- Bader, B. W., & Kolda, T. G. (2007). Efficient MATLAB computations with sparse and factored tensors. SIAM Journal on Scientific Computing, 30(1), 205-231. doi:10.2172/897641

- Kolda, T. G., & Bader, B. W. (2009). Orthogonal tensor decompositions. SIAM Journal on Scientific Computing, 51(3), 455-500. doi:10.2172/755101

- Nickel, M. [scikit-tensor](https://github.com/mnick/scikit-tensor)
