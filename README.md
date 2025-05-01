# IMS-Lookup
---

```markdown
# IMS Lookup 🔍📞

**IMS Lookup** is a terminal-based phone number lookup tool built on leaked **IndiaMART** data. It allows you to query across multiple `.xlsx` databases and instantly retrieve matching information.

---

## ⚠️ Disclaimer

This tool is intended for **educational and research purposes only**. Any use of this data must comply with applicable laws and ethical guidelines. The author is **not responsible** for any misuse.

---

## 📦 Installation

```bash
git clone https://github.com/CarlosMasio/IMS-Lookup.git
cd IMS-Lookup
```

---

## 📁 Database Installation

The database files are too large to host directly on GitHub.

To install:

```bash
wget http://192.168.228.74:8000/databases.zip
```

> ❗Access to this file is private.  
> 📩 **Contact me on Instagram**: [@ig.masio](https://instagram.com/ig.masio) for credentials or access permissions.

Then:

```bash
unzip databases.zip
```

---

## ⚙️ Setup

Make sure the necessary files are executable:

```bash
chmod +x ph.sh
chmod +x search_phone.py
```

---

## 🚀 Usage

Run the script with:

```bash
./ph.sh
```

Follow the prompt to enter a phone number, and the script will search across all 6 database files inside the `databases/` folder.

---

## 📚 Structure

- `search_phone.py`: Python script that searches the `.xlsx` files for matching phone numbers.
- `ph.sh`: Shell script that prompts the user and runs the Python script.
- `databases/`: Folder where all `.xlsx` files must be placed after extracting `databases.zip`.

---

## 📞 Support

For help or access to the database:
- DM on Instagram: [@ig.masio](https://instagram.com/ig.masio)

---
```

Would you like me to add license info or usage examples with sample output as well?
