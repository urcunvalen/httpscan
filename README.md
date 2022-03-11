# HTTPScan 

HTTPScan est un outil permettant de scanner de manière automatisée les en-têtes HTTP de sécurité d'un ensemble de site WEB.

## Installation

Dillinger requiert [shcheck.py](https://github.com/santoru/shcheck) pour fonctionner.

```sh
git clone https://github.com/santoru/shcheck.git
```

## Utilisation

HTTPScan peut-être utilisé de deux manières.

### En passant une URL spécifique en paramètre :

```sh
python3 httpscan.py url
```

> Note: Veuillez indiquer l'url complète : https://URL.com

### En se basant sur une liste d'URL :

Par défaut et en l'absence de paramètre, les urls sont à lister dans un fichier sans extension nommé **urls**, avec une URL par ligne.
Ce paramètre est modifiable dans les variables globales du fichier httpscan.py.

```sh
python3 httpscan.py
```
> Note: Veuillez indiquer les urls complètes : https://URL.com

Un dossier **Résultats/** est alors généré avec un fichier nominatif pour chaque URL scannée.