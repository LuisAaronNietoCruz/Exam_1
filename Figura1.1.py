#!/usr/bin/env python3
#
#    Example of dynamic system
#    Copyright (C) 2022  Victor De la Luz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1)

def f(x, b):
    return 2/3*x+b

plt.plot(x,[f(i,0) for i in x], 'r')
plt.plot(x,[f(i,1/3) for i in x], 'r')
plt.plot(x,[f(i,2/3) for i in x], 'r')
plt.plot(x,[f(i,-1/3) for i in x], 'r')



plt.xlim(0,1)
plt.ylim(0,1)
