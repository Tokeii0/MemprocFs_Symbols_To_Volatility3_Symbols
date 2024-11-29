# MemprocFs_Symbols_To_Volatility3_Symbols

A tool for converting Windows PDB files used by MemProcfs to Volatility3 symbol files (.json.xz).

## Prerequisites

1. Python 3.6+
2. Volatility3 framework
3. Windows PDB files ready for conversion

## Directory Structure

```
your_work_directory/
├── convert_pdbs_mt.py          # This conversion tool
├── volatility3/                # Volatility3 framework directory
├── Symbols_memprocfs/          # Source PDB files directory
│   └── *.pdb                   # PDB files
└── Symbols_vol3/              # Output directory (auto-created)
    └── *.pdb/                 # Symbol files directory
        └── *.json.xz          # Converted symbol files
```

## Usage

1. Place the script in the same directory level as the volatility3 directory
2. Ensure Symbols_memprocfs directory contains the PDB files to be converted
3. Run the script:
```bash
python convert_pdbs_mt.py
```

## Output Example

Converted files will be saved in the following structure:
```
Symbols_vol3/
└── ntdll.pdb/
    └── 0ADF62812708CFE13125A0E82555162A-1.json.xz
```

## Custom Configuration

To adjust the number of threads, modify the following part in the script:
```python
max_workers = 20  # Set to your desired number of threads
```

## Notes

1. Ensure sufficient disk space for converted files
2. Conversion process may take time depending on the number and size of PDB files
3. Recommended to run on a high-performance machine to take advantage of multi-threading

## Error Handling

- Script automatically captures and displays errors during processing
- Failure of single file conversion won't affect other files
- Final statistics show successful and failed conversions
