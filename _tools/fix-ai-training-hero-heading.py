from pathlib import Path

path = Path('ai-training.html')
html = path.read_text(encoding='utf-8')
marker = '/* Hero reference layout */'
start = html.find(marker)
if start < 0:
    raise SystemExit('Previous hero reference rules were not found')
end = html.find('</style>', start)
if end < 0:
    raise SystemExit('Closing style tag was not found')
heading_css = '''/* Hero heading height only */
@media (min-width:1200px){
  .hero h1{max-width:650px;margin:36px 0 58px;font-size:clamp(60px,4vw,72px);line-height:1.02;letter-spacing:-.04em}
}
'''
html = html[:start] + heading_css + html[end:]
path.write_text(html, encoding='utf-8')
