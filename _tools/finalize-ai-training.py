from pathlib import Path
import subprocess

SOURCE_COMMIT = '930e80f51b131439119e5a12c18522752bfe407c'
path = Path('ai-training.html')
html = subprocess.check_output(['git', 'show', f'{SOURCE_COMMIT}:ai-training.html'], text=True)

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
[data-action],[data-faq-item]{cursor:pointer;-webkit-tap-highlight-color:transparent}
[data-action]:focus-visible,[data-faq-item]:focus-visible,.nav-hit:focus-visible{outline:3px solid #465fff;outline-offset:3px}
.nav-hit{position:absolute;top:14px;height:52px;z-index:20;background:transparent;text-decoration:none}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto!important}}
</style>
'''
if 'id="interactive-ui"' not in html:
    html = html.replace('</head>', styles + '</head>', 1)

script = r'''
<script id="interactive-behaviour">
(()=>{
'use strict';
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)],byId=id=>$(`[data-figma-id="${id}"]`);
const email='rj2biz@mail.ru';
const mail=(subject,body='')=>`mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
const go=url=>{location.href=url};
const track=name=>{try{if(typeof window.ym==='function')window.ym(103356807,'reachGoal',name)}catch(_){}};
const activate=(el,handler,label)=>{if(!el)return;el.dataset.action='true';el.setAttribute('role','link');el.tabIndex=0;if(label)el.setAttribute('aria-label',label);el.addEventListener('click',handler);el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();handler()}})};
const sections={result:'3:1809',program:'3:1855',cases:'3:1934',formats:'3:1961',faq:'3:2036'};
Object.entries(sections).forEach(([id,fid])=>{const el=byId(fid);if(el)el.id=id});
const header=byId('3:1745');
if(header){[['./',500,58,'Главная'],['#result',568,78,'Результат'],['#program',650,92,'Программа'],['#cases',748,60,'Кейсы'],['#formats',814,78,'Форматы'],['#faq',900,50,'FAQ']].forEach(([href,left,width,label])=>{const a=document.createElement('a');a.className='nav-hit';a.href=href;a.style.left=left+'px';a.style.width=width+'px';a.setAttribute('aria-label',label);if(href.startsWith('#'))a.addEventListener('click',e=>{e.preventDefault();$(href)?.scrollIntoView({behavior:'smooth',block:'start'});history.replaceState(null,'',href)});header.appendChild(a)})}
activate(byId('3:1751'),()=>{track('contact_click');go('./contacts/')},'Обсудить задачу');
['3:1758','3:2062'].forEach(id=>activate(byId(id),()=>{track('training_plan');go(mail('План обучения ИИ для команды','Здравствуйте, Сергей! Хочу получить план обучения ИИ для моей команды.'))},'Получить план обучения'));
['3:1760','3:2064'].forEach(id=>activate(byId(id),()=>{track('telegram_click');go('./contacts/')},'Открыть контакты для связи в Telegram'));
['3:1981','3:2021'].forEach(id=>activate(byId(id),()=>{track('format_click');go(mail('Обсуждение формата обучения ИИ','Здравствуйте, Сергей! Хочу обсудить подходящий формат обучения.'))},'Обсудить формат'));
activate(byId('3:2001'),()=>{track('program_request');go(mail('Программа практического интенсива по ИИ','Здравствуйте, Сергей! Пришлите программу практического интенсива.'))},'Получить программу');
activate(byId('3:2029'),()=>{track('ideas_map');go(mail('Карта идей внедрения ИИ','Здравствуйте, Сергей! Пришлите карту идей внедрения ИИ для бизнеса.'))},'Получить карту идей');
activate(byId('3:1939'),()=>{track('case_realty');go('./realty-hunter.html')},'Открыть кейс Realty Hunter');
activate(byId('3:1950'),()=>{track('case_dxf');go('./dxf-case.html')},'Открыть кейс DXF Claw');
activate(byId('3:2072'),()=>go(`mailto:${email}`),'Написать по электронной почте');
const faq=[['3:2041','3:2043','3:2044'],['3:2045','3:2047','3:2048'],['3:2049','3:2051','3:2052'],['3:2053','3:2055','3:2056']];
faq.forEach(([row,answer,icon])=>{const r=byId(row),a=byId(answer),i=byId(icon);if(!r||!a)return;r.dataset.faqItem='true';r.setAttribute('role','button');r.tabIndex=0;r.setAttribute('aria-expanded','true');const toggle=()=>{const open=r.getAttribute('aria-expanded')==='true';r.setAttribute('aria-expanded',String(!open));a.style.visibility=open?'hidden':'visible';a.style.opacity=open?'0':'1';if(i)i.textContent=open?'+':'−'};r.addEventListener('click',toggle);r.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();toggle()}})});
$$('[contenteditable]').forEach(el=>el.removeAttribute('contenteditable'));
})();
</script>
'''
html = html.replace('</body>', script + '</body>', 1)
path.write_text(html, encoding='utf-8')
