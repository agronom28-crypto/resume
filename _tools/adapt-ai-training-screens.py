from pathlib import Path

path = Path('ai-training.html')
html = path.read_text(encoding='utf-8')
if 'id="responsive-screen-adapter"' in html:
    raise SystemExit('Responsive adapter already exists')

css = r'''
<style id="responsive-screen-adapter">
/* Responsive layer: desktop layout remains unchanged. */
html,body{max-width:100%;overflow-x:hidden}
img,svg,video{max-width:100%;height:auto}
button,a,[role="button"],[role="link"]{touch-action:manipulation}

@media (max-width:1100px){
  .container{width:min(100% - 48px,var(--container,1160px))!important}
  .header__row{gap:16px!important}
  .brand{min-width:0!important}
  .nav{gap:16px!important}
  .hero__grid,.hero-grid,.audience,.final,.final__grid{gap:44px!important}
  .grid-4{grid-template-columns:repeat(2,minmax(0,1fr))!important}
  .steps{grid-template-columns:repeat(3,minmax(0,1fr))!important}
  .step::after{display:none!important}
  .pricing,.price-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}
  .price--featured{grid-column:span 2}
}

@media (max-width:820px){
  html{scroll-padding-top:76px!important}
  .header__row{min-height:72px!important}
  .nav{display:none!important}
  .header__row>.btn,.header__row>.button{margin-left:auto!important}
  .hero__grid,.hero-grid,.audience,.final,.final__grid,.lead-card,.compare,.modules,.cases,.case-grid{grid-template-columns:minmax(0,1fr)!important}
  .hero__copy{padding-top:20px!important}
  .hero__visual{width:min(100%,560px)!important;margin-inline:auto!important}
  .result-card{position:static!important;margin-top:16px!important}
  .compare__col+.compare__col{border-left:0!important;border-top:1px solid var(--line,#dde2ea)!important}
  .modules,.cases,.case-grid{gap:20px!important}
  .pricing,.price-grid{grid-template-columns:minmax(0,1fr)!important}
  .price--featured{grid-column:auto!important}
  .price{min-height:0!important}
  .steps{grid-template-columns:repeat(2,minmax(0,1fr))!important}
  .lead-card{gap:32px!important}
  .cover{width:min(100%,360px)!important}
  .final img,.final__image{width:min(100%,360px)!important;height:auto!important;aspect-ratio:1;object-fit:cover}
}

@media (max-width:560px){
  :root{--mobile-gutter:16px}
  .container{width:calc(100% - 32px)!important;padding-inline:0!important}
  .section{padding-block:52px!important}
  .section--compact{padding-block:40px!important}
  .header__row{min-height:64px!important}
  .brand__mark{width:40px!important;height:40px!important}
  .brand__role{display:none!important}
  .header__row>.btn,.header__row>.button{min-width:0!important;min-height:44px!important;padding-inline:12px!important;font-size:12px!important;white-space:nowrap}
  h1{font-size:clamp(36px,11vw,44px)!important;line-height:1.04!important;overflow-wrap:anywhere}
  h2{font-size:clamp(30px,9vw,38px)!important;line-height:1.08!important;overflow-wrap:anywhere}
  h3{overflow-wrap:anywhere}
  .lead{font-size:16px!important}
  .hero{padding-top:18px!important;padding-bottom:58px!important}
  .hero__grid,.hero-grid{gap:28px!important}
  .actions{display:grid!important;grid-template-columns:1fr!important;width:100%!important}
  .actions .btn,.actions .button,.btn--wide{width:100%!important;min-width:0!important}
  .proof__grid{grid-template-columns:1fr!important}
  .proof__item{border-right:0!important;border-bottom:1px solid #344054!important}
  .proof__item:last-child{border-bottom:0!important}
  .grid-4,.steps,.modules,.cases,.case-grid,.pricing,.price-grid{grid-template-columns:minmax(0,1fr)!important}
  .card,.module,.case,.price{min-width:0!important}
  .audience{gap:32px!important}
  .roles li{grid-template-columns:36px minmax(0,1fr)!important}
  .artifact{grid-template-columns:1fr!important;gap:8px!important}
  .lead-card{padding:22px!important}
  .lead-card h2{font-size:30px!important}
  .cover{min-height:260px!important}
  .faq summary{min-height:72px!important;gap:16px!important}
  .faq p{font-size:14px!important}
  .final{gap:34px!important}
  table{display:block;max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}
}

@media (max-width:390px){
  .container{width:calc(100% - 24px)!important}
  .brand__name{font-size:13px!important}
  .header__row>.btn,.header__row>.button{padding-inline:10px!important;font-size:11px!important}
  h1{font-size:34px!important}
  h2{font-size:29px!important}
  .card,.module,.case,.price,.lead-card{padding:18px!important}
}

@media (hover:none){
  .btn:hover,.button:hover,.card:hover,.case:hover{transform:none!important}
}

@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{scroll-behavior:auto!important;animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
}
</style>
'''

if '</head>' not in html:
    raise SystemExit('Closing head tag not found')
html = html.replace('</head>', css + '\n</head>', 1)
path.write_text(html, encoding='utf-8')
print('Responsive screen adapter added')
