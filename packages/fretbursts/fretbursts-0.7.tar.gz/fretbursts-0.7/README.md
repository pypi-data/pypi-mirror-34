FRETBursts
==========

[![DOI](https://zenodo.org/badge/5991/tritemio/FRETBursts.svg)](https://zenodo.org/badge/latestdoi/5991/tritemio/FRETBursts)
[![TravisCI Build Status](https://travis-ci.org/OpenSMFS/FRETBursts.svg?branch=master)](https://travis-ci.org/OpenSMFS/FRETBursts)
[![AppVeyor Build status](https://ci.appveyor.com/api/projects/status/g0ih9gvm7r8459to/branch/master?svg=true)](https://ci.appveyor.com/project/tritemio/fretbursts-llfcd/branch/master)

> *Quick links: [Reference documentation](http://fretbursts.readthedocs.org/), [FRETBursts tutorials](https://github.com/OpenSMFS/FRETBursts_notebooks#fretbursts-notebooks), [FRETBursts paper](http://dx.doi.org/10.1101/039198)*

Latest News
-----------

#### Latest release 0.7 (2017-07-19)

For updates on the latest FRETBursts release see
[release notes](http://fretbursts.readthedocs.io/en/latest/releasenotes.html).


#### 2017-11-20 - Migration to OpenSMFS Organization

We moved the FRETBursts repository on GitHub to the [OpenSMFS organization](https://github.com/OpenSMFS).
The *Open Single-Molecule Fluorescence Spectroscopy* (OpenSMFS) organization collects open source software
for single-molecule spectroscopy (e.g. single-molecule FRET, Fluorescence Correlation spectroscopy, etc...).
FRETBursts joins the company of [PyBroMo](https://github.com/OpenSMFS/PyBroMo) (a freely-diffusing smFRET simulator)
and [pycorrelate](https://github.com/OpenSMFS/pycorrelate) (cross-correlation for FCS).

The new FRETBursts repository URL is [github.com/OpenSMFS/FRETBursts](https://github.com/OpenSMFS/FRETBursts) and the
FRETBursts "landing page" is now [opensmfs.github.io/FRETBursts/](https://opensmfs.github.io/FRETBursts/).
FRETBursts Documentation is hosted on ReadTheDocs and did not change URL.
CI services have been migrated. [Open issues](https://github.com/OpenSMFS/FRETBursts/issues) will be migrated soon.

#### 2016-08-17
Our software paper describing FRETBursts has been peer-reviewed and published by PLOS ONE:

- [FRETBursts: An Open Source Toolkit for Analysis of Freely-Diffusing Single-Molecule FRET](http://dx.doi.org/10.1371/journal.pone.0160716), DOI:10.1371/journal.pone.0160716

#### 2016-03-20
New online service to run FRETBursts without installation:

- [FRETBursts Online Demo](https://github.com/OpenSMFS/FRETBursts_notebooks#run-online)

For more info see this [blog post](http://tritemio.github.io/smbits/2016/03/22/binder-fretbursts/).

#### 2016-02-19

Check out our new paper describing smFRET bursts analysis and FRETBursts on the bioRxiv:

- [FRETBursts: Open Source Burst Analysis Toolkit for Confocal Single-Molecule FRET](http://dx.doi.org/10.1101/039198)

See also this [blog post](http://tritemio.github.io/smbits/2016/02/19/fretbursts/) announcing it.


Project Description
-------------------

<img title="FRETBurst generated ALEX histogram" style="float: right; margin-left: 30px;" src="https://cloud.githubusercontent.com/assets/4156237/12906391/9866197a-ce94-11e5-932b-548a511e4840.png" align="right" height="340" />

**[FRETBursts](http://opensmfs.github.io/FRETBursts)** is a
open source software for burst analysis of freely-diffusing
[single-molecule FRET](http://en.wikipedia.org/wiki/Single-molecule_FRET)
(smFRET) experiments.

### FRETBursts and Reproducibility

FRETBursts is an effort to bring
[reproducible computing](http://dx.doi.org/10.1371/journal.pcbi.1003285)
to the field of single-molecule confocal microscopy. It provides
a well-tested implementation of state-of-the-art algorithms
for confocal smFRET analysis.
The strong focus on computational reproducibility is
reflected in the notebook-based interface.
By leveraging a workflow based on [Jupyter Notebook](http://ipython.org/notebook.html),
FRETBursts facilitates saving all the analysis
parameters, comments and results in a single re-runnable document.

FRETBursts has full supports for [Photon-HDF5](http://photon-hdf5.org/),
an open file format for single-molecule fluorescence experiments
([Ingargiola 2016](http://dx.doi.org/10.1101/026484)).

### Feedback and Contributions

FRETBursts is open source and openly developed on GitHub.

We encourage users to report issues or ask questions using the
[GitHub Issue](https://github.com/OpenSMFS/FRETBursts/issues?state=open).
In the open source spirit, contributions are welcome and
managed using [GitHub Pull Request](https://help.github.com/articles/creating-a-pull-request).
Any level of contribution is accepted, from fixing typos, improving the docs
(most editing can be done online directly)
or implementing new features (see [github help page](https://help.github.com/articles/fork-a-repo/)).
For questions on how to contribute
please open a [GitHub Issue](https://github.com/OpenSMFS/FRETBursts/issues?state=open).

### Technical Features

FRETBursts allows to analyze both [single-spot](http://dx.doi.org/10.1126/science.283.5408.1676)
and [multi-spot smFRET](http://dx.doi.org/10.1117/12.2003704) data.
Alternating laser excitation ([ALEX](http://dx.doi.org/10.1529/biophysj.104.054114))
scheme is supported.

Main analysis features includes:

- background estimation as a function of time (for example in 30s windows)
- sliding-window burst search with adaptive (background-dependent) rate-threshold.
  No timetrace binning required. Both single (APBS) and dual-channel burst search (DCBS).
- burst corrections: background, D-spectral leakage (bleed-through),
  A-direct excitation, gamma-factor.
- per-burst statistics (# photons, burst duration, E, S, peak rate in burst, etc...)
- post-burst-search [selection functions](http://fretbursts.readthedocs.org/en/latest/burst_selection.html)
  (for ex.: [burst size](http://fretbursts.readthedocs.org/en/latest/burst_selection.html#fretbursts.select_bursts.size),
  [burst width](http://fretbursts.readthedocs.org/en/latest/burst_selection.html#fretbursts.select_bursts.width),
  [E, S](http://fretbursts.readthedocs.org/en/latest/burst_selection.html#fretbursts.select_bursts.ES), ...).
  Defining a new burst selection criterium requires only a few lines of code.
- [fit routines](http://fretbursts.readthedocs.org/en/latest/fit.html) for FRET efficiency
  ([multi-model histogram fit](http://fretbursts.readthedocs.org/en/latest/fit.html#fitting-e-or-s-histograms),
  [MLE Poisson models](http://fretbursts.readthedocs.org/en/latest/data_class.html#fretbursts.burstlib.Data.fit_E_ML_poiss),
  [weighted least squares models](http://fretbursts.readthedocs.org/en/latest/data_class.html#fretbursts.burstlib.Data.fit_E_m),
  [weighted expectation maximization](http://fretbursts.readthedocs.org/en/latest/data_class.html#fretbursts.burstlib.Data.fit_E_two_gauss_EM),
  etc...)
- Plot function: FRETBursts includes
  [a large set](https://github.com/OpenSMFS/FRETBursts/blob/master/fretbursts/burst_plot.py)
  of modular
  [plot functions](http://fretbursts.readthedocs.org/en/latest/files_description.html#module-fretbursts.burst_plot)
  for background, time-traces, rate-traces, E, S, ALEX histograms,
  weighted kernel density estimation ([KDE](http://en.wikipedia.org/wiki/Kernel_density_estimation))
  and more. Thanks to the excellent [Matplotlib](http://matplotlib.org/) library,
  FRETBursts can produce publication-quality plots out of the box.

Additionally FRETBursts includes notebooks to perform
[Burst Variance Analysis (BVA)](http://nbviewer.jupyter.org/github/OpenSMFS/FRETBursts_notebooks/blob/master/notebooks/Example%20-%20Burst%20Variance%20Analysis.ipynb)
([Torella 2011](http://doi.org/10.1016/j.bpj.2011.01.066))
and [2CDE](http://nbviewer.jupyter.org/github/OpenSMFS/FRETBursts_notebooks/blob/master/notebooks/Example%20-%202CDE%20Method.ipynb)
([Tomov 2012](http://doi.org/10.1016/j.bpj.2011.11.4025)).

Motivations
-----------

This software aims to be a reference implementation for both established
and novel algorithms related to bursts analysis of smFRET data.

Despite the broad diffusion of smFRET experiments on freely diffusing
molecules, before FRETBursts, no complete smFRET burst analysis software was
freely available on internet. Each group have re-implemented the analysis
in-house with little or no code sharing. This is clearly sub-optimal
either because specific advances in the burst analysis are not readily
available to a wide public of smFRET users and because subtle differences in
implementation make the comparison of experiments performed by different
groups problematic.

We envision FRETBursts both as a state-of-the-art burst analysis package
for smFRET experimenters, and as a toolkit for advanced users willing
to develop new algorithms or to compare alternative implementations.

Software Environment
--------------------
FRETBursts is written in the [python programming language](http://www.python.org/)
using the standard scientific-python stack of libraries (Numpy, Scipy, Matplotlib, IPython).
Not only FRETBursts but also the entire software stack on which it is built upon
are open-source and freely available to any scientist.

FRETBursts uses consolidated software engineering techniques (version control,
unit testing, regression testing) and a workflow based on
[Jupyter Notebook](http://ipython.org/notebook.html)
to ensure robustness and reproducibility of the results. For example,
when loading FRETBursts, the current version (down to the commit ID) is always
displayed (and saved together with the notebook).

We provide a [list of tutorials](#getting-started) (notebooks) that
can be viewed online, edited and re-executed. The
[reference documentation](http://fretbursts.readthedocs.org/)
is generated by Sphinx extracting the docstrings from the source code.

## Installation

For installation instructions see:

* [FRETBursts documentation: Getting started](http://fretbursts.readthedocs.org/en/latest/getting_started.html)

## Documentation

The official FRETBursts documentation is built and hosted by ReadTheDocs:

* [FRETBursts Documentation](http://fretbursts.readthedocs.org/)

We provide a list of Jupyter notebooks showing typical workflows
for smFRET analysis and illustrating FRETBursts functionalities.
These notebooks can be either viewed online or downloaded and executed locally
using publically available datasets (see below).

You can find the notebooks in the OpenSMFS/FRETBursts_notebooks repository: [FRETBursts_notebooks](https://github.com/OpenSMFS/FRETBursts_notebooks#fretbursts-notebooks)
repository.

> *NOTE:* A copy of the tutorials (without output) is [included](https://github.com/OpenSMFS/FRETBursts/tree/master/notebooks)
> in the FRETBursts repository.

FRETBursts notebooks use public [smFRET datasets](https://dx.doi.org/10.6084/m9.figshare.1456362.v13) that are automatically downloaded
when each notebook is executed for the first time.

## Development

The documentation is built using [Sphinx](http://sphinx-doc.org/) (1.2.2 or
later) and the [napoleon extension](https://pypi.python.org/pypi/sphinxcontrib-napoleon).
A notebook that builds the HTML docs can be found in
[`notebooks/dev/docs/`](https://github.com/OpenSMFS/FRETBursts/tree/master/notebooks/dev/docs).

The unit tests are written with [pytest](http://pytest.org/latest/).
Notebooks that execute the unit tests can be found in
[`notebooks/dev/test/`](https://github.com/OpenSMFS/FRETBursts/tree/master/notebooks/dev/tests).
In the same folder a notebook for regression testing is provided.


## Acknowledgments

This work was supported by NIH grants R01 GM069709 and R01 GM095904.

## License and Copyrights

Copyright (C) 2013-2016 The Regents of the University of California, Antonino Ingargiola and contributors.

License: GNU GPL 2

You can find a full copy of the license in the file LICENSE.txt
