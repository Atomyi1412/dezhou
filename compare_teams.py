import pandas as pd
import os

def normalize_col(name):
    return str(name).strip()

def find_columns(df):
    # Try to find header row
    for i in range(min(5, len(df))):
        row = df.iloc[i].astype(str).tolist()
        serial_idx = -1
        name_idx = -1
        
        for idx, val in enumerate(row):
            if '序号' in val or 'No' in val or 'ID' in val:
                serial_idx = idx
            if '队伍名称' in val or 'Team' in val:
                name_idx = idx
                
        if serial_idx != -1 and name_idx != -1:
            return i + 1, serial_idx, name_idx
    return 0, 0, 1 # Default

def load_and_extract(filepath):
    print(f"Loading {filepath}...")
    try:
        df = pd.read_excel(filepath, header=None)
        start_row, serial_col, name_col = find_columns(df)
        print(f"  Found headers at row {start_row}, Serial col: {serial_col}, Name col: {name_col}")
        
        data = {}
        for i in range(start_row, len(df)):
            row = df.iloc[i]
            try:
                serial = str(row.iloc[serial_col]).strip()
                if serial.endswith('.0'): serial = serial[:-2]
                name = str(row.iloc[name_col]).strip() if pd.notna(row.iloc[name_col]) else ""
                
                # Only keep valid serials (numeric)
                if serial and serial.lower() != 'nan':
                    data[serial] = name
            except Exception as e:
                continue
        return data
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return {}

file_teams = r"e:\trae\dezhou\2025圣诞大冒险组队报名表 (1).xlsx"
file_import = r"e:\trae\dezhou\圣诞积分统计明细.xlsx"

teams_ref = load_and_extract(file_teams)
teams_imp = load_and_extract(file_import)

print("\nComparing specific serials (12, 32, 39, 42):")
targets = ['12', '32', '39', '42']

for serial in targets:
    name_ref = teams_ref.get(serial, "NOT FOUND")
    name_imp = teams_imp.get(serial, "NOT FOUND")
    
    print(f"\nSerial {serial}:")
    print(f"  Ref (Team List): {repr(name_ref)}")
    print(f"  Imp (Import)   : {repr(name_imp)}")
    
    if name_ref != name_imp:
        print("  MISMATCH DETECTED!")
        # Analyze diff
        if name_ref == "NOT FOUND" or name_imp == "NOT FOUND":
            continue
            
        # Character by character comparison
        print("  Char comparison:")
        len_ref = len(name_ref)
        len_imp = len(name_imp)
        max_len = max(len_ref, len_imp)
        for i in range(max_len):
            c1 = name_ref[i] if i < len_ref else 'EOF'
            c2 = name_imp[i] if i < len_imp else 'EOF'
            if c1 != c2:
                o1 = ord(c1) if c1 != 'EOF' else 0
                o2 = ord(c2) if c2 != 'EOF' else 0
                print(f"    Idx {i}: Ref '{c1}' ({o1}) vs Imp '{c2}' ({o2})")
