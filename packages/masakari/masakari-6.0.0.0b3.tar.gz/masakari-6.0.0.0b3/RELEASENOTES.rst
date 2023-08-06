========
masakari
========

.. _masakari_6.0.0.0b3:

6.0.0.0b3
=========

.. _masakari_6.0.0.0b3_New Features:

New Features
------------

.. releasenotes/notes/bp-mutable-config-57efdd467c01aa7b.yaml @ b'4299b38883c7c711ff3e349f5b134b6c9a272caf'

- Masakari has been enabled for mutable config.
  Below option may be reloaded by sending SIGHUP to the correct process.
  
  'retry_notification_new_status_interval' option will apply to process
  unfinished notifications.


.. _masakari_6.0.0.0b2:

6.0.0.0b2
=========

.. _masakari_6.0.0.0b2_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/wsgi-applications-3ed7d6b89f1a5785.yaml @ b'5bbd78e326e7726229bb94f887f18f8b27bb7a14'

- WSGI application script ``masakari-wsgi`` is now available. It allows
  running the masakari APIs using a WSGI server of choice (for example
  nginx and uwsgi, apache2 with mod_proxy_uwsgi or gunicorn).
  The eventlet-based servers are still available, but the WSGI options will
  allow greater deployment flexibility.


.. _masakari_6.0.0.0b1:

6.0.0.0b1
=========

.. _masakari_6.0.0.0b1_New Features:

New Features
------------

.. releasenotes/notes/db-purge-support-7a33e2ea5d2a624b.yaml @ b'4048b1fd8eae065652105d19892071b0a4fa5533'

- Operators can now purge the soft-deleted records from the database tables.
  Added below command to purge the records:
  
    ``masakari-manage db purge --age_in_days <days> --max_rows <rows>``
  
  NOTE: ``notifications`` db records will be purged on the basis of ``update_at``
  and ``status`` fields (finished, ignored, failed) as these records will not be
  automatically soft-deleted by the system.

