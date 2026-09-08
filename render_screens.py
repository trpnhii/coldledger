from pathlib import Path
import re
import subprocess
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
SOURCE = (ROOT / "dist" / "index.html").read_text(encoding="utf-8")
OUT = Path("/workspace/scratch/coldledger-screens")
OUT.mkdir(parents=True, exist_ok=True)

screens = [
    ("01-login", "login"),
    ("02-dashboard", "dashboard"),
    ("03-shipments", "shipments"),
    ("04-create-shipment", "newshipment"),
    ("05-live-monitoring", "monitor"),
    ("06-incident-review", "incidents"),
    ("07-chain-of-custody", "custody"),
    ("08-evidence-package", "evidence"),
    ("09-settlement-review", "settlement"),
    ("10-devices-integrations", "devices"),
    ("11-analytics-impact", "impact"),
]

print_css = """
@page { size: 1440px 900px; margin: 0; }
html, body { width: 1440px; height: 900px; overflow: hidden; }
.main { height: 900px; overflow: hidden; }
.topbar { height: 62px; }
.head { margin: 8px 0 16px; }
.card { box-shadow: 0 5px 18px rgba(21,55,45,.06); }
.screen-index { position: fixed; }
"""

for filename, target in screens:
    html = SOURCE.replace("</style>", print_css + "</style>")
    html = html.replace('id="login" class="loginpage page active"', 'id="login" class="loginpage page"')
    html = html.replace('id="login" class="loginpage page"', 'id="login" class="loginpage page active"' if target == "login" else 'id="login" class="loginpage page"')
    html = re.sub(r'(id="(?:dashboard|shipments|newshipment|monitor|incidents|custody|evidence|settlement|devices|impact)" class="page) active"', r'\1"', html)
    if target != "login":
        html = html.replace(f'id="{target}" class="page"', f'id="{target}" class="page active"')
    html = html.replace('<b id="screenName">Dashboard</b>', f'<b id="screenName">{target.replace("newshipment", "Create shipment").replace("monitor", "Live monitoring").replace("incidents", "Incident review").replace("custody", "Chain of custody").replace("evidence", "Evidence package").replace("settlement", "Settlement review").replace("devices", "Devices & integrations").replace("impact", "Analytics & impact").title()}</b>')
    pdf = OUT / f"{filename}.pdf"
    HTML(string=html, base_url=str(ROOT / "dist")).write_pdf(pdf)
    subprocess.run(["pdftoppm", "-f", "1", "-singlefile", "-png", "-r", "96", str(pdf), str(OUT / filename)], check=True)
    pdf.unlink()

print(f"Rendered {len(screens)} screens to {OUT}")
