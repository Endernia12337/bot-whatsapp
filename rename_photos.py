from pathlib import Path

folder = Path("photos")
arquives = [f for f in folder.iterdir()
            if f.is_file()]

for arquive in arquives:
    index = int(str(arquives.index(arquive)).zfill(3))
    arquive.rename(f'{folder}/photo_{index + 1}{arquive.suffix}')

