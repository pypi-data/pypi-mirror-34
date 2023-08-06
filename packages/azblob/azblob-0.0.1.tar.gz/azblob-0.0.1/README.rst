Azure Blob
==========

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
 :target: https://github.com/ambv/black

One-line CLI to download from Azure blob storage. Supports private blobs.


Installation
------------

To install:

.. code-block:: bash

    $ pip install azblob

CLI
---

Using credentials from environment

.. code-block:: bash

    $ export AZBLOB_ACCOUNTNAME=
    $ export AZBLOB_ACCOUNTKEY=my_accountkey
    $ azblob download my_container my_blob


Using credentials from command line

.. code-block:: bash

    $ azblob -n my_accountname -k my_accountkey download my_container my_blob

and as always

.. code-block:: bash

    $ azblob -h
    $ azblob download -h
