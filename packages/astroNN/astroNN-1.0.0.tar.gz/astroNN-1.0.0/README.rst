.. image:: http://astronn.readthedocs.io/en/latest/_static/astroNN_icon_withname.png

|

.. image:: https://readthedocs.org/projects/astronn/badge/?version=latest
   :target: http://astronn.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/github/license/henrysky/astroNN.svg
   :target: https://github.com/henrysky/astroNN/blob/master/LICENSE
   :alt: GitHub license

.. image:: https://travis-ci.org/henrysky/astroNN.svg?branch=master
   :target: https://travis-ci.org/henrysky/astroNN
   :alt: Build Status

.. image:: https://img.shields.io/coveralls/henrysky/astroNN.svg
   :target: https://coveralls.io/github/henrysky/astroNN?branch=master
   :alt: Coverage Status

Getting Started
=================

astroNN is a python package to do various kinds of neural networks with targeted application in astronomy by using Keras
as model and training prototyping, but at the same time take advantage of Tensorflow's flexibility.

For non-astronomy applications, astroNN contains custom loss functions and layers which are compatible with Tensorflow
or Keras with Tensorflow backend. The custom loss functions mostly designed to deal with incomplete labels.
astroNN contains demo for implementing Bayesian Neural Net with Dropout Variational Inference in which you can get
reasonable uncertainty estimation and other neural nets.

For astronomy applications, astroNN contains some tools to deal with APOGEE, Gaia and LAMOST data. astroNN is mainly designed
to apply neural nets on APOGEE spectra analysis and predicting luminosity from spectra using data from Gaia
parallax with reasonable uncertainty from Bayesian Neural Net. Generally, astroNN can handle 2D and 2D colored images too.
Currently astroNN is a python package being developed by the main author to facilitate his research
project on deep learning application in stellar and galactic astronomy using SDSS APOGEE, Gaia and LAMOST data.

For learning purpose, astroNN includes a deep learning toy dataset for astronomer - `Galaxy10 Dataset`_.


`astroNN Documentation`_

`Quick Start guide`_

`Uncertainty Analysis of Neural Nets with Variational Methods`_


Acknowledging astroNN
-----------------------

Please cite astroNN in your publications if it helps your research. Here is an example BibTeX entry:

::

   @misc{leung2018astroNN,
     title={astroNN},
     author={Leung & Bovy},
     year={2018},
     howpublished={\url{https://github.com/henrysky/astroNN}},
   }

or AASTex

::

   \bibitem[Leung \& Bovy (2018)]{leung2018astroNN} Leung \& Bovy 2018, astroNN GitHub, https://github.com/henrysky/astroNN

Authors
-------------
-  | **Henry Leung** - *Initial work and developer* - henrysky_
   | Astronomy Student, University of Toronto
   | Contact Henry: henrysky.leung [at] mail.utoronto.ca

-  | **Jo Bovy** - *Project Supervisor* - jobovy_
   | Astronomy Professor, University of Toronto

License
-------------
This project is licensed under the MIT License - see the `LICENSE`_ file for details

.. _LICENSE: LICENSE
.. _henrysky: https://github.com/henrysky
.. _jobovy: https://github.com/jobovy

.. _astroNN Documentation: http://astronn.readthedocs.io/
.. _Quick Start guide: http://astronn.readthedocs.io/en/latest/quick_start.html
.. _Galaxy10 Dataset: http://astronn.readthedocs.io/en/latest/galaxy10.html
.. _Galaxy10 Tutorial Notebook: https://github.com/henrysky/astroNN/blob/master/demo_tutorial/galaxy10/Galaxy10_Tutorial.ipynb
.. _Uncertainty Analysis of Neural Nets with Variational Methods: https://github.com/henrysky/astroNN/tree/master/demo_tutorial/NN_uncertainty_analysis
