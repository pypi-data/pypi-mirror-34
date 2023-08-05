Citing libra_py_001_01
=============

The library libra_py is an academic project. The time and resources spent developing fastFM are therefore justified 
by the number of citations of the software. If you publish scientific articles using libra_py, please cite the following article (bibtex entry `citation.bib <http://jmlr.org/papers/v17/15-355.bib>`_).

    Bayer, I. "fastFM: A Library for Factorization Machines" Journal of Machine Learning Research 17, pp. 1-5 (2016)


libra_py: A Package for sparsity problem
============================================



Supported Operating Systems
---------------------------
fastFM has a continuous integration / testing servers (Travis) for **Linux (Ubuntu 14.04 LTS)**
and **OS X Mavericks**. Other OS are not actively supported.

Usage
-----
.. code-block:: python

    from fastFM import als
    fm = als.FMRegression(n_iter=1000, init_stdev=0.1, rank=2, l2_reg_w=0.1, l2_reg_V=0.5)
    fm.fit(X_train, y_train)
    y_pred = fm.predict(X_test)


Tutorials and other information are available `here <http://arxiv.org/abs/1505.00641>`_.
The C code is available as `subrepository <https://github.com/ibayer/fastFM-core>`_ and provides 
a stand alone command line interface. If you have still **questions** after reading the documentation please open a issue at GitHub.

+----------------+------------------+-----------------------------+
| Family         | Solver           | Loss                        |
+================+==================+=============================+
| Gaussian       | LBI_Linear       | Square Loss                 |
+----------------+------------------+-----------------------------+
| Binomial       | LBI_Logit        | Logit Model                 |
+----------------+------------------+-----------------------------+

*Supported solvers and tasks*

Installation
------------

**binary install**

``pip install libra_py``


Tests
-----

