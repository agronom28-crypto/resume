from pathlib import Path

path = Path('ai-training.html')
html = path.read_text(encoding='utf-8')
old = '.final img{width:360px;aspect-ratio:1;object-fit:cover;border-radius:50%}'
new = '.final img{width:360px;max-width:100%;height:auto;object-fit:contain;border-radius:0}'
if old not in html:
    raise SystemExit('Final image style was not found')
html = html.replace(old, new, 1)
css = '.dark .btn:not(.primary){color:#101828;background:#fff}'
html = html.replace('</style>', css + '</style>', 1)
path.write_text(html, encoding='utf-8')
