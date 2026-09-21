# Computational Analysis of Collatz Trajectory Scaling Laws

## 📌 Overview
This repository contains computational research focused on the statistical properties and scaling behaviors of the **Collatz Conjecture** (also known as the $3n + 1$ problem). The primary objective is to investigate the relationship between the peak values of a trajectory and the distance (number of steps) required to reach those peaks.

## 🧬 Mathematical Objective
The research explores the empirical observation of a **Peak-Distance Scaling Law**. By analyzing a large sample of trajectories, I aim to quantify the distribution of $\text{max}(T(n))$ relative to the stopping time $\sigma(n)$, seeking to identify if the growth follows a predictable stochastic or deterministic scaling pattern.

## 🛠️ Technical Stack
- **Language:** Python 3.x
- **Core Libraries:** 
  - `NumPy`, `SciPy`, `Matplotlib`

## 📈 Key Findings & Visualizations

### Collatz Landscape
![collatz landscape](./collatz_landscape.png)

### Peak-Distance Scaling
![peak distance](./collatz_peak_distances.png)


## 🚀 How to Run
```bash
pip install numpy scipy matplotlib
python collatz_analysis.py
