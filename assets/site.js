(function(){
  var burger=document.querySelector('.burger');
  var mm=document.querySelector('.mobile-menu');
  if(burger&&mm){burger.addEventListener('click',function(){mm.classList.toggle('open');});}
  function ym(id){ if(window.ym){ try{ window.ym(window.YM_COUNTER_ID,'reachGoal',id); }catch(e){} } }
  window.trackEvent=ym;
  document.querySelectorAll('a[href^="https://t.me/"]').forEach(function(a){a.addEventListener('click',function(){ym('telegram_click');});});
  document.querySelectorAll('a[href^="tel:"]').forEach(function(a){a.addEventListener('click',function(){ym('phone_click');});});
  document.querySelectorAll('a[href^="mailto:"]').forEach(function(a){a.addEventListener('click',function(){ym('email_click');});});
  document.querySelectorAll('a[data-track="service"]').forEach(function(a){a.addEventListener('click',function(){ym('service_view');});});
  document.querySelectorAll('a[data-track="case"]').forEach(function(a){a.addEventListener('click',function(){ym('case_view');});});
  var priceEl=document.querySelector('[data-track="price"]');
  if(priceEl && 'IntersectionObserver' in window){
    var seen=false;
    var io=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting&&!seen){seen=true;ym('price_view');}});},{threshold:0.4});
    io.observe(priceEl);
  }
  function getUTM(){
    var params=new URLSearchParams(window.location.search);
    var keys=['utm_source','utm_medium','utm_campaign','utm_content','utm_term'];
    var stored=JSON.parse(sessionStorage.getItem('utm_data')||'{}');
    var found=false;
    keys.forEach(function(k){if(params.get(k)){stored[k]=params.get(k);found=true;}});
    if(found){sessionStorage.setItem('utm_data',JSON.stringify(stored));}
    if(!sessionStorage.getItem('landing_page')){sessionStorage.setItem('landing_page',window.location.pathname);}
    return stored;
  }
  var utm=getUTM();
  document.querySelectorAll('form.lead-form').forEach(function(form){
    var started=false;
    form.addEventListener('focusin',function(){if(!started){started=true;ym('form_start');}});
    Object.keys(utm).forEach(function(k){var inp=form.querySelector('input[name="'+k+'"]');if(inp)inp.value=utm[k];});
    var lp=form.querySelector('input[name="landing_page"]');
    if(lp)lp.value=sessionStorage.getItem('landing_page')||window.location.pathname;
    var src=form.querySelector('input[name="source_page"]');
    if(src)src.value=window.location.href;
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var hp=form.querySelector('.hp-field input');
      if(hp&&hp.value){return;}
      ym('form_submit');
      var status=form.querySelector('.form-status');
      var data=new FormData(form);
      var name=data.get('name')||'';
      var task=data.get('task')||'';
      var contact=data.get('contact')||'';
      var budget=data.get('budget')||'';
      var deadline=data.get('deadline')||'';
      var endpoint=form.getAttribute('data-endpoint');
      if(endpoint){
        fetch(endpoint,{method:'POST',body:data}).then(function(r){if(!r.ok)throw new Error('bad');return r.json();}).then(function(){
          ym('form_success');
          if(status){status.textContent='Заявка отправлена. Отвечу в Telegram или почте в течение рабочего дня.';status.style.color='var(--p)';}
          form.reset();
        }).catch(function(){ym('form_error');fallbackToTelegram(name,task,contact,budget,deadline,status);});
      } else {
        fallbackToTelegram(name,task,contact,budget,deadline,status);
      }
    });
  });
  function fallbackToTelegram(name,task,contact,budget,deadline,status){
    var text='Заявка с сайта.\nИмя: '+name+'\nЗадача: '+task+'\nКонтакт: '+contact+'\nБюджет: '+budget+'\nСрок: '+deadline;
    var url='https://t.me/nsv_01?text='+encodeURIComponent(text);
    if(status){status.textContent='Форма подготовила сообщение — открываю Telegram для отправки.';status.style.color='var(--mut)';}
    window.open(url,'_blank');
  }
})();
