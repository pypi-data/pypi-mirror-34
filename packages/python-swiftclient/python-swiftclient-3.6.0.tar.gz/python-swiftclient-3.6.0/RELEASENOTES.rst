==================
python-swiftclient
==================

.. _python-swiftclient_3.6.0:

3.6.0
=====

.. _python-swiftclient_3.6.0_New Features:

New Features
------------

.. releasenotes/notes/360_notes-1ec385df13a3a735.yaml @ 172a09a4019dc637e525d14aef76f10e812385dd

- Add the ``--prompt`` option for the CLI which will cause the user to be
  prompted to enter a password. Any password otherwise specified by
  ``--key`` , ``--os-password`` or an environment variable will be ignored.

.. releasenotes/notes/360_notes-1ec385df13a3a735.yaml @ 172a09a4019dc637e525d14aef76f10e812385dd

- Added bash completion support to the ``swift`` CLI. Enable this by sourcing
  the included ``tools/swift.bash_completion`` file. Make it permanent by
  including this file in the system's ``/etc/bash_completion.d`` directory.

.. releasenotes/notes/360_notes-1ec385df13a3a735.yaml @ 172a09a4019dc637e525d14aef76f10e812385dd

- Add ability to generate a temporary URL with an IP range restriction.
  TempURLs with IP restrictions are supported are Swift 2.19.0 or later.

.. releasenotes/notes/360_notes-1ec385df13a3a735.yaml @ 172a09a4019dc637e525d14aef76f10e812385dd

- The client.py SDK now supports a ``query_string`` option on the
  ``head_object()`` method. This is useful for finding information on
  SLO/DLO manifests without fetching the entire manifest.

.. releasenotes/notes/360_notes-1ec385df13a3a735.yaml @ 172a09a4019dc637e525d14aef76f10e812385dd

- The client.py SDK now respects ``region_name`` when using sessions.

.. releasenotes/notes/360_notes-1ec385df13a3a735.yaml @ 172a09a4019dc637e525d14aef76f10e812385dd

- Added a ``.close()`` method to an object response, allowing clients to give
  up on reading the rest of the response body, if they so choose.

.. releasenotes/notes/360_notes-1ec385df13a3a735.yaml @ 172a09a4019dc637e525d14aef76f10e812385dd

- Fixed a bug where using ``--debug`` in the CLI with unicode account names
  would cause a client crash.

.. releasenotes/notes/360_notes-1ec385df13a3a735.yaml @ 172a09a4019dc637e525d14aef76f10e812385dd

- Make OS_AUTH_URL work in DevStack (for testing) by default.

.. releasenotes/notes/360_notes-1ec385df13a3a735.yaml @ 172a09a4019dc637e525d14aef76f10e812385dd

- Dropped Python 3.4 testing.

.. releasenotes/notes/360_notes-1ec385df13a3a735.yaml @ 172a09a4019dc637e525d14aef76f10e812385dd

- Various other minor bug fixes and improvements.


.. _python-swiftclient_3.5.0:

3.5.0
=====

.. _python-swiftclient_3.5.0_New Features:

New Features
------------

.. releasenotes/notes/350_notes-ad0ae19704b2eb88.yaml @ b91651eba09ed43903c55f24e3a1a52aefeea75f

- Allow for object uploads > 5GB from stdin.
  
  When uploading from standard input, swiftclient will turn the upload
  into an SLO in the case of large objects. By default, input larger
  than 10MB will be uploaded as an SLO with 10MB segment sizes. Users
  can also supply the ``--segment-size`` option to alter that
  threshold and the SLO segment size. One segment is buffered in
  memory (which is why 10MB default was chosen).

.. releasenotes/notes/350_notes-ad0ae19704b2eb88.yaml @ b91651eba09ed43903c55f24e3a1a52aefeea75f

- The ``--meta`` option can now be set on the upload command.

.. releasenotes/notes/350_notes-ad0ae19704b2eb88.yaml @ b91651eba09ed43903c55f24e3a1a52aefeea75f

- Updated PyPy test dependency references to be more accurate
  on different distros.

