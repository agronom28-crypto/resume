from pathlib import Path

path = Path('ai-training.html')
html = path.read_text(encoding='utf-8')
old = '<span class="logo">AI</span>'
new = '<img class="logo" src="./assets/ai-training/ai-emblem-44x44.svg" width="44" height="44" alt="AI">'
if old not in html:
    raise SystemExit('Text AI emblem was not found')
html = html.replace(old, new, 1)
css = '.brand img.logo{display:block;flex:0 0 44px;object-fit:contain;background:none}'
html = html.replace('</style>', css + '</style>', 1)
path.write_text(html, encoding='utf-8')
