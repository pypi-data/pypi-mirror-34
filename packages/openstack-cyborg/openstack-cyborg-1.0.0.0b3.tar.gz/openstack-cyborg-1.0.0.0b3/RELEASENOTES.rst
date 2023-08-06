================
openstack-cyborg
================

.. _openstack-cyborg_1.0.0.0b1:

1.0.0.0b1
=========

.. _openstack-cyborg_1.0.0.0b1_New Features:

New Features
------------

.. releasenotes/notes/basic-framework-28d6b42d9bf684af.yaml @ b'5b4b9a382c164573adb9dfe41401a269cdae27d4'

- The cyborg framework consists of three core services - API, Conductor
  and Agent.
  cyborg-api supports GET/POST/PUT/DELETE operations for accelerators.
  cyborg-conductor is responsible for handling all API requests that come in
  via the API service.
  cyborg-agent is responsible for all the Nova Cyborg interaction.
  It should be noted that for operations that are not associated with DB change,
  the cyborg-api could directly call cyborg-agent.

.. releasenotes/notes/cyborg-nova-interaction-8fe4e49e3c9b3b7b.yaml @ b'5b4b9a382c164573adb9dfe41401a269cdae27d4'

- Cyborg-Nova interaction was completed in Queens via three specs.
  The cyborg-nova-interaction spec serves as the main spec defines the interaction
  mechanism between Cyborg and Nova is via Placement to which cyborg-conductor
  will periodically report the accelerator resource info, which is acquired via
  resource tracker functionality in the agent.
  The cyborg-internal-api spec defines the internal api that is mainly used for
  internal communication between conductor/agent and driver.
  The cyborg-fpga-model-proposal spec defines the first tryout of data modeling of
  accelerator resources via resource provider. Two types of tables (accelerator
  for base PF and deployable for VF) are defined there and nested resource
  provider will be utilized in Rocky release.

.. releasenotes/notes/fpga-driver-8b1635e92b1297c1.yaml @ b'5b4b9a382c164573adb9dfe41401a269cdae27d4'

- The cyborg-fpga-driver-proposal spec provides the first proposal of a cyborg
  fpga driver. Two operations are supported - discover and program, although the
  latter was not finished in Queens and will be in Rocky. The code implementation
  starts with an Intel QAT card, but more vendor card support should be
  added later and the driver support should be generalized.

.. releasenotes/notes/generic-driver-88427acd7c7c12df.yaml @ b'5b4b9a382c164573adb9dfe41401a269cdae27d4'

- The cyborg generic driver provide a full implementation of CRUD operations,
  for testing purpose only. This is only an examplary implementation of a driver
  which specific accelerator driver could refer to.

.. releasenotes/notes/spdk-driver-89b178e1a2db29c0.yaml @ b'5b4b9a382c164573adb9dfe41401a269cdae27d4'

- The cyborg-spdk-driver-proposal spec defines the first software accelerator
  driver managed by Cyborg. SPDK is widely used in NVMe SSD user space driver
  to have a high performance. In Queens only basic operations on SPDK (discover,
  list, construct/delete subsystem for NVMeOF devices, add/delete ip address
  for vhost) are supported, more completed operation support should be expected
  in the next couple releases.

