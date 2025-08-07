import os
import uuid
import winreg
from cryptography.fernet import Fernet
import base64
import hashlib

# === Configuration ===
APP_NAME = "YourAppName"
REGISTRY_PATH = fr"Software\{APP_NAME}"
APPDATA_DIR = os.path.join(os.getenv("APPDATA"), APP_NAME)
LICENSE_FILE_PATH = os.path.join(APPDATA_DIR, "license.dat")

# === SALT for Encryption ===
# DO NOT expose this publicly in production. Use a secure backend if possible.
SALT = b"YourSecretSalt_KeepItSafe"

# === Generate encryption key from salt + device ID ===
def generate_encryption_key(device_id):
    key = hashlib.pbkdf2_hmac("sha256", SALT, device_id.encode(), 100000)
    return base64.urlsafe_b64encode(key[:32])  # Fernet requires 32-byte key

# === Encrypt license key ===
def encrypt_license(license_key, device_id):
    f = Fernet(generate_encryption_key(device_id))
    return f.encrypt(license_key.encode())

# === Decrypt license key ===
def decrypt_license(encrypted_license, device_id):
    f = Fernet(generate_encryption_key(device_id))
    return f.decrypt(encrypted_license).decode()

# === Registry functions ===
def save_device_id_to_registry(device_id):
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, REGISTRY_PATH)
    winreg.SetValueEx(key, "DeviceID", 0, winreg.REG_SZ, device_id)
    winreg.CloseKey(key)

def get_device_id_from_registry():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REGISTRY_PATH)
        value, _ = winreg.QueryValueEx(key, "DeviceID")
        winreg.CloseKey(key)
        return value
    except FileNotFoundError:
        return None

# === Save/load encrypted license to/from file ===
def save_encrypted_license(encrypted_license):
    os.makedirs(APPDATA_DIR, exist_ok=True)
    with open(LICENSE_FILE_PATH, "wb") as f:
        f.write(encrypted_license)

def load_encrypted_license():
    if not os.path.exists(LICENSE_FILE_PATH):
        return None
    with open(LICENSE_FILE_PATH, "rb") as f:
        return f.read()

# === Remove (deactivate) license key ===
def remove_license_key():
    if os.path.exists(LICENSE_FILE_PATH):
        os.remove(LICENSE_FILE_PATH)
        print("🧹 License key removed.")
    else:
        print("ℹ️ No license key found to remove.")

# === Main menu/interaction logic ===
def initialize():
    device_id = get_device_id_from_registry()
    if not device_id:
        device_id = str(uuid.uuid4())
        save_device_id_to_registry(device_id)
        print("📌 Device ID generated and stored.\n")

    while True:
        print("\n=== License Manager ===")
        print("1. Check license key")
        print("2. Enter new license key")
        print("3. Remove license key")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            encrypted_license = load_encrypted_license()
            if encrypted_license:
                try:
                    license_key = decrypt_license(encrypted_license, device_id)
                    print(f"✅ License key: {license_key}")
                except Exception as e:
                    print(f"❌ Failed to decrypt license key: {e}")
            else:
                print("⚠️ No license key found.")
        
        elif choice == "2":
            license_key = input("🔑 Enter your license key: ").strip()
            encrypted = encrypt_license(license_key, device_id)
            save_encrypted_license(encrypted)
            print("✅ License key encrypted and stored.")
        
        elif choice == "3":
            remove_license_key()
        
        elif choice == "4":
            print("👋 Exiting.")
            break

        else:
            print("❌ Invalid choice. Try again.")

# === Entry point ===
if __name__ == "__main__":
    initialize()
