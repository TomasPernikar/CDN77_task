Instalace Proxmox VE na cílový server pomocí Ansible a následně vytvoření VM šablony pro deploy dalších VMs klonováním.

Requirements:
Instalace ansible
V inventáři mít cílový server (pve-server)

Postup:
1) Spustit playbook install-pve.yml
2) Restartovat cílový server
3) Spustit playbook main_after-reboot.yml (Playbook vytvoří připojená PVE na síťový adaptér a vytvoří VM template s vmid 100.
4) Projít manuálně instalaci a upravit si templatu podle svých potřeb.
5) VM uložit jako template ($ qm template 100 [OPTIONS])
