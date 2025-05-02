# IMS Lookup 🔍📞

**IMS Lookup** is a terminal-based phone number lookup tool built on leaked **IndiaMART** data. It allows you to query across multiple `.xlsx` databases and instantly retrieve matching information.

---

## ⚠️ Disclaimer

This tool is intended for **educational and research purposes only**. Any use of this data must comply with applicable laws and ethical guidelines. The author is **not responsible** for any misuse.

---

## 🧰 Requirements

Make sure you have Python 3 and `pip` installed.

Install required Python packages:

```bash
pip3 install pandas openpyxl
````

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

Make sure the extracted `.xlsx` files are placed inside a folder called `databases/`.

---

## ⚙️ Setup

Make the main files executable:

```bash
chmod +x ph.sh
chmod +x search_phone.py
```

---

## 🚀 Usage

Run the script:

```bash
./ph.sh
```

Enter a phone number when prompted. The tool will search through all 6 `.xlsx` files inside the `databases/` folder and print matching details line by line.

If the number is not found, it will display:

```
This phone number is not associated with the database.
```

---

## 📚 Structure

* `search_phone.py`: Python script that searches the `.xlsx` files for matching phone numbers.
* `ph.sh`: Bash script that prompts for input and runs the Python script.
* `databases/`: Folder containing all `.xlsx` files (from `databases.zip`).

---

## 📞 Support

For help or access to the database:

* DM me on Instagram: [@ig.masio](https://instagram.com/ig.masio)
---
