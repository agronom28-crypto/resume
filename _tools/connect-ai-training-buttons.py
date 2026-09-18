from pathlib import Path

path = Path('ai-training.html')
html = path.read_text(encoding='utf-8')
marker = 'id="ai-training-controls"'
if marker in html:
    raise SystemExit('Controls already connected')

script = r'''
<script id="ai-training-controls">
(()=>{
'use strict';
const email='rj2biz@mail.ru';
const contactUrl='./contacts/';
const norm=value=>(value||'').replace(/\s+/g,' ').trim();
const mail=(subject,body)=>`mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body||'')}`;
const track=name=>{try{if(typeof window.ym==='function')window.ym(103356807,'reachGoal',name)}catch(_){}};
const sections=[
 ['result',['Сначала процесс. Потом инструмент.','Готовая система для ежедневной работы']],
 ['program',['Шесть модулей от аудита до внедрения']],
 ['cases',['Показываю решения на собственных продуктах']],
 ['formats',['Выберите глубину внедрения']],
 ['faq',['Перед началом']]
];
for(const [id,needles] of sections){
 const section=[...document.querySelectorAll('section')].find(el=>needles.some(n=>norm(el.textContent).includes(n)));
 if(section&&!document.getElementById(id))section.id=id;
}
const destination=(text,el)=>{
 if(text==='Главная')return {url:'./',goal:'nav_home'};
 if(text==='Результат')return {url:'#result',goal:'nav_result'};
 if(text==='Программа')return {url:'#program',goal:'nav_program'};
 if(text==='Кейсы')return {url:'#cases',goal:'nav_cases'};
 if(text==='Форматы')return {url:'#formats',goal:'nav_formats'};
 if(text==='FAQ')return {url:'#faq',goal:'nav_faq'};
 if(text.includes('Обсудить задачу'))return {url:contactUrl,goal:'contact_click'};
 if(text.includes('Написать в Telegram'))return {url:contactUrl,goal:'telegram_click'};
 if(text.includes('Получить план обучения'))return {url:mail('План обучения ИИ для команды','Здравствуйте, Сергей! Хочу получить план обучения ИИ для моей команды.'),goal:'training_plan'};
 if(text.includes('Получить программу'))return {url:mail('Программа практического интенсива по ИИ','Здравствуйте, Сергей! Пришлите, пожалуйста, программу практического интенсива.'),goal:'program_request'};
 if(text.includes('Получить карту идей'))return {url:mail('Карта идей внедрения ИИ','Здравствуйте, Сергей! Пришлите, пожалуйста, карту идей внедрения ИИ для бизнеса.'),goal:'ideas_map'};
 if(text.includes('Обсудить формат')){
   const card=el.closest('article,.price,.pricing-card,.card')||el.parentElement;
   const context=norm(card?.textContent);
   const subject=context.includes('Корпоративное')?'Корпоративное внедрение ИИ':context.includes('Диагностика')?'Диагностика ИИ-процесса':'Обсуждение формата обучения ИИ';
   return {url:mail(subject,'Здравствуйте, Сергей! Хочу обсудить подходящий формат работы.'),goal:'format_click'};
 }
 if(text.includes('Открыть кейс')){
   const card=el.closest('article,.case,.card')||el.parentElement;
   const context=norm(card?.textContent);
   if(context.includes('Realty Hunter'))return {url:'./realty-hunter.html',goal:'case_realty'};
   if(context.includes('DXF Claw'))return {url:'./dxf-case.html',goal:'case_dxf'};
 }
 return null;
};
const candidates=[...new Set([
 ...document.querySelectorAll('a,button,[role="button"],.btn,.button,[class*="button"],[data-figma-name]')
])];
for(const el of candidates){
 const label=norm(el.getAttribute('aria-label')||el.getAttribute('data-figma-name')||el.textContent);
 const action=destination(label,el);
 if(!action)continue;
 el.style.cursor='pointer';
 if(el.tagName==='A'){
   el.setAttribute('href',action.url);
   el.addEventListener('click',event=>{
     track(action.goal);
     if(action.url.startsWith('#')){
       const target=document.querySelector(action.url);
       if(target){event.preventDefault();target.scrollIntoView({behavior:'smooth',block:'start'});history.replaceState(null,'',action.url)}
     }
   });
 }else{
   if(!el.hasAttribute('tabindex'))el.tabIndex=0;
   if(!el.hasAttribute('role'))el.setAttribute('role','link');
   const run=()=>{track(action.goal);if(action.url.startsWith('#')){document.querySelector(action.url)?.scrollIntoView({behavior:'smooth',block:'start'});history.replaceState(null,'',action.url)}else location.href=action.url};
   el.addEventListener('click',event=>{if(event.target.closest('a'))return;run()});
   el.addEventListener('keydown',event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();run()}});
 }
}
for(const el of document.querySelectorAll('a[href=""],a[href="#"]')){
 const action=destination(norm(el.textContent),el);
 if(action)el.href=action.url;
}
})();
</script>
'''

if '</body>' not in html:
    raise SystemExit('Closing body tag not found')
html = html.replace('</body>', script + '\n</body>', 1)
path.write_text(html, encoding='utf-8')
print('Connected AI training controls')
