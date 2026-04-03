from pathlib import Path

folder = Path("photos")
arquives = [f for f in folder.iterdir()
            if f.is_file()]

for arquive in arquives:
    arquive.rename(f'{folder}/photo_{arquives.index(arquive) + 1}{arquive.suffix}')