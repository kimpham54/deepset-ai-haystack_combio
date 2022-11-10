from pathlib import Path

path = Path('/Users/kpham/Desktop/coding-kim/haystack/combio_clean/singletxt/')

for f in path.iterdir():
    f.rename(f.with_suffix('.txt'))