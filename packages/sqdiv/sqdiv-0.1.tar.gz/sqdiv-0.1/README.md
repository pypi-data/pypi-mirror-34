# squarest-divisors

A small utility to compute the squarest pair of divisors for an integer.

# Installation

Install from PyPI:

```
$ pip install sqdiv
```

# Usage

The original intended usage is with `matplotlib`, to automatically figure out how many rows and columns are needed based on the number of subplots I actually need to plot.

Let's say I had a series of 11 things I needed to plot on a `matplotlib` figure, something akin to a [`seaborn.FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html), but with some custom things added.

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from sqdiv import n_rows_cols

height = 3
nrows, ncols = n_rows_cols(len(labels))  # len(labels) == 11
fig = plt.figure(figsize=(ncols * height, nrows * height))
gs = GridSpec(nrows=nrows, ncols=ncols)

# Now, setup the axes to plot on.
axes = dict()
for i, c in enumerate(labels):
    # This allows us to share axes across the plots.
    if i != 0:
        axes[c] = fig.add_subplot(gs[i], sharey=axes[labels[0]])
    else:
        axes[c] = fig.add_subplot(gs[i])
    axes[c].set_title(f'{c}')
    axes[c].set_xlabel('x')
    axes[c].set_ylabel('y')

# Below here, plot to your heart's content on each axes object.
```

The trivial case (1 by number of items) is not provided as part of the functionality because, hey, it's trivial!

# Feature Requests

Contributions are welcome. If you'd like to submit something, let's discuss on the [GitHub Issues tracker](https://github.com/ericmjl/squarest-divisors/issues) first.

Because `sqdiv` is currently maintained by volunteers and has no fiscal support, any feature requests will be prioritized according to what maintainers encounter as a need in our day-to-day jobs. Please temper expectations accordingly.
