# Programme Python : Readme

Ce programme permet d'envoyer un message personnalisé contenant un lien à tous les membres d'un serveur Discord sur lequel le bot est présent. Il utilise la librairie `discord.py` pour interagir avec l'API Discord et le module `pystyle` pour afficher des messages colorés dans la console. Le programme lit la configuration (token, lien et message) depuis le fichier `config.json`.

## Installation des modules `pystyle` et `discord.py`

Les modules `pystyle` et `discord.py` peuvent être installés à l'aide de `pip`. Pour cela, ouvrez un terminal et exécutez la commande suivante :

```bash
pip install pystyle
pip install discord.py
```

## Utilisation du programme

### Configuration

Avant de lancer le programme, vous devez configurer les paramètres dans le fichier `config.json`. Les paramètres disponibles sont :

- `"token"` : le token de votre bot Discord.
- `"lien"` : le lien que vous souhaitez envoyer.
- `"message"` : le message que vous souhaitez envoyer.

Vous devez remplir les champs correspondants dans le fichier `config.json` avant d'exécuter le programme.

### Lancement du programme

Une fois que vous avez configuré les paramètres dans le fichier `config.json`, vous pouvez lancer le programme en exécutant le fichier `main.py`.

Un `/pub` est intégré.

Le bot va maintenant envoyer le message personnalisé contenant le lien à tous les membres du serveur et quittera automatiquement le serveur.

### Licence

Ce programme est sous licence MIT. Veuillez consulter le fichier `LICENSE` pour plus d'informations.
