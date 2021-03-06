.. _storage:

Storage
#######

Backends
========

PostgreSQL
----------

.. autoclass:: cliquet.storage.postgresql.PostgreSQL


Redis
-----

.. autoclass:: cliquet.storage.redis.Redis


Memory
------

.. autoclass:: cliquet.storage.memory.Memory


.. _cloud-storage:

Cloud Storage
-------------

.. autoclass:: cliquet.storage.cloud_storage.CloudStorage


API
===

Implementing a custom storage backend consists in implementating the following
interface:

.. automodule:: cliquet.storage
    :members:


Exceptions
----------

.. automodule:: cliquet.storage.exceptions
    :members:


Store custom data
=================

Storage can be used to store arbitrary data.

.. code-block:: python

    custom = BaseResource(request)
    custom.name = '__custom'

    data = {'subscribed': datetime.now()}
    user_id = request.authenticated_userid

    storage = request.registry.storage
    storage.create(resource=custom, user_id=user_id, record=data)
