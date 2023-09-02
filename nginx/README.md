Ansible playbook na instalaci 2 instancí nginx. První hostuje soubory z lokálního disku a poslouchá na portu 81 (nginx stub status) Druhá instance funguje jako reverzní cacheující proxy server, který využívá první nginx instanci jako svůj upstream, poslouchá na portu 80 a běží v docker kontejneru sestaveném pomocí Dockerfile.

REQUIREMENTS:
Nainstalovaný ansible, mít v inventáři cílový server (webserver)

PB: main.yml
