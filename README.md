# Moment of Inertia Analysis

This project analyses rotational motion data from a first-year physics lab using Python, focusing on angular velocity, uncertainty visualisation, and linear regression.

## Overview


The analysis includes:

* Plotting angular velocity against time for different configurations  
* Visualisation of measurement uncertainty using error bars  
* Linear regression to determine angular acceleration  
* Comparison of inner and outer mass distributions through fitted models  

## Data

The following datasets are used:

* `inner-ring-averaged-data.csv`  
* `outer-ring-averaged-data.csv`  

These should be placed in the `data/` directory.


## Project Structure

```
moment-of-inertia-analysis/
│
├── data/              # Experimental datasets (CSV files)
├── figures/           # Generated plots
├── src/               # Analysis scripts and core logic
│   └── analysis.py    # Main analysis script
│
├── report/            # Full lab report
├── README.md          # Project overview and documentation
├── .gitignore         # Files ignored by Git
```

## How to Run

1. Install required packages:

```
pip install numpy matplotlib scipy
```

2. Run the script:

```
python src/analysis.py
```

3. Output:

* A plot showing angular velocity vs time with fitted models  
* Figure saved in `figures/angular_velocity_plot.png`

## Methods

* Linear model:  
  ω(t) = ω₀ + αt  
* Linear regression using `linregress`  
* Uncertainty visualisation using standard error of the mean  

## Results

* Angular velocity trends were visualised for different configurations  
* Linear fits were used to extract angular acceleration  
* Differences in gradients reflect changes in moment of inertia

<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/33a351c4-34c5-481f-9ef0-566f0dc8655f" />


## Technologies Used

* Python  
* NumPy  
* Matplotlib  
* SciPy

## Notes

The calculation of angular acceleration and moment of inertia is not included in this script, as the original experimental context and parameters were not fully recoverable during reconstruction.

The full methodology, results, and discussion are provided in the accompanying lab report PDF.
