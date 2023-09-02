Ansible playbook na instalaci zookeeperu clusteru odolávajícímu výpadku 2 instancí služby (5 nodů).

REQUIREMENTS:
Nainstalovaný ansible, mít inventory s jednotlivými nody a ip adresami ve tvaru:
[node1]
ip1

[node2]
ip2

[node3]
ip3

[node4]
ip4

[node5]
ip5

[nodes]
ip1
ip2
ip3
ip4
ip5

PB: main.yml
