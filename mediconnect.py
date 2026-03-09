import json
import os
import hashlib
from datetime import datetime

# ── Where we save data ──────────────────────────────────
USERS_FILE = "data/users.json"
PRESC_FILE = "data/prescriptions.json"

# ── Insurance companies and their valid IDs ─────────────
INSURANCES = {
    "RSSB":   ["RSSB001", "RSSB002", "RSSB100"],
    "MMI":    ["MMI001",  "MMI002",  "MMI200"],
    "SORAS":  ["SOR001",  "SOR002",  "SOR300"],
    "BRITAM": ["BRI001",  "BRI002",  "BRI400"],
}

# ── Sicknesses and their medicines ──────────────────────
MEDICINES = {
    "Malaria":       ["Artemether", "Lumefantrine", "Quinine"],
    "Flu":           ["Paracetamol", "Vitamin C", "Antihistamine"],
    "Diabetes":      ["Metformin", "Insulin", "Glibenclamide"],
    "Hypertension":  ["Amlodipine", "Lisinopril", "Atenolol"],
    "Typhoid":       ["Ciprofloxacin", "Azithromycin", "Ceftriaxone"],
    "Stomach pain":  ["Omeprazole", "Buscopan", "Activated Charcoal"],
}

# ── Pharmacies: distance, rating, accepted insurances, sicknesses they treat ──
PHARMACIES = {
    "PharmaCare Plus":   {"km": 2.5, "rating": 4.8, "insurances": ["RSSB", "MMI"],                "sicknesses": ["Malaria", "Flu", "Typhoid"]},
    "City MedShop":      {"km": 3.1, "rating": 4.5, "insurances": ["SORAS", "BRITAM"],            "sicknesses": ["Diabetes", "Hypertension", "Stomach pain"]},
    "HealthFirst":       {"km": 4.0, "rating": 4.2, "insurances": ["RSSB", "SORAS"],              "sicknesses": ["Flu", "Hypertension", "Malaria"]},
    "MediQuick":         {"km": 1.8, "rating": 4.6, "insurances": ["MMI", "BRITAM"],              "sicknesses": ["Typhoid", "Diabetes", "Stomach pain"]},
    "People's Pharmacy": {"km": 5.2, "rating": 3.9, "insurances": ["RSSB", "BRITAM", "MMI", "SORAS"], "sicknesses": ["Flu", "Malaria", "Stomach pain"]},
}


# ════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ════════════════════════════════════════════════════════

def load_data(filename):
    """Load data from a JSON file. Return empty dict if file doesn't exist."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}


def save_data(filename, data):
    """Save data to a JSON file."""
    os.makedirs("data", exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def hash_password(password):
    """Convert password to a secure hash before saving."""
    return hashlib.sha256(password.encode()).hexdigest()


def divider():
    print("\n" + "-" * 40)


def wait():
    input("\nPress Enter to continue...")


def pick_from_list(options, prompt):
    """Show a numbered list and return the item the user picks."""
    for i, item in enumerate(options, 1):
        print(f"  {i}. {item}")
    while True:
        choice = input(f"\n{prompt}: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("  Invalid choice. Try again.")
