Welcome to the sktime workshop at pydata global 2024
====================================================

This tutorial is about [skchange] and sktime [sktime].

`skchange` is a python compatible framework library for detecting anomalies, changepoints in time series, and segmentation.

`skchange` is based on, and extends, `sktime`, the most widely used scikit-learn compatible framework library for learning with time series.

Both packages are maintained under permissive license, easily extensible by anyone, and interoperable with the python data science stack.
This workshop gives a hands-on introduction to the new joint detection interface developed in skchange and sktime, for detecting point anomalies, changepoints, and segment anomalies.

[skchange]: https://skchange.readthedocs.io/en/latest/
[sktime]: https://www.sktime.net

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sktime/sktime-tutorial-pydata-global-2024/main?filepath=notebooks) [![!discord](https://img.shields.io/static/v1?logo=discord&label=discord&message=chat&color=lightgreen)](https://discord.com/invite/54ACzaFsn7) [![!slack](https://img.shields.io/static/v1?logo=linkedin&label=LinkedIn&message=news&color=lightblue)](https://www.linkedin.com/company/scikit-time/)

## :rocket: How to get started

In the tutorial, we will move through notebooks section by section.

You have different options how to run the tutorial notebooks:

* Run the notebooks in the cloud on [Binder] - for this you don't have to install anything!
* Run the notebooks on your machine. [Clone] this repository, get [conda], install the required packages (`sktime`, `seaborn`, `jupyter`) in an environment, and open the notebooks with that environment. For detail instructions, see below. For troubleshooting, see sktime's more detailed [installation instructions].
* or, use python venv, and/or an editable install of this repo as a package. Instructions below.

[Binder]: https://mybinder.org/v2/gh/sktime/sktime-tutorial-pydata-global-2024/main?filepath=notebooks
[clone]: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[conda]: https://docs.conda.io/en/latest/
[installation instructions]: https://www.sktime.net/en/latest/installation.html

Please let us know on the [sktime discord](https://discord.com/invite/54ACzaFsn7) if you have any issues during the conference, or join to ask for help anytime.

## :bulb: Description

The tutorial will give an introduction to the detection API in skchange and sktime, with a focus on unsupervised detection of anomalies and change points. The tutorial includes:

- An introduction to the different types of detection tasks for time series data: anomalies, changepoints, point/set/segment, un/supervised, stream, panel, uni/multivariate
- `skchange` and `sktime` for anomaly, changepoint detection
- cost and score functions for anomaly and changepoint detectors
- pipelines for anomaly and changepoint detection

`skchange` is developed at Norsk Regnesentral.

Both `skchange` and `sktime` are developed by open communities, with aims of ecosystem integration in a neutral, charitable space. We welcome contributions and seek to provides opportunity for anyone worldwide.

We invite anyone to get involved as a developer, user, supporter (or any combination of these).


## :movie_camera: Other Tutorials

- [EuroSciPy 2024 - Hierarchical, global forecasting, foundation models, extensions and marketplace](https://github.com/sktime/sktime-workshop-euroscipy2024)

- [Pydata Global 2023 - General sktime introduction, new features 2023](https://github.com/sktime/sktime-tutorial-pydata-global-2023)

- [Europython 2023 - General sktime introduction, half-day workshop](https://github.com/sktime/sktime-tutorial-europython-2023)

- [PyCon Prague 2023 - Forecasting, Advanced Pipelines, Benchmarking](https://github.com/sktime/sktime-tutorial-pydata-global-2023)

- [Pydata Amsterdam 2023 - Probabilistic prediction, forecasting, evaluation](https://github.com/sktime/sktime-tutorial-pydata-Amsterdam-2023)

- [ODSC Europe 2023 - Forecasting, Pipelines, and ML Engineering](https://github.com/sktime/sktime-tutorial-ODSC-Europe-2023)

- [Pydata London 2023 - Time Series Classification, Regression, Distances & Kernels](https://github.com/sktime/sktime-tutorial-pydata-london-2023)

- [Pydata Berlin 2022 - Advanced Forecasting Tutorial](https://www.youtube.com/watch?v=4Rf9euAhjNc)

- [Pydata London 2022 - How to implement your own estimator in sktime](https://www.youtube.com/watch?v=S_3ewcvs_pg)

- [Pydata Global 2022 - Feature extraction, Pipelines, Tuning](https://github.com/sktime/sktime-tutorial-pydata-global-2022)


## :wave: How to contribute

If you're interested in contributing to `skchange` or `sktime`,
you can find out more how to get involved [here](https://www.sktime.net/en/latest/get_involved.html).

Any contributions are welcome, not just code!

## Installation instructions for local use

To run the notebooks locally, you will need:

* a local repository clone
* a python environment with required packages installed

### Cloning the repository

To clone the repository locally:

`git clone https://github.com/sktime/sktime-tutorial-pydata-global-2024`

### Using conda env

1. Create a python virtual environment:
`conda create -y -n skchange_pydata python=3.11`
2. Install required packages:
`conda install -y -n skchange_pydata pip skchange sktime seaborn jupyter pmdarima statsmodels`
3. Activate your environment:
`conda activate skchange_pydata`
4. If using jupyter: make the environment available in jupyter:
`python -m ipykernel install --user --name=skchange_pydata`

### Using python venv

1. Create a python virtual environment:
`python -m venv skchange_pydata`
2. Activate your environment:
 - `source skchange_pydata/bin/activate` for Linux
 - skchange_pydata/Scripts/activate` for Windows
3. Install the requirements:
`pip install -r requirements`
4. If using jupyter: make the environment available in jupyter:
`python -m ipykernel install --user --name=skchange_pydata`
