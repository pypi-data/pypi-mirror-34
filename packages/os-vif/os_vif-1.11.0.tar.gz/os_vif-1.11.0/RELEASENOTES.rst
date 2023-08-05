======
os_vif
======

.. _os_vif_1.11.0:

1.11.0
======

.. _os_vif_1.11.0_New Features:

New Features
------------

.. releasenotes/notes/add-no-op-plugin-763a6703e7328a24.yaml @ b'ba61a981171b3514219eb6ecf306e421f99ce127'

- A new VIF plugin, ``vif_plug_noop``, has been added which can be used with
  network backends that do not require any action to be performed when a
  network interface is plugged. This plugin allow for use of, for example,
  the generic vhost user VIF type without OVS.

