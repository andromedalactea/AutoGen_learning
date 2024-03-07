# filename: pressure_plot.py

import matplotlib.pyplot as plt
import numpy as np

force = 50  # in Newtons
area = np.arange(1, 101)  # area varies between 1 to 100
pressure = force / area  # pressure = force/area

plt.plot(area, pressure)
plt.title('Pressure vs Area')
plt.xlabel('Area (m^2)')
plt.ylabel('Pressure (N/m^2)')
plt.grid(True)

# Save the figure in the current directory
plt.savefig('pressure_vs_area.png')
plt.show()