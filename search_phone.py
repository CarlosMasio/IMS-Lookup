#!/usr/bin/env python3

import pandas as pd
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 search_phone.py <phone_number>")
        return

    phone_number = sys.argv[1]
    database_dir = "databases"

    if not os.path.isdir(database_dir):
        print(f"❌ Folder '{database_dir}' not found.")
        return

    for i in range(1, 7):
        file_path = os.path.join(database_dir, f'IMS[{i}].xlsx')
        if not os.path.isfile(file_path):
            continue

        try:
            xls = pd.ExcelFile(file_path, engine='openpyxl')
            for sheet in xls.sheet_names:
                df = xls.parse(sheet)
                for col in df.columns:
                    matches = df[df[col].astype(str).str.contains(phone_number, na=False)]
                    if not matches.empty:
                        print(f"\n✅ Match found in: {file_path}, sheet: {sheet}\n")
                        for _, row in matches.iterrows():
                            print(" • " + ", ".join(f"{col}: {row[col]}" for col in df.columns))
                        return
        except Exception as e:
            print(f"⚠️ Error reading {file_path}: {e}")

    print(f"❌ Phone number '{phone_number}' is not associated with the database.")

if __name__ == "__main__":
    main()
