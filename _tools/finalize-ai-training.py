from pathlib import Path
import re
from urllib.parse import quote

path = Path('ai-training.html')
html = path.read_text(encoding='utf-8')

# Remove Figma editing artifacts.
html = re.sub(r'\scontenteditable="true"', '', html)
html = re.sub(r'\sspellcheck="false"', '', html)

# Replace embedded images with repository assets to reduce page weight.
assets = {
    '20:2428': './newphoto.png',
    '25:2471': './newphoto.png',
    '25:2474': './newphoto.png',
    '26:2480': './Обложка DFX claw.png',
    '26:2477': './hero-realty-hunter.png',
}
for figma_id, src in assets.items():
    pattern = rf'(<img[^>]*data-figma-id="{re.escape(figma_id)}"[^>]*\ssrc=")[^"]*(")'
    html = re.sub(pattern, rf'\1{src}\2', html, count=1)

# Production metadata.
html = re.sub(r'<title>.*?</title>', '<title>Обучение ИИ для бизнеса и команд — Сергей Николаенко</title>', html, count=1, flags=re.S)
meta = '''
<meta name="description" content="Практическое обучение ИИ для собственников и команд на реальных бизнес-процессах: сценарии, промты, регламент и первый пилот.">
<link rel="canonical" href="https://agronom28-crypto.github.io/resume/ai-training.html">
<meta property="og:type" content="website">
<meta property="og:title" content="Обучение ИИ для бизнеса и команд">
<meta property="og:description" content="Практическое обучение на ваших процессах с готовыми сценариями и регламентом.">
<meta property="og:url" content="https://agronom28-crypto.github.io/resume/ai-training.html">
'''
if 'rel="canonical"' not in html:
    html = html.replace('</title>', '</title>' + meta, 1)

styles = '''
<style id="interactive-ui">
[data-action],[data-nav-link],[data-case-link],[data-faq-item]{cursor:pointer;-webkit-tap-highlight-color:transparent}
[data-action],[data-case-link]{transition:transform .18s ease,box-shadow .18s ease,filter .18s ease}
[data-action]:hover,[data-case-link]:hover{filter:brightness(.98);box-shadow:0 14px 34px rgba(13,20,38,.14)!important}
[data-action]:active,[data-case-link]:active{transform:translateY(1px)}
[data-action]:focus-visible,[data-nav-link]:focus-visible,[data-case-link]:focus-visible,[data-faq-item]:focus-visible{outline:3px solid #465fff;outline-offset:4px}
.site-nav-links{display:flex!important;align-items:center;justify-content:center;gap:28px;height:44px!important;transform:matrix(1,0,0,1,505,20)!important;white-space:nowrap!important}
.site-nav-links a{color:#344054;text-decoration:none;font:500 13px/44px 'Inter',sans-serif}
.site-nav-links a:hover{color:#465fff}
[data-faq-answer]{transition:opacity .18s ease,visibility .18s ease}
[data-faq-item][aria-expanded="false"] [data-faq-answer]{opacity:0;visibility:hidden}
[data-faq-item][aria-expanded="true"] [data-faq-answer]{opacity:1;visibility:visible}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto!important}[data-action],[data-case-link],[data-faq-answer]{transition:none!important}}
</style>
'''
if 'id="interactive-ui"' not in html:
    html = html.replace('</head>', styles + '</head>', 1)

