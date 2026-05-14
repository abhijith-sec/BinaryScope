## Usage

### Scan a File

```bash
python src/cli.py <file_path>
```

Example:

```bash
python src/cli.py samples/test.pdf
```

### Example Output

```text
===================================
         BinaryScope
===================================

[+] File            : samples/test.pdf
[+] Detected Type   : PDF
[+] Extension       : .pdf
[+] SHA256 Hash     : 8f2c3f...

===================================
```

## Features

- Magic number file detection
- Extension mismatch detection
- SHA256 hashing
- CLI-based forensic analysis
