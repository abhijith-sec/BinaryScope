# BinaryScope

BinaryScope is a Python-based digital forensics and file analysis tool designed to identify file types using magic number signatures, detect extension mismatches, and generate cryptographic hashes for integrity verification.

The project was developed to explore fundamental concepts used in digital forensics, malware analysis, and incident response workflows.

---

## Overview

File extensions can be easily modified to disguise a file's true nature. Attackers often rename malicious executables to appear as harmless documents or images.

BinaryScope addresses this problem by analyzing a file's magic number (file signature) and comparing it with the file extension provided by the operating system.

The tool helps analysts verify file authenticity and identify potentially suspicious files during forensic investigations.

---

## Features

* Magic number-based file type detection
* File extension verification
* Extension mismatch detection
* SHA-256 hash generation
* Command-line interface
* Lightweight and easy to use
* Cross-platform Python implementation

---

## How It Works

1. The tool reads the target file in binary mode.
2. It extracts the file signature (magic number).
3. The signature is compared against a known signature database.
4. The detected file type is compared with the file extension.
5. A SHA-256 hash is calculated for integrity verification.
6. Results are displayed in a structured format.

---

## Example Usage

```bash
python src/cli.py <file_path>
```

Example:

```bash
python src/cli.py samples/test.pdf
```

---

## Sample Output

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

---

## Concepts Applied

This project demonstrates practical implementation of several cybersecurity and computer science concepts:

### Digital Forensics

* File signature analysis
* Evidence validation
* File identification techniques

### Malware Analysis Fundamentals

* Detection of disguised files
* Extension spoofing identification
* Binary file inspection

### Cryptography

* SHA-256 hashing
* File integrity verification
* Hash-based identification

### Python Development

* File handling
* Binary data processing
* Modular project structure
* Command-line application development

### Security Operations

* Basic threat triage
* Initial file assessment
* Artifact analysis

---

## Technologies Used

* Python 3
* hashlib
* argparse
* File signature analysis techniques

---

## Project Structure

```text
BinaryScope/
│
├── src/
│   ├── cli.py
│   ├── detector.py
│   ├── hasher.py
│
├── signatures/
│   └── signatures.json
│
├── samples/
│   └── test.pdf
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Learning Outcomes

Through the development of BinaryScope, I gained hands-on experience with:

* Digital forensics fundamentals
* Magic number identification
* Cryptographic hashing algorithms
* Binary file analysis
* Secure software development practices
* Python-based security tool development

---

## Future Enhancements

* Support for additional hashing algorithms (MD5, SHA1)
* Recursive directory scanning
* JSON and HTML report generation
* YARA rule integration
* PE and ELF file analysis
* VirusTotal API integration
* Batch file processing

---

## Author

Abhijith

Cybersecurity Student | Security Enthusiast | Certified Ethical Hacker (CEH) | Aspiring Security Analyst

GitHub: https://github.com/abhijith-sec

---

## Disclaimer

This tool was developed for educational, research, and defensive cybersecurity purposes only.