script = r'''
<script id="interactive-behaviour">
(()=>{
'use strict';
const $=s=>document.querySelector(s);
const $$=s=>[...document.querySelectorAll(s)];
const byId=id=>$(`[data-figma-id="${id}"]`);
const email='rj2biz@mail.ru';
const mail=(subject,body='')=>`mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
const open=(url,newTab=false)=>{if(newTab){window.open(url,'_blank','noopener,noreferrer')}else{window.location.href=url}};
const track=name=>{try{if(typeof window.ym==='function'){window.ym(103356807,'reachGoal',name)}}catch(_){}};
const activate=(el,handler,label)=>{
 if(!el)return;
 el.dataset.action='true'; el.setAttribute('role','link'); el.setAttribute('tabindex','0');
 if(label)el.setAttribute('aria-label',label);
 el.addEventListener('click',e=>{if(e.target.closest('a'))return;handler(e)});
 el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();handler(e)}});
};
const sectionIds={result:'3:1809',program:'3:1855',cases:'3:1934',formats:'3:1961',faq:'3:2036'};
Object.entries(sectionIds).forEach(([id,figma])=>{const el=byId(figma);if(el)el.id=id});
const nav=byId('3:1750');
if(nav){nav.classList.add('site-nav-links');nav.innerHTML=`<a href="./">Главная</a><a href="#result">Результат</a><a href="#program">Программа</a><a href="#cases">Кейсы</a><a href="#formats">Форматы</a><a href="#faq">FAQ</a>`;nav.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();document.querySelector(a.getAttribute('href'))?.scrollIntoView({behavior:'smooth',block:'start'});history.replaceState(null,'',a.getAttribute('href'))}))}
const contact=()=>{track('contact_click');open('./contacts/')};
const telegram=()=>{track('telegram_click');open('./contacts/')};
['3:1751'].forEach(id=>activate(byId(id),contact,'Обсудить задачу'));
['3:1758','3:2062'].forEach(id=>activate(byId(id),()=>{track('training_plan');open(mail('План обучения ИИ для команды','Здравствуйте, Сергей! Хочу получить план обучения ИИ для моей команды.'))},'Получить план обучения'));
['3:1760','3:2064'].forEach(id=>activate(byId(id),telegram,'Открыть контакты для связи в Telegram'));
['3:1981','3:2021'].forEach(id=>activate(byId(id),()=>{track('format_click');open(mail('Обсуждение формата обучения ИИ','Здравствуйте, Сергей! Хочу обсудить подходящий формат обучения.'))},'Обсудить формат'));
activate(byId('3:2001'),()=>{track('program_request');open(mail('Программа практического интенсива по ИИ','Здравствуйте, Сергей! Пришлите, пожалуйста, программу практического интенсива.'))},'Получить программу');
activate(byId('3:2029'),()=>{track('ideas_map');open(mail('Карта идей внедрения ИИ','Здравствуйте, Сергей! Пришлите, пожалуйста, карту идей внедрения ИИ для бизнеса.'))},'Получить карту идей');
activate(byId('3:1939'),()=>{track('case_realty');open('./realty-hunter.html')},'Открыть кейс Realty Hunter');
activate(byId('3:1950'),()=>{track('case_dxf');open('./dxf-case.html')},'Открыть кейс DXF Claw');
const footer=byId('3:2072');activate(footer,()=>open(`mailto:${email}`),'Написать Сергею Николаенко по электронной почте');
const faq=[['3:2041','3:2043','3:2044'],['3:2045','3:2047','3:2048'],['3:2049','3:2051','3:2052'],['3:2053','3:2055','3:2056']];
faq.forEach(([row,answer,icon],index)=>{const r=byId(row),a=byId(answer),i=byId(icon);if(!r||!a)return;r.dataset.faqItem='true';a.dataset.faqAnswer='true';r.setAttribute('role','button');r.setAttribute('tabindex','0');r.setAttribute('aria-expanded',index===0?'true':'false');const toggle=()=>{const next=r.getAttribute('aria-expanded')!=='true';r.setAttribute('aria-expanded',String(next));if(i)i.textContent=next?'−':'+'};r.addEventListener('click',toggle);r.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();toggle()}});if(i)i.textContent=index===0?'−':'+'});
$$('[contenteditable]').forEach(el=>el.removeAttribute('contenteditable'));
$$('img').forEach(img=>{img.decoding='async';if(!img.closest('[data-figma-id="3:1753"]'))img.loading='lazy'});
})();
</script>
'''
if 'id="interactive-behaviour"' not in html:
    html = html.replace('</body>', script + '</body>', 1)

path.write_text(html, encoding='utf-8')
print(f'Updated {path}: {len(html)} characters')
