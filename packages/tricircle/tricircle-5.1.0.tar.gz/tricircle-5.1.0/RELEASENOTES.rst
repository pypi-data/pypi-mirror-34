=========
tricircle
=========

.. _tricircle_4.2.0:

4.2.0
=====

.. _tricircle_4.2.0_New Features:

New Features
------------

.. releasenotes/notes/add-lbaas-ebb1009abd3da0dd.yaml @ b'2728624a46998d829e9c42f484edc573e9e23e19'

- Support LBaaS in multi-region scenario. To enable adding instances as
  members with VIP, amphora routes the traffic sent from VIP to its
  gateway. However, in Tricircle, the gateway obtained from central neutron
  is not the real gateway in local neutron. As a result, only subnet
  without gateway is supported as member subnet. We will remove the
  limitation in the future, and LBaaS working together with Nova Cells V2
  multi-cells will also be supported in the future.

.. releasenotes/notes/add-qos-policy-rule-f8f1529d7ad5d888.yaml @ b'db679ef7cb145fbede3dd514959baea81aad23a1'

- Provide central Neutron QoS plugin and implement QoS driver. Support QoS policy creation, update and delete, QoS policy binding with network or port.

.. releasenotes/notes/enable-update-default-securitygroup-9bb426021926d3e8.yaml @ b'25ada0602ef9c253cef7be10d5a28e9ce9a6706e'

- Support updating default security group using asynchronous methods.


.. _tricircle_3.4.0:

3.4.0
=====

.. _tricircle_3.4.0_New Features:

New Features
------------

.. releasenotes/notes/add-service-function-chaining-fc2cf9a2e8610b91.yaml @ b'2d22bb18bf9cce72c584700f2e44a16b2c9195d4'

- Support service function chaining creation and deletion based on networking-sfc,
  currently all the ports in the port chain need to be in the same network and the
  network type must be VxLAN.

.. releasenotes/notes/support-pagination-for-async-job-81728e9cb7aef731.yaml @ b'bc6a45e4f45835b9e2a93127e79aacba6b6d2c2a'

- Support pagination for asynchronous job list operation. Jobs in job table
  will be shown ahead of those in job log table. If page size is not specified
  from client, then maximum pagination limit from configuration will be used.

.. releasenotes/notes/support-pagination-for-resource-routing-list-13bcb0f1897dedf8.yaml @ b'71e0c21b2e272e7d5657d23cb48cf6ea9fdfc4b3'

- Support pagination for resource routing list operation. If page size is
  not specified from client, then maximum pagination limit from
  configuration will be used.


.. _tricircle_3.3.0:

3.3.0
=====

.. _tricircle_3.3.0_New Features:

New Features
------------

.. releasenotes/notes/add-vlan-aware-vms-afa8c5a906f2ab49.yaml @ b'b0c61d60be53a317fff4b2dedf2a0cf19a8cb1c7'

- Support VLAN aware VMs

.. releasenotes/notes/asynchronous-job-management-api-c16acb43b495af7c.yaml @ b'3f5b0e8cc2433190dd93ebc05fcf006c46644486'

- Asynchronous job management API allows administrator
  to perform CRUD operations on a job. For jobs in job
  log, only list and show operations are allowed.
  
  * Create a job
  * List jobs
  * Show job details
  * Delete a job
  * Redo a job


.. _tricircle_3.2.0:

3.2.0
=====

.. _tricircle_3.2.0_New Features:

New Features
------------

.. releasenotes/notes/flat-network-8634686c1fede7b2.yaml @ b'ee008cae6b8fc65717f4699c5634fc3e071c391b'

- Support flat type of tenant network or external network

.. releasenotes/notes/multi-gateway-ns-networking-fbd876c7659a55a9.yaml @ b'22f9334b77ffb77f78af31176a126d3dd4d57c1c'

- Support network topology that each OpenStack cloud provides external network for tenant's north-south traffic and at the same time east-west networking of tenant networks among OpenStack clouds is also enabled


.. _tricircle_3.1.0:

3.1.0
=====

.. _tricircle_3.1.0_Prelude:

Prelude
-------

.. releasenotes/notes/support-wsgi-deployment-21eb19bcb04932f0.yaml @ b'6eb93e844d5634285f3ac86a0e00011b98ceb2c7'

Tricircle Admin API now supports WSGI deployment. The endpoint of Tricircle Admin API could be accessed via the format of http://host/tricircle, and no need to expose special port, thus reduce the risk of port management.


.. _tricircle_3.1.0_New Features:

New Features
------------

.. releasenotes/notes/enable-allowed-address-pairs-bca659413012b06c.yaml @ b'0beeb821978a1a00393f17b09a55903def5d0130'

- Enable allowed-address-pairs in the central plugin.

.. releasenotes/notes/enable-router-az-and-simplify-net-topology-5ac8739b167e3e4a.yaml @ b'da443110e90fefd2deb89d15c6838f1c23f2952f'

- Router
  
  * Support availability zone for router
  * Local router, which will reside only inside one region, can be
    attached with external network directly, no additional intermediate
    router is needed.

.. releasenotes/notes/vxlan-network-2a21433b4b691f72.yaml @ b'cc770090c03a7c59c259a527e4e3b224891bf52e'

- Support VxLAN network type for tenant network and bridge network to be
  stretched into multiple OpenStack clouds


.. _tricircle_3.0.0:

3.0.0
=====

.. _tricircle_3.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/initial-release-notes-bd28a4a4bf1f84d2.yaml @ b'47376bd087c31e2da01e891ae348758b3a8fb474'

