import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from pathlib import Path


# Defining Functions
def linear(x, m, c):
    return m*x + c

def main():
    # Define project paths
    project_root = Path(__file__).resolve().parent.parent
    data_dir = project_root / "data"
    figures_dir = project_root / "figures"

    inner_file = data_dir / "inner-ring-averaged-data.csv"
    outer_file = data_dir / "outer-ring-averaged-data.csv"
  
    # Slicing Data
    t_mid_inner, inner_omega, inner_error = np.loadtxt(
                              inner_file,
                              delimiter=',',
                              skiprows=1,
                              unpack=True
    )
    
    t_mid_outer, outer_omega, outer_error = np.loadtxt(
                              outer_file,
                              delimiter=',',
                              skiprows=1,
                              unpack=True
    )
    
    # Plotting
    plt.figure(figsize=(10,6))
    
    plt.errorbar(t_mid_inner, inner_omega, yerr=inner_error,
                 label='Inner Ring',
                 fmt='o',
                 capsize=3,
                 markersize=5
    )
    
    plt.errorbar(t_mid_outer, outer_omega, yerr=outer_error,
                 label='Outer Ring',
                 fmt='o',
                 capsize=3,
                 markersize=5
    )
    
    innerfit = linregress(t_mid_inner, inner_omega)
    outerfit = linregress(t_mid_outer, outer_omega)
    
    xfit_inner = np.linspace(np.min(t_mid_inner), np.max(t_mid_inner), 100)
    xfit_outer = np.linspace(np.min(t_mid_outer), np.max(t_mid_outer), 100)
    
    plt.plot(
        xfit_inner,
        linear(xfit_inner, innerfit.slope, innerfit.intercept),
        label='Inner Fit',
        color='tab:blue'
    )
    
    plt.plot(
        xfit_outer,
        linear(xfit_outer, outerfit.slope, outerfit.intercept),
        label='Outer Fit',
        color='tab:orange'
    )
    
    plt.ylabel(r"$\omega$ (rad/s)")
    plt.xlabel('t_mid (s)')
    
    plt.tight_layout()
    plt.legend()
    plt.savefig("figures/angular_velocity_plot.png", dpi=300)
    plt.show()
  
if __name__ == "__main__":
    main()
