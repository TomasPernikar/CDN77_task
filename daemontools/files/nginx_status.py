import time
import subprocess

# URL adresa pro ziskani statistik ze stranky Nginx status
nginx_status_url = "http://127.0.0.1:81/nginx_status"

# Cesta k vystupnimu souboru pro ukladani statistik
output_file = "/var/log/nginx_stats.log"

while True:
    # Provedeni HTTP GET pozadavku na Nginx status pomoci curl
    curl_command = ["curl", "-sD", "-", nginx_status_url]
    response = subprocess.run(curl_command, capture_output=True, text=True)

    #  Return code 
    if response.returncode == 0:
        # Ziskani textoveho obsahu odpovedi, ktery obsahuje statistiky
        stats_data = response.stdout

        # Otevreni souboru pro zapis statistik
        with open(output_file, "w") as f:
            f.write(stats_data)

    # Cekani 5 minut 
    time.sleep(300)

