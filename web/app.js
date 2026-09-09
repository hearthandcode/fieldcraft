import {check} from './examples/check.mjs';
const $=s=>document.querySelector(s);
if ($('#run')) {
  const initial=$('#candidate').value;
  const run=()=>{
    try {
      const raw=$('#capacity').value;
      if(raw.trim()==='') throw new RangeError('Enter a capacity');
      const result=check($('#candidate').value,Number(raw));
      $('#verdict').textContent=result.pass?'PASS / Within the contract':'FAIL / Constraint violated';
      $('#verdict').className=result.pass?'cyan':'gold';
      $('#counts').textContent=`${result.count} normalized items · capacity ${raw}`;
      $('#checks').replaceChildren(...[
        `${result.withinCapacity?'✓':'×'} Capacity ceiling ${result.withinCapacity?'satisfied':'exceeded'}`,
        `${result.unique?'✓':'×'} Exact-string uniqueness ${result.unique?'satisfied':'violated'}`
      ].map(t=>{const li=document.createElement('li');li.textContent=t;return li;}));
    } catch(e){$('#verdict').textContent='INVALID INPUT';$('#counts').textContent=e.message;$('#checks').replaceChildren();}
  };
  $('#run').onclick=run;
  $('#fail').onclick=()=>{$('#capacity').value=2;$('#candidate').value='Check file encoding\nCheck file encoding\nRecord source digest';run();};
  $('#reset').onclick=()=>{$('#capacity').value=4;$('#candidate').value=initial;run();};
  for(const el of [$('#capacity'),$('#candidate')])el.oninput=()=>{$('#verdict').textContent='Changed / Run to check';$('#counts').textContent='The input changed; the previous result is stale.';$('#checks').replaceChildren();};
  run();
}
if($('#search')){
 let filter='all';
 const update=()=>{let count=0;const q=$('#search').value.toLowerCase().trim();document.querySelectorAll('.collection-row').forEach(row=>{const visible=(filter==='all'||row.dataset.category===filter)&&row.textContent.toLowerCase().includes(q);row.hidden=!visible;if(visible)count++;});$('#search-status').textContent=count?`${count} ${count===1?'entry':'entries'} shown`:'No matching entries. Try another subject.';};
 $('#search').oninput=update;
 document.querySelectorAll('[data-filter]').forEach(button=>button.onclick=()=>{filter=button.dataset.filter;document.querySelectorAll('[data-filter]').forEach(b=>{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button));});update();});
}