The Tricircle is to provide networking automation across Neutron in OpenStack multi-region deployment.


.. _tricircle_3.0.0_New Features:

New Features
------------

.. releasenotes/notes/combine-bridge-network-c137a03f067c49a7.yaml @ b'b60ba570bb1e941cee31f8bf0ce7e3f898152823'

- North-south bridge network and east-west bridge network are combined into one to bring better DVR and shared VxLAN network support.

.. releasenotes/notes/initial-release-notes-bd28a4a4bf1f84d2.yaml @ b'47376bd087c31e2da01e891ae348758b3a8fb474'

- Network
  
  * List networks
  * Create network
  * Show network details
  * Delete network

.. releasenotes/notes/initial-release-notes-bd28a4a4bf1f84d2.yaml @ b'47376bd087c31e2da01e891ae348758b3a8fb474'

- Subnet
  
  * List subnets
  * Create subnet
  * Show subnet details
  * Delete subnet

.. releasenotes/notes/initial-release-notes-bd28a4a4bf1f84d2.yaml @ b'47376bd087c31e2da01e891ae348758b3a8fb474'

- Port
  
  * List ports
  * Create port
  * Show port details
  * Delete port

.. releasenotes/notes/initial-release-notes-bd28a4a4bf1f84d2.yaml @ b'47376bd087c31e2da01e891ae348758b3a8fb474'

- Router
  
  * List routers
  * Create router
  * Show router details
  * Delete router
  * Add interface to router
  * Delete interface from router
  * List floating IPs
  * Create floating IP
  * Show floating IP details
  * Update floating IP
  * Delete floating IP

.. releasenotes/notes/initial-release-notes-bd28a4a4bf1f84d2.yaml @ b'47376bd087c31e2da01e891ae348758b3a8fb474'

- Security Group
  
  * List security groups
  * Create security group
  * Show security group details
  * List security group rules
  * Create security group rule
  * Delete security group rule

.. releasenotes/notes/initial-release-notes-bd28a4a4bf1f84d2.yaml @ b'47376bd087c31e2da01e891ae348758b3a8fb474'

- Note for Networking
  
  * Only Local Network and VLAN network supported.
    Local Network means the network will only present in one region,
    it could be VxLAN or VLAN network.
    VLAN is the only L2 network type which supports cross
    Neutron L2 networking and the bridge network for L3 networking.
  * Pagination and sort are not supported at the same time for list
    operation.
  * For security group rule, remote group is not supported yet. Use IP
    prefix to create security group rule.
  * One availability zone can include more than one region through
    Tricircle pod management.
  * Availability zone or region name for availability zone hint can be
    specified during network creation, that means this network will be
    presented in the specified list of availability zone or region. If no
    availability zone hint is specified and the network is not Local
    Network, then the network can be spread into all regions. For Local
    Network without availability zone hint specified in creation, then
    the network will only be presented in the first region where the
    resource(VM, baremetal or container) is booted and plugged into this
    network.
  * Need to specify one region name as the availability zone hint for
    external network creation, that means the external network will
    be located in the specified region.

.. releasenotes/notes/network-subnet-update-baed5ded548f7269.yaml @ b'654fd620ecc292538c39ce1ff1e089551f61cdfd'

- Network
  
  * Update networks
  
    * qos-policy not supported

.. releasenotes/notes/network-subnet-update-baed5ded548f7269.yaml @ b'654fd620ecc292538c39ce1ff1e089551f61cdfd'

- Subnet
  
  * Update subnets

.. releasenotes/notes/port-base-update-6668b76c2346633c.yaml @ b'ac65bc3832103343bc0576e43205da51892ce6f8'

- Port
  
  * Update port
  
    * name, description, admin_state_up, extra_dhcp_opts, device_owner,
      device_id, mac_address, security group attribute updates supported

.. releasenotes/notes/resource-routing-operation-649eb810911312ec.yaml @ b'7ca32bb3e8e96a93a8dbb9e1ef2f312c39d8b8f2'

- Resource routing APIs add operations on resource routing
  table. This makes it possible to create, show, delete
  and update the resource routing entry in the resource
  routing by cloud administrator for the maintenance and
  emergency fix need. But the update and delete operations
  on the entry generated by the Tricircle itself is not
  proposed, because central Neutron may make wrong
  judgement on whether the resource exists or not
  without this routing entry. Moreover, related request
  can not be forwarded to the proper local Neutron
  either. So even though the update and delete operations
  are provided, they are better not to be used in case of
  causing unexpected problems.
  
  * List resource routings
  * Create resource routing
  * Show resource routing details
  * Delete resource routing
  * Update resource routing


.. _tricircle_3.0.0_Known Issues:

Known Issues
------------

.. releasenotes/notes/initial-release-notes-bd28a4a4bf1f84d2.yaml @ b'47376bd087c31e2da01e891ae348758b3a8fb474'

- refer to https://bugs.launchpad.net/tricircle

.. releasenotes/notes/network-subnet-update-baed5ded548f7269.yaml @ b'654fd620ecc292538c39ce1ff1e089551f61cdfd'

- Update network or subnet may not lead to the expected result if an
  instance is being booted at the same time. You can redo the update
  operation later to make it execute correctly.

.. releasenotes/notes/port-base-update-6668b76c2346633c.yaml @ b'ac65bc3832103343bc0576e43205da51892ce6f8'

- Update port may not lead to the expected result if an instance is being
  booted at the same time. You can redo the update operation later to make
  it execute correctly.

