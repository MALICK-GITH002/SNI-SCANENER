import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
from collections import defaultdict

class SubdomainScanner:
    def __init__(self, threads=10, use_ssl=False, ports=None):
        """
        Initialise le scanner avec les paramètres fournis.

        Args:
            threads (int): Nombre de threads à utiliser pour le scan.
            use_ssl (bool): Utiliser HTTPS (port 443) à la place de HTTP (port 80).
            ports (list): Liste des ports personnalisés à scanner.
        """
        init(autoreset=True)  # Initialiser Colorama pour les couleurs
        self.threads = threads
        self.protocols = ["https"] if use_ssl else ["http"]
        self.ports = ports if ports else ([443] if use_ssl else [80])
        self.results = []

    def scan_subdomain(self, subdomain, protocol, port):
        """
        Effectue une requête HTTP/HTTPS vers un sous-domaine spécifique.

        Args:
            subdomain (str): Le sous-domaine à scanner.
            protocol (str): Le protocole à utiliser (http/https).
            port (int): Le port à scanner.

        Returns:
            dict: Résultat du scan avec le statut HTTP ou une erreur.
        """
        url = f"{protocol}://{subdomain}:{port}"
        try:
            response = requests.get(url, timeout=5)
            return {"host": subdomain, "protocol": protocol, "port": port, "status": response.status_code, "success": True}
        except requests.exceptions.RequestException as e:
            return {"host": subdomain, "protocol": protocol, "port": port, "error": str(e), "success": False}

    def scan(self, subdomains):
        """
        Lance le scan de tous les sous-domaines fournis.

        Args:
            subdomains (list): Liste des sous-domaines à scanner.
        """
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = [
                executor.submit(self.scan_subdomain, sub, proto, port)
                for sub in subdomains
                for proto in self.protocols
                for port in self.ports
            ]
            self.results = [future.result() for future in as_completed(futures)]

    def categorize_results(self):
        """
        Organise les résultats par statut HTTP.

        Returns:
            dict: Résultats regroupés par statut HTTP.
        """
        batches = defaultdict(list)
        for result in self.results:
            if result["success"]:
                batches[result["status"]].append(result)
            else:
                batches["ERROR"].append(result)
        return batches

    def display_results(self):
        """
        Affiche les résultats du scan avec des couleurs pour chaque statut HTTP.
        """
        batches = self.categorize_results()

        for status, batch in batches.items():
            if status == "ERROR":
                print(f"\n{Fore.RED}[ERROR] Failed scans:")
                for r in batch:
                    print(f" - {r['protocol']}://{r['host']}:{r['port']} (Error: {r['error']})")
            elif status == 200:
                print(f"\n{Fore.GREEN}[STATUS 200] Successful scans:")
                for r in batch:
                    print(f" - {r['protocol']}://{r['host']}:{r['port']} (Status: 200)")
            elif status == 403:
                print(f"\n{Fore.LIGHTYELLOW_EX}[STATUS 403] Forbidden scans:")
                for r in batch:
                    print(f" - {r['protocol']}://{r['host']}:{r['port']} (Status: 403)")
            elif status == 400:
                print(f"\n{Fore.YELLOW}[STATUS 400] Bad Request scans:")
                for r in batch:
                    print(f" - {r['protocol']}://{r['host']}:{r['port']} (Status: 400)")
            else:
                print(f"\n{Fore.CYAN}[STATUS {status}] Other scans:")
                for r in batch:
                    print(f" - {r['protocol']}://{r['host']}:{r['port']} (Status: {status})")
