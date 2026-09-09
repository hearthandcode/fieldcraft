from pathlib import Path
import markdown, json, shutil, hashlib, html
root=Path(__file__).resolve().parents[1]; out=root/'site';out.mkdir(exist_ok=True)
registry=json.loads((root/'publication.json').read_text())
for a in registry['articles']:
 source=root/'content'/f"{a['slug']}.md"
 assert hashlib.sha256(source.read_bytes()).hexdigest()==a['export_sha256'],'Content drift: re-export the master'
for name in ['style.css','app.js','index.html']:
 shutil.copy2(root/'web'/name,out/name)
shutil.copytree(root/'examples',out/'examples',dirs_exist_ok=True)
shutil.copytree(root/'content',out/'content',dirs_exist_ok=True)
shutil.copy2(root/'publication.json',out/'publication.json')
header='''<header><a class="brand" href="./"><span class="mark">✳</span> HEARTH & CODE <span class="brand-sub">/ FIELDCRAFT</span></a><nav aria-label="Main"><a href="./#library">The collection</a><a href="./#about">About</a><a href="https://github.com/hearthandcode/fieldcraft">GitHub ↗</a></nav></header>'''
demo='''<section class="demo" aria-labelledby="demo-title"><div class="demo-top"><span class="eyebrow">WORKING EXAMPLE / LOCAL EXECUTION</span><h3 id="demo-title">A small contract. An observable result.</h3></div><div class="demo-grid"><div><label for="capacity">Capacity k</label><input id="capacity" type="number" min="0" max="1000" value="4"><label for="candidate">Candidate X · one item per line</label><textarea id="candidate" rows="6">Check file encoding
Validate required metadata
Record source digest</textarea><div class="demo-actions"><button id="run" class="primary">Run the check ↗</button><button id="fail">Failing fixture</button><button id="reset">Reset</button></div></div><div class="result" aria-live="polite" aria-atomic="true"><span class="eyebrow">PREDICATE RESULT</span><h3 id="verdict">Ready to check</h3><p id="counts">Run the example to evaluate the candidate.</p><ul id="checks"></ul><p class="note">No model call. No data leaves this page.</p></div></div></section>'''
for a in registry['articles']:
 body=markdown.markdown((root/'content'/f"{a['slug']}.md").read_text(),extensions=['fenced_code','tables']).replace('<!--DEMO-->',demo)
 page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="One independent acceptance predicate, a runnable example, and a counterexample."><title>{html.escape(a['title'])} · Fieldcraft</title><link rel="stylesheet" href="style.css"><script type="module" src="app.js"></script></head><body><a class="skip" href="#main">Skip to content</a>{header}<main id="main" class="article-layout"><aside class="article-aside"><a href="./#library">← The collection</a><p class="eyebrow">FIELD NOTE 001</p><p>ESS &<br>agentic engineering</p><hr><p>09 SEP 2026<br>6 MIN READ</p><span class="pill">Design preview</span><p><a href="content/{a['slug']}.md" download>Markdown ↓</a></p><p><a href="examples/check.mjs" download>Working example ↓</a></p></aside><article><div class="eyebrow">CONSTRAINTS / VALIDATION / EVIDENCE</div><h1>{html.escape(a['title'])}</h1><p class="article-deck">Turn “looks right” into a condition you can inspect.</p>{body}<a class="back" href="./">← Back to Fieldcraft</a></article></main><footer><span>HEARTH & CODE · FIELDCRAFT</span><span>One technique. A working example. A visible result.</span></footer></body></html>'''
 (out/f"{a['slug']}.html").write_text(page)
(out/'.nojekyll').touch()
print('Built index +',len(registry['articles']),'article; source hashes verified')
