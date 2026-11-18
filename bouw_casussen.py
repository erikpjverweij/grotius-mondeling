"""Voegt alle casusbestanden uit casussen/index.json samen tot casussen.js.
Draai na het toevoegen of wijzigen van een casusbestand:  python bouw_casussen.py"""
import json, pathlib
d = pathlib.Path(__file__).parent
idx = json.loads((d / "casussen" / "index.json").read_text(encoding="utf-8"))
alle = []
for f in idx["bestanden"]:
    alle += json.loads((d / "casussen" / f).read_text(encoding="utf-8"))
ids = [c["id"] for c in alle]
dubbel = {i for i in ids if ids.count(i) > 1}
if dubbel:
    raise SystemExit(f"Dubbele casus-id's: {sorted(dubbel)}")
(d / "casussen.js").write_text("window.CASUSSEN=" + json.dumps(alle, ensure_ascii=False) + ";\n", encoding="utf-8")
print(f"{len(alle)} casussen geschreven naar casussen.js")
