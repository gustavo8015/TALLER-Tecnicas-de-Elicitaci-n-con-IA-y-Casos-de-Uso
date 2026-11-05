import json,html
H=json.load(open('historias.json', encoding='utf-8'))
cols=[("Backlog del Producto","backlog"),("Sprint 1 (MVP)","mvp"),("Para el futuro","futuro")]
def card(h):
    return f'<div class="c"><div class="t">{h["id"]} · {h["epica"]}</div><div>{html.escape(h["texto"])}</div><div class="p">{h["puntos"]} pts · {h["prioridad"]}</div></div>'
body="".join(f'<div class="col"><h2>{n} <span>{sum(1 for h in H if h["lista"]==k)}</span></h2>{"".join(card(h) for h in H if h["lista"]==k)}</div>' for n,k in cols)
open('board.html','w').write(f'''<html><head><meta charset="utf-8"><style>
body{{margin:0;font-family:Helvetica,Arial,sans-serif;background:#fff}}.wrap{{padding:20px;width:1500px;background:#15803D}}
h1{{color:#fff;font-size:22px;margin:0 0 14px}}.cols{{display:flex;gap:16px;align-items:flex-start}}
.col{{background:#F1F5F9;border-radius:12px;padding:12px;width:470px}}h2{{font-size:16px;margin:0 0 10px}}h2 span{{background:#CBD5E1;border-radius:8px;padding:1px 8px;font-size:13px}}
.c{{background:#fff;border-radius:8px;padding:10px;margin-bottom:8px;font-size:13px;line-height:1.3;box-shadow:0 1px 2px rgba(0,0,0,.2)}}.t{{font-weight:bold;color:#15803D;margin-bottom:4px}}.p{{color:#475569;font-size:12px;margin-top:6px}}
</style></head><body><div class="wrap"><h1>Voluntariado Connect · User Story Mapping</h1><div class="cols">{body}</div></div></body></html>''')
