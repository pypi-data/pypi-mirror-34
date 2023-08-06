import tfields
import numpy as np
import matplotlib.pyplot as plt


def plot_tile_loads(loads, **kwargs):
    loads = np.array(loads)
    loads = loads.reshape((-1, 29)).T
    axis = kwargs.pop('axis', tfields.plotting.gca(2))
    mask = kwargs.pop('mask', None)
    if mask is not None:
        mask = mask.reshape((-1, 29)).T
        vmin = kwargs.get('vmin', None)
        vmax = kwargs.get('vmax', None)
        cmap = kwargs.get('cmap', None)
        loads = tfields.plotting.to_colors(loads,
                                           cmap=cmap, vmin=vmin, vmax=vmax)
        alphas = np.ones(mask.shape)
        alphas[mask] = 0.
        loads[:, :, -1] = alphas
    artist = axis.imshow(loads, **kwargs)
    axis.set_xticks(np.array([0, 30, 54, 84, 113]) - 0.5)
    axis.set_xticks(np.arange(-0.5, 112.5, 1), minor=True)
    axis.set_yticks(np.arange(-0.5, 28.5, 1), minor=True)
    plt.rc('grid', linestyle="solid", color='black')
    axis.grid(color='k', which='minor')
    axis.tick_params(
        axis='minor',  # changes apply to both axis
        which='both',  # both major and minor ticks are affected
        bottom='off',  # ticks along the bottom edge are off
        top='off',  # ticks along the top edge are off
        labelbottom='off')  # labels along the bottom edge are off
    axis.tick_params(
        axis='both',  # changes apply to both axis
        which='major',  # both major and minor ticks are affected
        bottom='off',  # ticks along the bottom edge are off
        top='on',  # ticks along the top edge are off
        labelbottom='off')  # labels along the bottom edge are off
    axis.yaxis.set_ticks_position('none')
    plt.setp(axis.get_yticklabels(), visible=False)
    return artist
