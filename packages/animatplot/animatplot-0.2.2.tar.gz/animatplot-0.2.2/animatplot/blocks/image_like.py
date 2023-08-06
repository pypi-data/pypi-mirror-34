from .base import Block
import matplotlib.pyplot as plt
import numpy as np


class Pcolormesh(Block):
    """Animates a pcolormesh

    Parameters
    ----------
    X : 2D np.ndarray, optional
    Y : 2D np.ndarray, optional
    C : list of 2D np.ndarray or a 3D np.ndarray
    axis : matplotlib axis, optional
        an axis to attach the block to.
    t_axis : int, optional
        The axis of the array that represents time. Defaults to 0.
        No effect if C is a list.

    Notes
    -----
    All other keyword arguments get passed to ``axis.pcolormesh``
    see :meth:`matplotlib.axes.Axes.pcolormesh` for details.
    """
    def __init__(self, *args, axis=None, t_axis=0, **kwargs):
        if len(args) == 1:
            self.C = args[0]
            self._arg_len = 1
        elif len(args) == 3:
            self.X, self.Y, self.C = args
            self._arg_len = 3
            if len(self.X.shape) != 2 or len(self.Y.shape) != 2:
                raise TypeError('X, Y must be 2D arrays')
        else:
            raise TypeError(
                'Illegal arguments to pcolormesh; see help(pcolormesh)')

        super().__init__(axis, t_axis)

        self._is_list = isinstance(self.C, list)
        self.C = np.asanyarray(self.C)

        Slice = self._make_slice(0, 3)
        if self._arg_len == 1:
            self.quad = self.ax.pcolormesh(self.C[Slice], **kwargs)
        elif self._arg_len == 3:
            self.quad = self.ax.pcolormesh(self.X, self.Y, self.C[Slice],
                                           **kwargs)

    def _update(self, i):
        Slice = self._make_pcolormesh_slice(i, 3)
        self.quad.set_array(self.C[Slice].ravel())
        return self.quad

    def __len__(self):
        return self.C.shape[2]

    def _make_pcolormesh_slice(self, i, dim):
        if self._is_list:
            return i
        Slice = [slice(-1)]*3  # weird thing to make animation work
        Slice[self.t_axis] = i
        return tuple(Slice)


class Imshow(Block):
    """Animates a series of images

    Parameters
    ----------
    images : list of 2D/3D arrays, or a 3D or 4D array
        matplotlib considers arrays of the shape
        (n,m), (n,m,3), and (n,m,4) to be images.
        Images is either a list of arrays of those shapes,
        or an array of shape (T,n,m), (T,n,m,3), or (T,n,m,4)
        where T is the length of the time axis (assuming ``t_axis=0``).
    axis : matplotlib axis, optional
        The axis to attach the block to
    t_axis : int, optional
        The axis of the array that represents time. Defaults to 0.
        No effect if images is a list.

    Notes
    -----
    This block accepts additional keyword arguments to be passed to
    :meth:`matplotlib.axes.Axes.imshow`
    """
    def __init__(self, images, axis=None, t_axis=0, **kwargs):
        self.ims = np.asanyarray(images)
        super().__init__(axis, t_axis)

        self._is_list = isinstance(images, list)
        self._dim = len(self.ims.shape)

        Slice = self._make_slice(0, self._dim)
        self.im = self.ax.imshow(self.ims[Slice], **kwargs)

    def _update(self, i):
        Slice = self._make_slice(i, self._dim)
        self.im.set_array(self.ims[Slice])
        return self.im

    def __len__(self):
        if self._is_list:
            return self.ims.shape[0]
        return self.ims.shape[self.t_axis]
