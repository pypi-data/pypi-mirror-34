==============
networking-odl
==============

.. _networking-odl_13.0.0.0b3:

13.0.0.0b3
==========

.. _networking-odl_13.0.0.0b3_Prelude:

Prelude
-------

.. releasenotes/notes/odl_features-option-type-change-367385ae7d1e949e.yaml @ 1ca4cff225b734e5040a7aa07cabde2d749c20bd

The config option odl_features_json has been added to allow specifying features in the same format ODL returns during negotiation.


.. releasenotes/notes/remove-v1-driver-df408f9916fc5e5d.yaml @ 182be58f4034e989394ca0fa92dd8169ec059546

The v1 drivers, which were deprecated in the Queens cycle, are removed. All existing usages should be updated to use the v2 drivers.


.. _networking-odl_13.0.0.0b3_New Features:

New Features
------------

.. releasenotes/notes/odl_features-option-type-change-367385ae7d1e949e.yaml @ 1ca4cff225b734e5040a7aa07cabde2d749c20bd

- The odl_features_json option accepts a JSON compatible with the JSON
  response from ODL's API for retrieving features
  ("/restconf/operational/neutron:neutron/features").
  
  If this option is configured, networking_odl will not query ODL for
  its feature support and will instead use the configured value. If
  odl_features and odl_features_json are both specified, odl_features_json
  will take precedence and odl_features will not be used at all.


.. _networking-odl_13.0.0.0b3_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/remove-v1-driver-df408f9916fc5e5d.yaml @ 182be58f4034e989394ca0fa92dd8169ec059546

- If you've been using v1 drivers, update your configuration to use the
  v2 drivers.
  Otherwise, neutron won't boot properly if v1 drivers are still used.


.. _networking-odl_13.0.0.0b3_Critical Issues:

Critical Issues
---------------

.. releasenotes/notes/remove-v1-driver-df408f9916fc5e5d.yaml @ 182be58f4034e989394ca0fa92dd8169ec059546

- The v1 drivers are removed. If you're still using v1 drivers, migrate to
  use the v2 drivers.

