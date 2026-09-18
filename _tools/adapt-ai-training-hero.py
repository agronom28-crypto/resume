from pathlib import Path

path = Path('ai-training.html')
html = path.read_text(encoding='utf-8')
marker = '/* Hero reference layout */'
if marker in html:
    raise SystemExit('Hero reference layout already exists')

css = r'''
/* Hero reference layout */
@media (min-width:1200px){
  .hero{min-height:calc(100svh - 84px);display:flex;align-items:flex-start;padding:28px 0 72px}
  .hero>.wrap{width:min(1648px,calc(100% - 64px))}
  .hero-grid{grid-template-columns:minmax(0,1.04fr) minmax(520px,.96fr);gap:clamp(72px,5vw,110px);align-items:start}
  .hero .tag{margin-top:0;padding:9px 15px;font-size:13px}
  .hero h1{max-width:760px;margin:38px 0 64px;font-size:clamp(64px,4.4vw,86px);line-height:.99;letter-spacing:-.045em}
  .hero .lead{max-width:820px;font-size:clamp(19px,1.3vw,25px);line-height:1.55}
  .hero .actions{margin-top:40px;gap:18px}
  .hero .btn{min-height:72px;padding:0 40px;font-size:18px;border-radius:14px}
  .hero-visual{width:100%;margin-bottom:155px}
  .hero-visual img{width:100%;aspect-ratio:700/810;object-fit:cover;border-radius:56px 56px 0 0}
  .result{bottom:-155px;min-height:156px;padding:26px 28px;border-radius:0 0 28px 28px;display:flex;flex-direction:column;justify-content:center}
  .result small{font-size:14px;letter-spacing:.02em;text-transform:uppercase}
  .result strong{max-width:620px;margin-top:14px;font-size:24px;line-height:1.35}
}
@media (min-width:1200px) and (max-height:820px){
  .hero h1{margin:28px 0 38px;font-size:clamp(58px,4vw,72px)}
  .hero .lead{font-size:19px}
  .hero .btn{min-height:60px}
  .hero-visual img{max-height:620px}
  .result{bottom:-130px;min-height:132px}
  .hero-visual{margin-bottom:130px}
}
'''
html = html.replace('</style>', css + '</style>', 1)
path.write_text(html, encoding='utf-8')
