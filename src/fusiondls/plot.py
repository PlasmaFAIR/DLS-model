import warnings

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D

from .typing import FloatArray

colors = ["teal", "darkorange", "firebrick", "limegreen", "magenta", "cyan", "navy"]


def plot_B_field_profile(
    inner_S: FloatArray,
    inner_B: FloatArray,
    inner_Xpoint: int,
    outer_S: FloatArray,
    outer_B: FloatArray,
    outer_Xpoint: int,
) -> plt.Axes:
    r"""Plot :math:`B_\mathrm{total}` as a function of
    :math:`S_{\parallel}` for the inner and outer divertors

    Note that :math:`S_{\parallel}` should go from target to midplane

    Parameters
    ----------
    inner_S :
        :math:`S_{\parallel}` for inner divertor
    inner_B :
        :math:`B_\mathrm{total}` for inner divertor
    inner_Xpoint : int
        Index of X-point in ``inner_S``
    outer_S :
        :math:`S_{\parallel}` for outer divertor
    outer_B :
        :math:`B_\mathrm{total}` for outer divertor
    outer_Xpoint : int
        Index of X-point in ``outer_S``

    Returns
    -------
    plt.Axes

    """

    _fig, ax = plt.subplots()
    size = 100

    def plot_side(s, btot, xpoint, color, label):
        ax.plot(s, btot, color=color, label=label)
        ax.scatter(s[xpoint], btot[xpoint], color=color, marker="x", s=size)
        ax.scatter(s[0], btot[0], color=color, marker="o", s=size)
        ax.scatter(s[-1], btot[-1], color=color, marker="d", s=size)

    plot_side(inner_S, inner_B, inner_Xpoint, colors[0], "Inner")
    plot_side(outer_S, outer_B, outer_Xpoint, colors[1], "Outer")

    ax.set_xlabel(r"$S_{\parallel}$ (m from target)")
    ax.set_ylabel(r"$B_{tot}$ (T)")
    ax.legend()

    h, _ = ax.get_legend_handles_labels()
    kwargs = {"color": "grey", "linewidth": 0, "markersize": 10}
    extra_handles = [
        Line2D([0], [0], marker="x", label="X-point", **kwargs),
        Line2D([0], [0], marker="o", label="Target", **kwargs),
        Line2D([0], [0], marker="d", label="Midplane", **kwargs),
    ]

    ax.legend(fontsize=12, handles=h + extra_handles)

    return ax


def colored_line(x, y, c, ax, **lc_kwargs):
    """
    Plot a line with a color specified along the line by a third value.

    It does this by creating a collection of line segments. Each line segment is
    made up of two straight lines each connecting the current (x, y) point to the
    midpoints of the lines connecting the current point with its two neighbors.
    This creates a smooth line with no gaps between the line segments.

    Taken from Matplotlib examples

    Parameters
    ----------
    x, y : array-like
        The horizontal and vertical coordinates of the data points.
    c : array-like
        The color values, which should be the same size as x and y.
    ax : Axes
        Axis object on which to plot the colored line.
    **lc_kwargs
        Any additional arguments to pass to matplotlib.collections.LineCollection
        constructor. This should not include the array keyword argument because
        that is set to the color argument. If provided, it will be overridden.

    Returns
    -------
    matplotlib.collections.LineCollection
        The generated line collection representing the colored line.
    """
    if "array" in lc_kwargs:
        warnings.warn('The provided "array" keyword argument will be overridden')

    # Default the capstyle to butt so that the line segments smoothly line up
    default_kwargs = {"capstyle": "butt"}
    default_kwargs.update(lc_kwargs)

    # Compute the midpoints of the line segments. Include the first and last points
    # twice so we don't need any special syntax later to handle them.
    x = np.asarray(x)
    y = np.asarray(y)
    x_midpts = np.hstack((x[0], 0.5 * (x[1:] + x[:-1]), x[-1]))
    y_midpts = np.hstack((y[0], 0.5 * (y[1:] + y[:-1]), y[-1]))

    # Determine the start, middle, and end coordinate pair of each line segment.
    # Use the reshape to add an extra dimension so each pair of points is in its
    # own list. Then concatenate them to create:
    # [
    #   [(x1_start, y1_start), (x1_mid, y1_mid), (x1_end, y1_end)],
    #   [(x2_start, y2_start), (x2_mid, y2_mid), (x2_end, y2_end)],
    #   ...
    # ]
    coord_start = np.column_stack((x_midpts[:-1], y_midpts[:-1]))[:, np.newaxis, :]
    coord_mid = np.column_stack((x, y))[:, np.newaxis, :]
    coord_end = np.column_stack((x_midpts[1:], y_midpts[1:]))[:, np.newaxis, :]
    segments = np.concatenate((coord_start, coord_mid, coord_end), axis=1)

    lc = LineCollection(segments, **default_kwargs)
    lc.set_array(c)  # set the colors of each segment

    return ax.add_collection(lc)
