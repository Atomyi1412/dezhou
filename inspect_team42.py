import pandas as pd
import openpyxl

file_path = r"e:\trae\dezhou\2025圣诞大冒险组队报名表 (1).xlsx"

print(f"Inspecting {file_path}...")

try:
    # Use openpyxl engine to get more details if needed, but pandas is easier for quick look
    df = pd.read_excel(file_path, header=None)
    
    # Find header
    start_row = 0
    col_serial = -1
    col_name = -1
    
    for i in range(min(20, len(df))):
        row = df.iloc[i].astype(str).tolist()
        for idx, val in enumerate(row):
            if '序号' in val or 'No' in val or 'ID' in val:
                col_serial = idx
            if '队伍名称' in val or 'Team' in val:
                col_name = idx
        
        if col_serial != -1 and col_name != -1:
            start_row = i + 1
            print(f"Header found at row {i}, Serial col: {col_serial}, Name col: {col_name}")
            break
            
    # Look for Team 42
    found = False
    for i in range(start_row, len(df)):
        row = df.iloc[i]
        serial = str(row.iloc[col_serial]).strip()
        if serial.endswith('.0'): serial = serial[:-2]
        
        if serial == '42':
            found = True
            name_val = row.iloc[col_name]
            print(f"Found Team 42 at row {i}:")
            print(f"  Raw Name Value: {repr(name_val)}")
            print(f"  Is Null/NaN: {pd.isna(name_val)}")
            break
            
    if not found:
        print("Team 42 not found.")

    # Also try openpyxl to check for images (images are stored in the sheet object, not cells)
    print("\nChecking for images with openpyxl...")
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    print(f"  Images count: {len(ws._images)}")
    for img in ws._images:
        print(f"  Image found at anchor: {img.anchor}")
        # Note: anchor usually gives top-left cell
        
except Exception as e:
    print(f"Error: {e}")
