#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════════════════╗
║              HACKER DATA GENERATOR - ADVANCED EDITION                      ║
║                          FAKE DATA / DEMO ONLY                             ║
║                                                                            ║
║  Version avancée avec options supplémentaires et mode interactif.         ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

import sys
import time
import random
from typing import List, Dict

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

class AdvancedHackerDataGenerator:
    """Générateur avancé de données fictives avec options étendues"""

    FAKE_IP_RANGES = ["192.0.2.", "198.51.100.", "203.0.113."]
    
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

    PHONE_PREFIXES = ["+33", "+1", "+44", "+49", "+39"]
    DEPARTMENTS = ["Engineering", "Security", "Data Science", "Infrastructure", "Operations"]

    def __init__(self):
        """Initialisation du générateur"""
        self.data_generated = []
        self.export_format = "terminal"

    def typewriter_effect(self, text: str, delay: float = 0.02, color: str = Colors.RESET) -> None:
        """Affiche du texte caractère par caractère"""
        for char in text:
            sys.stdout.write(f"{color}{char}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def loading_animation(self, duration: float = 2.0, message: str = "Traitement") -> None:
        """Affiche une animation de chargement"""
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        end_time = time.time() + duration
        
        while time.time() < end_time:
            for frame in frames:
                sys.stdout.write(f"\r{Colors.CYAN}{frame} {message}...{Colors.RESET}")
                sys.stdout.flush()
                time.sleep(0.08)
        
        print(f"\r{Colors.GREEN}✓ {message} terminé{Colors.RESET}                    ")

    def display_menu(self) -> None:
        """Affiche le menu principal"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}╔════════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}║          HACKER DATA GENERATOR - MENU AVANCÉ                ║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}╚════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}[1]{Colors.RESET} Générer des données (mode standard)")
        print(f"{Colors.YELLOW}[2]{Colors.RESET} Générer avec adresses professionnelles")
        print(f"{Colors.YELLOW}[3]{Colors.RESET} Générer avec numéros de téléphone")
        print(f"{Colors.YELLOW}[4]{Colors.RESET} Générer des données étendues (tous les champs)")
        print(f"{Colors.YELLOW}[5]{Colors.RESET} Statistiques sur les données générées")
        print(f"{Colors.YELLOW}[0]{Colors.RESET} Quitter")
        print()

    def generate_phone(self) -> str:
        """Génère un numéro de téléphone fictif"""
        prefix = random.choice(self.PHONE_PREFIXES)
        number = "".join(str(random.randint(0, 9)) for _ in range(9))
        return f"{prefix} {number[:3]} {number[3:6]} {number[6:]}"

    def generate_department_email(self) -> tuple:
        """Génère un email professionnel fictif"""
        dept = random.choice(self.DEPARTMENTS).lower().replace(" ", "_")
        name = random.choice(self.FAKE_NAMES).lower().replace(" ", ".")
        email = f"{name}@{dept}.fake"
        return email, dept

    def generate_employee_id(self) -> str:
        """Génère un ID employé fictif"""
        dept_prefix = random.choice([d[:3].upper() for d in self.DEPARTMENTS])
        number = random.randint(10000, 99999)
        return f"{dept_prefix}-{number}"

    def generate_standard_record(self) -> dict:
        """Génère un enregistrement standard"""
        return {
            "username": f"cyber_{random.choice(self.FAKE_NAMES).lower().split()[0]}{random.randint(100, 9999)}",
            "name": random.choice(self.FAKE_NAMES),
            "ip": f"{random.choice(self.FAKE_IP_RANGES)}{random.randint(0, 255)}",
            "address": f"{random.randint(1, 999)} {random.choice(self.FAKE_STREETS)}, {random.randint(10000, 99999)} {random.choice(self.FAKE_CITIES)}",
            "email": f"{random.choice(self.FAKE_NAMES).lower().replace(' ', '.')}@nexus.fake",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

    def generate_professional_record(self) -> dict:
        """Génère un enregistrement avec informations professionnelles"""
        record = self.generate_standard_record()
        email, dept = self.generate_department_email()
        record.update({
            "employee_id": self.generate_employee_id(),
            "department": dept.replace("_", " ").title(),
            "work_email": email,
            "phone": self.generate_phone()
        })
        return record

    def generate_extended_record(self) -> dict:
        """Génère un enregistrement avec tous les champs étendus"""
        record = self.generate_professional_record()
        record.update({
            "district": random.choice(self.FAKE_DISTRICTS),
            "access_level": random.choice(["USER", "ADMIN", "GUEST", "SYSTEM"]),
            "status": random.choice(["ACTIVE", "INACTIVE", "SUSPENDED"]),
            "last_login": (time.time() - random.randint(0, 2592000))
        })
        return record

    def display_record(self, record: dict, index: int, record_type: str = "standard") -> None:
        """Affiche un enregistrement formaté"""
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}[RECORD #{index}]{Colors.RESET}")
        print(f"  {Colors.CYAN}Username:{Colors.RESET}    {Colors.BRIGHT}{record['username']}{Colors.RESET}")
        print(f"  {Colors.GREEN}Name:{Colors.RESET}        {record['name']}")
        print(f"  {Colors.YELLOW}IP Address:{Colors.RESET}  {Colors.BRIGHT}{record['ip']}{Colors.RESET}")
        print(f"  {Colors.RED}Address:{Colors.RESET}     {record['address']}")
        print(f"  {Colors.BLUE}Email:{Colors.RESET}       {record['email']}")
        
        if record_type in ["professional", "extended"]:
            print(f"  {Colors.MAGENTA}Employee ID:{Colors.RESET} {record.get('employee_id', 'N/A')}")
            print(f"  {Colors.CYAN}Department:{Colors.RESET}  {record.get('department', 'N/A')}")
            print(f"  {Colors.GREEN}Work Email:{Colors.RESET} {record.get('work_email', 'N/A')}")
            print(f"  {Colors.YELLOW}Phone:{Colors.RESET}      {record.get('phone', 'N/A')}")
        
        if record_type == "extended":
            print(f"  {Colors.BLUE}District:{Colors.RESET}    {record.get('district', 'N/A')}")
            print(f"  {Colors.RED}Access Level:{Colors.RESET} {record.get('access_level', 'N/A')}")
            print(f"  {Colors.MAGENTA}Status:{Colors.RESET}     {record.get('status', 'N/A')}")
        
        print(f"  {Colors.DIM}Timestamp:{Colors.RESET}   {record['timestamp']}")
        print(f"  {Colors.CYAN}├─────────────────────────────────────────────┤{Colors.RESET}")

    def generate_and_display(self, count: int, record_type: str = "standard") -> None:
        """Génère et affiche les données"""
        type_labels = {
            "standard": "données standard",
            "professional": "données professionnelles",
            "extended": "données étendues"
        }
        
        print(f"\n{Colors.GREEN}{Colors.BOLD}[DEMO] Génération de {count} enregistrements {type_labels[record_type]}...{Colors.RESET}\n")
        
        try:
            for i in range(1, count + 1):
                if record_type == "standard":
                    record = self.generate_standard_record()
                elif record_type == "professional":
                    record = self.generate_professional_record()
                else:
                    record = self.generate_extended_record()
                
                self.data_generated.append(record)
                self.display_record(record, i, record_type)
                time.sleep(0.3)
                
                progress = (i / count) * 100
                bar_length = 40
                filled = int(bar_length * i / count)
                bar = "█" * filled + "░" * (bar_length - filled)
                sys.stdout.write(f"\r{Colors.CYAN}Progress: [{bar}] {progress:.1f}%{Colors.RESET}")
                sys.stdout.flush()
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.RED}{Colors.BOLD}⚠ Interruption (Ctrl+C){Colors.RESET}")
            print(f"{Colors.YELLOW}{len(self.data_generated)} enregistrements générés.{Colors.RESET}\n")
            return

        print(f"\n\n{Colors.GREEN}{Colors.BOLD}✓ Génération terminée !{Colors.RESET}")
        print(f"{Colors.CYAN}Total: {len(self.data_generated)} enregistrements générés{Colors.RESET}\n")

    def display_statistics(self) -> None:
        """Affiche les statistiques des données générées"""
        if not self.data_generated:
            print(f"{Colors.RED}Aucune donnée générée. Générez d'abord des données.{Colors.RESET}\n")
            return
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}═══════════════════════════════════════════════════════{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.MAGENTA}STATISTIQUES DES DONNÉES GÉNÉRÉES{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}═══════════════════════════════════════════════════════{Colors.RESET}\n")
        
        total = len(self.data_generated)
        
        print(f"  {Colors.CYAN}Nombre total d'enregistrements:{Colors.RESET} {Colors.BRIGHT}{total}{Colors.RESET}")
        
        if total > 0:
            unique_names = len(set(r['name'] for r in self.data_generated))
            unique_ips = len(set(r['ip'] for r in self.data_generated))
            unique_cities = len(set(r['address'].split(',')[-1].strip() for r in self.data_generated))
            
            print(f"  {Colors.GREEN}Noms uniques:{Colors.RESET}         {unique_names}")
            print(f"  {Colors.YELLOW}Adresses IP uniques:{Colors.RESET} {unique_ips}")
            print(f"  {Colors.BLUE}Villes uniques:{Colors.RESET}       {unique_cities}")
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}═══════════════════════════════════════════════════════{Colors.RESET}\n")

    def display_warning(self) -> None:
        """Affiche l'avertissement de démonstration"""
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
        """Lance l'interface interactive"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}")
        print("╔════════════════════════════════════════════════════════════════════════════╗")
        print("║                   *** HACKER DATA GENERATOR ***                           ║")
        print("║                        ADVANCED EDITION                                   ║")
        print("║                     FAKE DATA / DEMO ONLY                                  ║")
        print("╚════════════════════════════════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}\n")
        
        self.loading_animation(1.5, "Initialisation")
        
        while True:
            self.display_menu()
            
            try:
                choice = input(f"{Colors.YELLOW}Sélectionnez une option: {Colors.RESET}").strip()
                
                if choice == "0":
                    print(f"\n{Colors.YELLOW}Programme arrêté. À bientôt !{Colors.RESET}\n")
                    break
                
                elif choice in ["1", "2", "3", "4"]:
                    while True:
                        try:
                            count = int(input(f"{Colors.YELLOW}Nombre de résultats (1-100): {Colors.RESET}"))
                            if 1 <= count <= 100:
                                break
                            else:
                                print(f"{Colors.RED}Veuillez entrer un nombre entre 1 et 100.{Colors.RESET}")
                        except ValueError:
                            print(f"{Colors.RED}Entrée invalide.{Colors.RESET}")
                    
                    if choice == "1":
                        self.generate_and_display(count, "standard")
                    elif choice == "2":
                        self.generate_and_display(count, "professional")
                    elif choice == "3":
                        self.generate_and_display(count, "professional")
                    elif choice == "4":
                        self.generate_and_display(count, "extended")
                
                elif choice == "5":
                    self.display_statistics()
                
                else:
                    print(f"{Colors.RED}Option invalide. Veuillez réessayer.{Colors.RESET}")
                
                input(f"{Colors.DIM}Appuyez sur Entrée pour continuer...{Colors.RESET}")
                
            except KeyboardInterrupt:
                print(f"\n{Colors.RED}{Colors.BOLD}Programme arrêté.{Colors.RESET}\n")
                break
            except Exception as e:
                print(f"{Colors.RED}Erreur: {e}{Colors.RESET}\n")
        
        if self.data_generated:
            self.display_warning()


def main():
    """Point d'entrée du programme"""
    try:
        generator = AdvancedHackerDataGenerator()
        generator.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}{Colors.BOLD}Programme interrompu.{Colors.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}Erreur fatale: {e}{Colors.RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
