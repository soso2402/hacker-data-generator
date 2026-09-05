<!-- markdownlint-disable-file -->
# 🎭 Hacker Data Generator

> **⚠️ FAKE DATA / DEMO ONLY** - Programme de démonstration générant exclusivement des données fictives

Un programme Python autonome qui simule un **générateur de données façon hacker** directement dans le terminal avec effets visuels, animations et interface immersive.

## ✨ Caractéristiques

✅ **Données 100% fictives** - Aucune donnée réelle générée ou récupérée  
✅ **IP réservées aux exemples** - Utilise uniquement 192.0.2.x, 198.51.100.x et 203.0.113.x (RFC 5737)  
✅ **Adresses inventées** - Génère des adresses postales totalement fictives  
✅ **Effets visuels** - Couleurs ANSI (vert, rouge, cyan, jaune) et animations  
✅ **Interface hacker** - Écran de démarrage avec lignes [SYSTEM], [SCAN], [GENERATE], [DEMO]  
✅ **Effet machine à écrire** - Texte qui s'écrit caractère par caractère  
✅ **Animation de chargement** - Barre de progression avec symboles animés  
✅ **Contrôle utilisateur** - Choix du nombre de résultats (1-100)  
✅ **Arrêt sécurisé** - Appuyez sur Ctrl+C pour interrompre à tout moment  
✅ **Aucune connexion Internet** - Complètement autonome et offline  
✅ **Python 3.6+** - Code compatible avec les versions récentes de Python

## 🚀 Installation

### Prérequis
- Python 3.6 ou supérieur
- Terminal compatible ANSI (Linux, macOS, WSL, ou Windows 10+)

### Clonage du repository

```bash
git clone https://github.com/soso2402/hacker-data-generator.git
cd hacker-data-generator
```

## 💻 Utilisation

### Lancement simple

```bash
python3 hacker_data_gen.py
```

### Sur Windows

```bash
python hacker_data_gen.py
```

### Rendre le script exécutable (Linux/macOS)

```bash
chmod +x hacker_data_gen.py
./hacker_data_gen.py
```

## 📋 Guide d'utilisation

1. **Lancement** : Le programme affiche un écran de démarrage avec animation
2. **Entrée** : Entrez le nombre de résultats à générer (1-100)
3. **Génération** : Les données fictives s'affichent progressivement avec défilement
4. **Arrêt** : Appuyez sur **Ctrl+C** pour interrompre à tout moment
5. **Fin** : Le programme affiche un résumé et un avertissement de démonstration

## 📊 Exemple de sortie

```
╔════════════════════════════════════════════════════════════════════════════╗
║                 *** HACKER DATA GENERATOR v1.0 ***                        ║
║                     FAKE DATA / DEMO ONLY                                  ║
╚════════════════════════════════════════════════════════════════════════════╝

[SYSTEM] Initialisation des modules...
[SYSTEM] Vérification des droits d'accès...
[SCAN] Scan des données fictives...
✓ Système prêt

[DEMO] Génération de 5 enregistrements fictifs...

[RECORD #1]
  Username:  cyber_alice2847
  Name:       Alice Cipher
  IP Address: 192.0.2.142
  Address:    42 Rue Cyber, 75001 NeoCity (Sector-7)
  Email:      alice.cipher@nexus.fake
  Timestamp:  2026-09-05 12:36:12
  ├─────────────────────────────────────────────┤

Progress: [████████████████████████████████████████] 100.0%

✓ Génération terminée !
Total: 5 enregistrements fictifs générés
```

## 🔍 Données générées

### Adresses IP fictives
- **192.0.2.x** (TEST-NET-1)
- **198.51.100.x** (TEST-NET-2)
- **203.0.113.x** (TEST-NET-3)

Ces plages sont officiellement réservées par la RFC 5737 pour les exemples et la documentation, **jamais pour un usage réseau réel**.

### Adresses postales fictives
- Numéro de rue : 1-999
- Rues : Rue Cyber, Avenue Blockchain, Boulevard Quantum, etc.
- Codes postaux : 10000-99999
- Villes : NeoCity, CyberVille, DataTown, etc.
- Districts : District-01, Zone-A, Sector-7, etc.

### Autres données fictives
- **Usernames** : cyber_alice2847, data_bob5032, etc.
- **Noms** : Alice Cipher, Bob Knight, Charlie Overflow, etc.
- **Emails** : username@nexus.fake, username@cipher.demo, etc.
- **Timestamps** : Heure actuelle du système

## ⌨️ Contrôles

| Touche | Action |
|--------|--------|
| `1-9` puis `Entrée` | Entrer le nombre de résultats |
| `Ctrl+C` | Arrêter le programme à tout moment |

## 🛡️ Garanties de sécurité

✅ **Aucun accès réseau** - Le programme fonctionne 100% hors ligne  
✅ **Pas de scans** - Aucun réseau n'est scanné  
✅ **Pas de données réelles** - Toutes les données sont inventées  
✅ **Pas d'appels externes** - Aucune requête HTTP/HTTPS  
✅ **Pas de fichiers** - Les données ne sont pas écrites sur disque (sauf demande explicite)  
✅ **Code ouvert** - Lisible et auditable par tous

## 🎨 Palette de couleurs

Le programme utilise les couleurs ANSI suivantes :

- 🟢 **Vert** (`#92FF00`) - Succès, validations
- 🔴 **Rouge** (`#FF0000`) - Erreurs, avertissements
- 🔵 **Cyan** (`#00FFFF`) - Informations système
- 🟡 **Jaune** (`#FFFF00`) - Actions en cours
- 🟣 **Magenta** (`#FF00FF`) - En-têtes des enregistrements

## 📦 Structure du code

```
hacker_data_gen.py
├── Colors (classe)           # Codes ANSI pour les couleurs
├── HackerDataGenerator (classe)
│   ├── Données fictives      # IP ranges, noms, adresses, etc.
│   ├── Effets visuels        # Typewriter, animations
│   ├── Génération            # Création des données fictives
│   └── Affichage             # Formatage terminal
└── main()                    # Point d'entrée
```

## 🔧 Personnalisation

Vous pouvez facilement modifier :

- **Couleurs** : Éditez la classe `Colors` (codes ANSI)
- **Noms de rues** : Modifiez `FAKE_STREETS`
- **Villes** : Modifiez `FAKE_CITIES`
- **Délais d'animation** : Ajustez les paramètres `delay` et `time.sleep()`
- **Limite de résultats** : Changez le maximum de 100 à une autre valeur

## 📝 Licence

Ce projet est fourni à titre d'exemple et de démonstration éducative.

## ⚠️ Clause de non-responsabilité

Ce programme génère **UNIQUEMENT des données fictives**. Il est conçu à des fins éducatives et de démonstration. 

- Aucune donnée réelle n'est générée
- Aucune données n'est transmise sur Internet
- Le programme fonctionne complètement hors ligne
- Les adresses IP utilisées sont réservées aux exemples (RFC 5737)

## 🤝 Contribuer

Les contributions sont bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter de nouvelles données fictives
- Améliorer les effets visuels

## 📧 Support

Pour toute question ou suggestion, ouvrez une **issue** sur le repository GitHub.

---

**Made with ❤️ for educational purposes only** 🎓
