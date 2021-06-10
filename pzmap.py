#
# Copyright (c) 2011 Christopher Felton
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# The following is derived from the slides presented by
# Alexander Kain for CS506/606 "Special Topics: Speech Signal Processing"
# CSLU / OHSU, Spring Term 2011.


import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np


def pzmap(z, p, filename=None, ztransform=False):
    """Plot the complex z-plane given a transfer function.
    """

    # get a figure/plot
    ax = plt.subplot(111)

    if ztransform:
        # create the unit circle
        uc = patches.Circle((0, 0), radius=1, fill=False,
                            color='black', ls='dashed')
        ax.add_patch(uc)

    # Plot the zeros and set marker properties
    t1 = plt.plot(z.real, z.imag, 'go', ms=10)
    plt.setp(t1, markersize=10.0, markeredgewidth=1.0,
             markeredgecolor='k', markerfacecolor='g')

    # Plot the poles and set marker properties
    t2 = plt.plot(p.real, p.imag, 'rx', ms=10)
    plt.setp(t2, markersize=12.0, markeredgewidth=3.0,
             markeredgecolor='r', markerfacecolor='r')

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # set the ticks
    max_tick = np.ceil(np.amax(np.abs(np.concatenate(
                   [z.imag, p.imag, z.real, p.real]
               ))))
    _ticks = np.arange(start=-max_tick, stop=max_tick+0.5, step=0.5)

    r = 1.5
    plt.axis('scaled')
    plt.axis([-r, r, -r, r])
    plt.xticks(_ticks)
    plt.yticks(_ticks)

    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)
