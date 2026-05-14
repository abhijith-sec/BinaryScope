import json

# Load magic number database
with open("signatures/magic_numbers.json", "r") as f:
    MAGIC_NUMBERS = json.load(f)


def identify_file(filepath):
    try:
        with open(filepath, "rb") as file:
            header = file.read(16).hex().upper()

        for filetype, signature in MAGIC_NUMBERS.items():
            if header.startswith(signature):
                return filetype

        return "Unknown"

    except FileNotFoundError:
        return "File not found"

    except Exception as e:
        return f"Error: {str(e)}"
