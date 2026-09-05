#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════════════════╗
║                    HACKER DATA GENERATOR - DEMO ONLY                       ║
║                                                                            ║
║  Ce programme génère UNIQUEMENT des données fictives pour démonstration.  ║
║  Aucune donnée réelle n'est récupérée ou transmise sur Internet.          ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

import sys
import time
import random
from typing import List, Tuple

# Codes ANSI pour les couleurs
class Colors:
    """Palette de couleurs ANSI pour le terminal"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    BRIGHT = '\033[1m'

class HackerDataGenerator:
    """Générateur de données fictives avec interface hacker"""

    # Données fictives réservées aux exemples
    FAKE_IP_RANGES = [
        "192.0.2.",
        "198.51.100.",
        "203.0.113."
    ]

    FAKE_STREETS = [
        "Rue Cyber", "Avenue Blockchain", "Boulevard Quantum",
        "Chemin Données", "Place Réseau", "Impasse Serveur",
        "Route Algorithme", "Voie Cryptage", "Allée Binaire",
        "Passage Pixel", "Square Digital", "Cours Système"
    ]

    FAKE_CITIES = [
        "NeoCity", "CyberVille", "DataTown", "NetworkOpolis",
        "QuantumHaven", "TechMetropolis", "ByteCity", "CloudVille",
        "DigitalPort", "SynergyHub", "VirtualCity", "CodeZone"
    ]

    FAKE_DISTRICTS = [
        "District-01", "Zone-A", "Sector-7", "Hub-42",
        "Node-XIII", "Cluster-9", "Vertex-5", "Portal-22"
    ]

    FAKE_NAMES = [
        "Alice Cipher", "Bob Knight", "Charlie Overflow", "Diana Router",
        "Eve Packet", "Frank Loop", "Grace Terminal", "Henry Cache",
        "Iris Socket", "Jack Protocol", "Kate Buffer", "Leon Stream"
    ]

    def __init__(self):
        """Initialisation du générateur"""
        self.count = 0
        self.data_generated = []

    def typewriter_effect(self, text: str, delay: float = 0.02, color: str = Colors.RESET) -> None:
        """Affiche du texte caractère par caractère (effet machine à écrire)"""
        for char in text:
            sys.stdout.write(f"{color}{char}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def loading_animation(self, duration: float = 2.0) -> None:
        """Affiche une animation de chargement"""
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        end_time = time.time() + duration
        
        while time.time() < end_time:
            for frame in frames:
                sys.stdout.write(f"\r{Colors.CYAN}{frame} Initialisation du système...{Colors.RESET}")
                sys.stdout.flush()
                time.sleep(0.08)
        
        print(f"\r{Colors.GREEN}✓ Système prêt{Colors.RESET}                    ")

    def display_startup_screen(self) -> None:
        """Affiche l'écran de démarrage hacker"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}")
        print("╔════════════════════════════════════════════════════════════════════════════╗")
        print("║                                                                            ║")
        print("║                 *** HACKER DATA GENERATOR v1.0 ***                        ║")
        print("║                     FAKE DATA / DEMO ONLY                                  ║")
        print("║                                                                            ║")
        print("╚════════════════════════════════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}\n")

        # Simulation du démarrage système
        self.typewriter_effect("[SYSTEM] Initialisation des modules...", color=Colors.YELLOW)
        time.sleep(0.3)
        self.typewriter_effect("[SYSTEM] Vérification des droits d'accès...", color=Colors.YELLOW)
        time.sleep(0.3)
        self.typewriter_effect("[SCAN] Scan des données fictives...", color=Colors.CYAN)
        time.sleep(0.3)
        
        self.loading_animation(1.5)
        
        self.typewriter_effect("[GENERATE] Préparation du générateur...", color=Colors.YELLOW)
        time.sleep(0.3)
        self.typewriter_effect(f"{Colors.GREEN}[SUCCESS] Tous les systèmes actifs{Colors.RESET}", 
                              color=Colors.GREEN)
        print()

    def generate_fake_ip(self) -> str:
        """Génère une adresse IP fictive"""
        ip_range = random.choice(self.FAKE_IP_RANGES)
        last_octet = random.randint(0, 255)
        return f"{ip_range}{last_octet}"

    def generate_fake_address(self) -> str:
        """Génère une adresse postale fictive"""
        street_number = random.randint(1, 999)
        street_name = random.choice(self.FAKE_STREETS)
        postal_code = random.randint(10000, 99999)
        city = random.choice(self.FAKE_CITIES)
        district = random.choice(self.FAKE_DISTRICTS)
        
        return f"{street_number} {street_name}, {postal_code} {city} ({district})"

    def generate_fake_email(self) -> str:
        """Génère un email fictif"""
        domains = ["nexus.fake", "cipher.demo", "quantum.local", "digital.net"]
        username = random.choice(self.FAKE_NAMES).lower().replace(" ", ".")
        domain = random.choice(domains)
        return f"{username}@{domain}"

    def generate_fake_username(self) -> str:
        """Génère un nom d'utilisateur fictif"""
        prefixes = ["cyber_", "data_", "net_", "sys_", "bit_"]
        suffixes = [str(random.randint(100, 9999)) for _ in range(1)]
        return f"{random.choice(prefixes)}{random.choice(self.FAKE_NAMES).lower().split()[0]}{random.choice(suffixes)}"

    def generate_single_record(self) -> dict:
        """Génère un seul enregistrement fictif"""
        return {
            "username": self.generate_fake_username(),
            "name": random.choice(self.FAKE_NAMES),
            "ip": self.generate_fake_ip(),
            "address": self.generate_fake_address(),
            "email": self.generate_fake_email(),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

    def display_record(self, record: dict, index: int) -> None:
        """Affiche un enregistrement avec formatage"""
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}[RECORD #{index}]{Colors.RESET}")
        print(f"  {Colors.CYAN}Username:{Colors.RESET}  {Colors.BRIGHT}{record['username']}{Colors.RESET}")
        print(f"  {Colors.GREEN}Name:{Colors.RESET}       {record['name']}")
        print(f"  {Colors.YELLOW}IP Address:{Colors.RESET} {Colors.BRIGHT}{record['ip']}{Colors.RESET}")
        print(f"  {Colors.RED}Address:{Colors.RESET}    {record['address']}")
        print(f"  {Colors.BLUE}Email:{Colors.RESET}      {record['email']}")
        print(f"  {Colors.DIM}Timestamp:{Colors.RESET}   {record['timestamp']}")
        print(f"  {Colors.CYAN}├─────────────────────────────────────────────┤{Colors.RESET}")

    def generate_data(self, count: int) -> None:
        """Génère et affiche les données fictives"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}[DEMO] Génération de {count} enregistrements fictifs...{Colors.RESET}\n")
        
        try:
            for i in range(1, count + 1):
                # Affichage de la progression
                record = self.generate_single_record()
                self.data_generated.append(record)
                
                # Affichage progressif du record
                self.display_record(record, i)
                
                # Délai pour l'effet de défilement
                time.sleep(0.3)
                
                # Barre de progression
                progress = (i / count) * 100
                bar_length = 40
                filled = int(bar_length * i / count)
                bar = "█" * filled + "░" * (bar_length - filled)
                sys.stdout.write(f"\r{Colors.CYAN}Progress: [{bar}] {progress:.1f}%{Colors.RESET}")
                sys.stdout.flush()
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.RED}{Colors.BOLD}⚠ Interruption de l'utilisateur (Ctrl+C){Colors.RESET}")
            print(f"{Colors.YELLOW}{len(self.data_generated)} enregistrements générés avant l'arrêt.{Colors.RESET}\n")
            return

        print(f"\n\n{Colors.GREEN}{Colors.BOLD}✓ Génération terminée !{Colors.RESET}")
        print(f"{Colors.CYAN}Total: {len(self.data_generated)} enregistrements fictifs générés{Colors.RESET}\n")

    def display_demo_warning(self) -> None:
        """Affiche un avertissement de démonstration"""
        print(f"\n{Colors.BOLD}{Colors.RED}")
        print("╔════════════════════════════════════════════════════════════════════════════╗")
        print("║                         ⚠ FAKE DATA / DEMO ONLY ⚠                         ║")
        print("║                                                                            ║")
        print("║  • Toutes les données sont ENTIÈREMENT FICTIVES                           ║")
        print("║  • Les adresses IP utilisent les plages réservées aux exemples (RFC 5737) ║")
        print("║  • Aucune donnée réelle n'a été récupérée                                 ║")
        print("║  • Aucune donnée n'a été transmise sur Internet                           ║")
        print("║  • Ce programme est uniquement à des fins de démonstration                ║")
        print("║                                                                            ║")
        print("╚════════════════════════════════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}\n")

    def run(self) -> None:
        """Lance le programme principal"""
        self.display_startup_screen()
        
        # Demande du nombre de résultats
        while True:
            try:
                user_input = input(f"{Colors.YELLOW}Nombre de résultats à générer (1-100): {Colors.RESET}")
                count = int(user_input)
                
                if 1 <= count <= 100:
                    break
                else:
                    print(f"{Colors.RED}Veuillez entrer un nombre entre 1 et 100.{Colors.RESET}")
            except ValueError:
                print(f"{Colors.RED}Entrée invalide. Veuillez entrer un nombre.{Colors.RESET}")
            except KeyboardInterrupt:
                print(f"\n{Colors.RED}{Colors.BOLD}Programme arrêté par l'utilisateur.{Colors.RESET}\n")
                sys.exit(0)

        # Génération des données
        self.generate_data(count)
        
        # Affichage de l'avertissement
        self.display_demo_warning()
        
        # Message de fin
        print(f"{Colors.GREEN}{Colors.BOLD}[DEMO] Simulation terminée avec succès{Colors.RESET}")
        print(f"{Colors.CYAN}Appuyez sur Ctrl+C pour quitter le programme.{Colors.RESET}\n")


def main():
    """Point d'entrée du programme"""
    try:
        generator = HackerDataGenerator()
        generator.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}{Colors.BOLD}Programme arrêté.{Colors.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}Erreur: {e}{Colors.RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
