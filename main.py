from SubdomainScannerTool import SubdomainScanner

if __name__ == "__main__":
    # Liste des sous-domaines à scanner
    subdomains = [
        "www.example.com",
        "api.example.com",
        "login.example.com",
        "test.example.com"
    ]

    # Initialiser le scanner
    scanner = SubdomainScanner(
        threads=10,     # Nombre de threads
        use_ssl=True,   # Utiliser HTTPS
        ports=[80, 443, 8080]  # Ports personnalisés
    )

    # Lancer le scan
    scanner.scan(subdomains)

    # Afficher les résultats
    scanner.display_results()
