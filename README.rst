ansible-ssh
===========

Adds interactive SSH capabilities to Ansible,
especially useful in setups with VMs in private
subnets accessible only via jumphosts.

It uses Ansible's inventory file so any ``ansible_ssh_common_args`` or ``ansible_ssh_extra_args`` apply to ``ansible-ssh`` as well.

Requirements
------------
* ``ansible``
* ``pip``

Usage
-----

Run with ``-h`` for command-line help::

    usage: ansible-ssh [-h] [--inventory INVENTORY] [--key-file KEYFILE]
                       [--user USER] [--verbose] [--become]
                       host

    positional arguments:
      host                  the host to ssh into, if not provided a list of hosts
                            in current inventory file is printed
    
    optional arguments:
      -h, --help            show this help message and exit
      --inventory INVENTORY, -i INVENTORY
                            ansible inventory file to use instead of the one
                            defined in ansible.cfg
      --key-file KEYFILE, -k KEYFILE
                            ssh private key file to use instead of the default for
                            the user
      --user USER, -u USER, -l USER
                            override the user defined in ansible inventory file
      --verbose, -v         pass verbose flag to ssh command
      --become, -b          ssh as root instead of the inventory-supplied account


Example
-------
.. code-block:: bash

    $ ansible-ssh lb-0
    executing ssh -C -o ControlMaster=auto -o ControlPersist=60s -o ProxyCommand="ssh -W %h:%p -q ubuntu@10.200.100.60" -l ubuntu 192.168.1.30
    Last login: Sat May 25 15:40:13 2019 from 192.168.1.100
    ubuntu@lb-0:~$ 

