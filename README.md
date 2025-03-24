📬 PubMP - Bot Discord d'envoi automatique de MP

Ce bot Discord envoie automatiquement un message privé à chaque membre (non-bot) d’un serveur dès qu’il est ajouté, puis quitte le serveur. Il est aussi possible de déclencher l’envoi manuellement via la commande /pub.

🔧 Configuration

Assure-toi d’avoir un fichier config.json dans le même dossier que le script, avec ce format :

{
  "token": " ",

  "lien": " ",

  "message": " "
}

Variables :
- token : le token de ton bot Discord
- lien : le lien que tu veux inclure dans les messages
- message : le message à envoyer (tu peux utiliser {user} pour mentionner le destinataire)

📦 Dépendances

Installe les modules nécessaires avec (ou lance juste le bot avec le start.bat qu'il le fera automatiquement) :

pip install discord.py pystyle

▶️ Utilisation

Lance le bot :

python main.py

Fonctionnalités :
- Envoi automatique du message dès que le bot rejoint un serveur
- Commande /pub disponible pour envoyer les messages manuellement
- Le bot quitte le serveur après l'envoi des messages
- Le message peut contenir la variable {user}, qui sera remplacée par une mention de l'utilisateur 

⚠️ Avertissement

L'utilisation abusive de ce script peut violer les Conditions d'utilisation de Discord. Utilisez-le uniquement dans des contextes autorisés.

Développé par eden.pyc ❤️ Forked by sl0wdown
