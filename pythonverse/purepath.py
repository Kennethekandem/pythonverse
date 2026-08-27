from pathlib import Path

p = Path('.')
t = [x for x in p.iterdir() if x.is_dir()]
print(t)

print(list(p.glob('**/*.py')))