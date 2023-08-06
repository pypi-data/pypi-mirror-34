Let me crawl
=======================

Curate proxies from various sources in terms of latency. Supported on python 2.7.* and >3.4.


.. code-block:: bash

    >> from letmecrawl import letmecrawl
    >> for proxy in letmecrawl():
    >>     print(proxy)
    88.99.11.10:6666



Installation
-----------------
.. code-block:: bash

    pip install letmecrawl

Docker
-----------------

Use docker image as a http service:

.. code-block:: bash

    docker pull montenegrodr/letmecrawl:latest

Running:

.. code-block:: bash

    docker run -p 8000:8000 montenegrodr/letmecrawl:latest

Request proxy from top of the queue:

.. code-block:: bash

    $ curl localhost:8000
    {"proxy":"138.68.178.106:80"}

    $ curl localhost:8000
    {"proxy":"184.59.102.95:80"}
