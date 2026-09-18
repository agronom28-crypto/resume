from pathlib import Path
import re

path = Path('ai-training.html')
html = path.read_text(encoding='utf-8')

pattern = r'<div class="cover">.*?</div>'
replacement = '<img class="lead-cover" src="./assets/ai-training/ai-business-ideas-cover-292x292.svg" width="292" height="292" loading="lazy" alt="Карта идей внедрения ИИ для бизнеса">'
html, count = re.subn(pattern, replacement, html, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'Expected one cover block, replaced {count}')

css = '.lead-cover{display:block;width:292px;max-width:100%;height:auto;justify-self:end;border-radius:28px;box-shadow:0 18px 40px #17255424}@media(max-width:1000px){.lead-cover{justify-self:start}}'
html = html.replace('</style>', css + '</style>', 1)
path.write_text(html, encoding='utf-8')
