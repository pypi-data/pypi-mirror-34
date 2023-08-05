################
pfmisc  v1.2.2
################

.. image:: https://badge.fury.io/py/pfmisc.svg
    :target: https://badge.fury.io/py/pfmisc

.. image:: https://travis-ci.org/FNNDSC/pfdcm.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/pfmisc

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/pfmisc

.. contents:: Table of Contents

********
Overview
********

This repository provides ``pfmisc`` -- miscellaneous services for the ``pf`` family.

pfmisc
======

Most simply, ``pfmisc`` provides debug and color modules.

*****
Usage
*****

Simply do a 

.. code-block:: python

    import pfmisc

    class MyClass():

        def __init__(self, *args, **kwargs):
            self.debug  = pfmisc.debug()

            self.debug.qprint('hello there!')

which will result in some decent debugging in stdout.

************
Installation
************

Installation is relatively straightforward, and we recommend using either python virtual environments or docker.

Python Virtual Environment
==========================

On Ubuntu, install the Python virtual environment creator

.. code-block:: bash

  sudo apt install virtualenv

Then, create a directory for your virtual environments e.g.:

.. code-block:: bash

  mkdir ~/python-envs

You might want to add to your .bashrc file these two lines:

.. code-block:: bash

    export WORKON_HOME=~/python-envs
    source /usr/local/bin/virtualenvwrapper.sh

Then you can source your .bashrc and create a new Python3 virtual environment:

.. code-block:: bash

    source .bashrc
    mkvirtualenv --python=python3 python_env

To activate or "enter" the virtual env:

.. code-block:: bash

    workon python_env

To deactivate virtual env:

.. code-block:: bash

    deactivate

Using the ``fnndsc/ubuntu-python3`` dock
========================================

We provide a slim docker image with python3 based off Ubuntu. If you want to play inside this dock and install ``pman`` manually, do

.. code-block:: bash

    docker pull fnndsc/ubuntu-python3

This docker has an entry point ``python3``. To enter the dock at a different entry and install your own stuff:

.. code-block:: bash

   docker run -ti --entrypoint /bin/bash fnndsc/ubuntu-python3
   
Now, 

.. code-block:: bash

   apt update && \
   apt install -y libssl-dev libcurl4-openssl-dev librtmp-dev && \
   pip install pfmisc
   
**If you do the above, remember to** ``commit`` **your changes to the docker image otherwise they'll be lost when you remove the dock instance!**

.. code-block:: bash

  docker commit <container-ID> local/ubuntu-python3-pfdcm
  
 where ``<container-ID>`` is the ID of the above container.