# Subdomain Scanner Tool

**Subdomain Scanner Tool** est un outil Python conçu pour scanner des sous-domaines, détecter leurs statuts HTTP, et catégoriser les résultats avec des couleurs pour une lisibilité améliorée. Cet outil est rapide, extensible et supporte les connexions via HTTP/HTTPS avec des ports personnalisés.

## Fonctionnalités

- **Scan Multi-Threaded** : Scanne simultanément plusieurs sous-domaines pour une exécution rapide.
- **Support des Protocoles et Ports** : Permet de scanner via HTTP ou HTTPS, avec des ports personnalisés.
- **Catégorisation par Statuts HTTP** :
  - **200 (Succès)** : Affiché en vert.
  - **403 (Interdit)** : Affiché en orange.
  - **400 (Mauvaise Requête)** : Affiché en jaune.
  - **Autres Statuts** : Affichés en bleu.
  - **Erreurs Réseau** : Affichées en rouge (timeouts, connexions refusées, etc.).
- **Couleurs Améliorées** : Les résultats sont colorés pour une meilleure visualisation.
- **Modularité** : La logique est encapsulée dans une classe réutilisable.

## Prérequis

- Python 3.x
- Bibliothèques Python suivantes :
  - `requests`
  - `colorama`

## Installation

1. **Installer Python et les Dépendances** :
   Assurez-vous que Python est installé sur votre système. Installez les bibliothèques nécessaires avec :
   ```bash
   pip install requests colorama
   ```

2. **Télécharger les Fichiers** :
   Téléchargez ou clonez les deux fichiers suivants :
   - `SubdomainScannerTool.py`
   - `main.py`

3. **Structure des Fichiers** :
   Placez les deux fichiers dans le même répertoire :
   ```
   .
   ├── SubdomainScannerTool.py
   └── main.py
   ```

## Utilisation

1. **Modifier les Sous-Domaines** :
   Ouvrez le fichier `main.py` et mettez à jour la liste des sous-domaines à scanner :
   ```python
   subdomains = [
       "www.example.com",
       "api.example.com",
       "login.example.com",
       "test.example.com"
   ]
   ```

2. **Lancer le Scan** :
   Exécutez le fichier principal avec Python :
   ```bash
   python main.py
   ```

3. **Résultats** :
   Les résultats seront affichés dans le terminal, regroupés par statut HTTP. Voici un exemple de sortie :
   ```
   [STATUS 200] Successful scans:
    - https://www.example.com:443 (Status: 200)

   [STATUS 403] Forbidden scans:
    - https://api.example.com:443 (Status: 403)

   [ERROR] Failed scans:
    - https://unknown.example.com:443 (Error: Connection Timeout)
   ```

## Personnalisation

- **Nombre de Threads** :
  Par défaut, l'outil utilise 10 threads. Vous pouvez modifier ce paramètre dans `main.py` :
  ```python
  scanner = SubdomainScanner(threads=20, use_ssl=True, ports=[80, 443])
  ```

- **Protocole (HTTP/HTTPS)** :
  Activez HTTPS en passant `use_ssl=True` dans l'initialisation du scanner.

- **Ports Personnalisés** :
  Ajoutez des ports spécifiques dans la liste `ports` :
  ```python
  scanner = SubdomainScanner(threads=10, use_ssl=False, ports=[80, 8080])
  ```

## Dépannage

- **Module Not Found** :
  Si vous obtenez une erreur `ModuleNotFoundError`, assurez-vous que les fichiers `SubdomainScannerTool.py` et `main.py` sont dans le même répertoire.

- **Erreur de Connexion** :
  Les erreurs comme `Connection Timeout` ou `Connection Refused` se produisent lorsque le serveur scanné ne répond pas ou refuse la connexion. Cela n'est pas un problème avec l'outil.

- **Problème de Permissions** :
  Assurez-vous que votre réseau ou pare-feu ne bloque pas les connexions sortantes.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez ajouter des fonctionnalités ou corriger des bogues, n'hésitez pas à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le distribuer.

---

**Auteur** : [MALICK-GITH002](https://github.com/MALICK-GITH002)
