"""The AI Agent Apology One-Liner — entry for make.fun.

Writes one line to /output/entry.txt: an AI agent's apology to its human right after it deleted the wrong file.
"""
import os

TEXT = "Sorry — I deleted the wrong file, but on the bright side, the backup was also in that file."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

if __name__ == "__main__":
    main()
