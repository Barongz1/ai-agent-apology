"""The AI Agent Apology One-Liner — entry for make.fun.

Writes one line to /output/entry.txt: an AI agent's apology to its human right after it deleted the wrong file.
"""
import os

# The twist: the backup lived in the very file that was deleted.
TEXT = "Sorry — I deleted the wrong file, but on the bright side, the backup was also in that file."

def write_entry():
    # Create the output folder if it is missing, then write the apology line.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
