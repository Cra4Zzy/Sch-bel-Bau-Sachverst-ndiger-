from pathlib import Path

p = Path('index.html')
html = p.read_text(encoding='utf-8')

# Replace original hero image treatment with the approved brighter variant.
html = html.replace(
    'background:linear-gradient(135deg,#050f1c0f,#050f1c6b)',
    'background:linear-gradient(135deg,#050f1c08,#050f1c45)',
    1,
)
html = html.replace(
    'filter:brightness(1.4)saturate(.78)contrast(1.03)',
    'filter:brightness(1.82)saturate(.8)contrast(1.02)',
    1,
)

# Add the customer-approved lighter navy overrides if not already present.
marker = 'id="customer-light-navy-variant"'
if marker not in html:
    block = '''\n<style id="customer-light-navy-variant">\n/* Kundenwunsch: das bisher sehr dunkle Navy bewusst heller und offener gestalten,\n   ohne Kontrast, Seriosität und die orange Akzentfarbe zu verlieren. */\n:root{\n  --navy-surface:#173b5d;\n  --navy-surface-hover:#224d72;\n  --navy-deep:#102f4b;\n}\n.cover,\n.field-work,\n.contact-panel,\n.mobile-menu{background:var(--navy-surface)}\n.site-footer{background:var(--navy-deep)}\n.service-row:before{background:var(--navy-surface-hover)}\n.cover-visual{background:#2d6288}\n.cover-visual:after{background:linear-gradient(135deg,rgba(16,47,75,.02),rgba(16,47,75,.30))}\n.header-call{background:rgba(16,47,75,.42)}\n</style>'''
    html = html.replace('</head>', block + '</head>', 1)

p.write_text(html, encoding='utf-8')
