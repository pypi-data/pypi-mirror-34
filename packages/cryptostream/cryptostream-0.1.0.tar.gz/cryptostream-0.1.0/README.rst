**********
Installing
**********

You can easily install cryptostream with pip:

.. code-block:: sh

 pip install cryptostream


**********
Motivation
**********

Imagine two companies A and B. Company B is building drones and writing software for drones. Company A wants to use those drones. The drone saves log files onboard. If the drone crashes or any other accident happens, this log file gives us information about what went wrong. However, this causes several issues: Company A could manipulate those log files, especially if they know that the crash is their own mistake. A simple solution would be to stream the log files to company B, for example via LTE. This, however, causes another type of problem: Privacy. If company A does not want company B to know the contents of the log files, except for rare occasions like accidents, we encrypt the data so that company B can only decode the logs if company A gives them the private key. 

********
Examples
********

.. code-block:: sh

 cd examples
 python generate-keys.py
 python encrypt-and-decrypt.py

