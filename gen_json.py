from pathlib import Path

# config
host     = 'https://diewcoftza.github.io/tundermeme'
img_exts = { '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp' }
img_dir  = Path('./docs')

# scan image files
img_files = [
    f.name for f in img_dir.iterdir()
    if f.is_file() and f.suffix.lower() in img_exts
]
img_files.sort()

# craft json
print('[')
for f in img_files:
    if f == img_files[-1]: # last
        print('  "{}/{}"'.format(host, f))
    else:
        print('  "{}/{}",'.format(host, f))
print(']')
