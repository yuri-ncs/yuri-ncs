"""Gera os SVGs de seção, stack e rodapé do README (versões dark e light).

Uso: py tools/gen_svg.py   (a partir da raiz do repo)
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
MONO = "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "Inter, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"

# Mesmas cores do banner; o "fg" das peças transparentes contrasta com o fundo do GitHub.
THEMES = {
    "dark": dict(card="#081226", fg="#F0F6FC", muted="#B4C3D9", dim="#5C7399", rule="#2A4470",
                 accent="#1F6FD6", accent2="#8AC0FF", chip="#1E3358", chip_fg="#CFE0F7",
                 teal="#0E7490", purple="#4C1D95", green="#166534"),
    "light": dict(card="#F6F8FC", fg="#0B1A33", muted="#475A78", dim="#64748B", rule="#B8C6DB",
                  accent="#1F6FD6", accent2="#1D4ED8", chip="#DCE5F2", chip_fg="#1E3358",
                  teal="#0E7490", purple="#5B21B6", green="#15803D"),
}

SECTIONS = [("0x01", "Sobre mim", "sobre"), ("0x02", "Stack", "stack"), ("0x03", "Atividade", "atividade")]

# Cada linha usa a cor de um campo do frame CAN do banner (ID, dados, CRC, ACK, demais).
STACK = [
    ("linguagens", "accent", ["C++", "C", "Rust", "Python", "Dart", "C#"]),
    ("embarcado", "teal", ["ESP-IDF", "STM32 HAL", "Embassy", "FreeRTOS", "LVGL"]),
    ("aplicações", "chip", ["Flutter", ".NET · Avalonia", "Dear ImGui", "Electron"]),
    ("ferramentas", "purple", ["BUSMASTER", "J-Link", "Kvaser · PEAK · SocketCAN", "KiCad", "Claude Code"]),
    ("qualidade", "green", ["gtest", "pytest", "HIL", "GitHub Actions", "Docker"]),
]


def text_w(s, size, em=0.6):
    # shortcut: largura estimada por caractere; ajuste `em` se mudar a fonte
    return len(s) * size * em


def svg(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}">\n<title>{escape(title)}</title>\n{body}\n</svg>\n')


def header(tag, title, t):
    x_line = 92 + text_w(title, 28, 0.62) + 24
    # trem de bits no fim da linha, como o CAN_H do banner
    wave = "M1048 36 H1068 V22 H1086 V36 H1100 V22 H1132 V36 H1150 V22 H1164 V36 H1200"
    body = f"""<rect x="0" y="22" width="72" height="30" rx="6" fill="{t['accent']}"/>
<text x="36" y="43" font-family="{MONO}" font-size="16" font-weight="600" fill="#FFFFFF" text-anchor="middle">{tag}</text>
<text x="92" y="47" font-family="{SANS}" font-size="28" font-weight="800" letter-spacing="-0.6" fill="{t['fg']}">{escape(title)}</text>
<path d="M{x_line:.0f} 36 H1040" stroke="{t['rule']}" stroke-width="1.5" stroke-dasharray="4 6"/>
<path d="{wave}" fill="none" stroke="{t['accent']}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>"""
    return svg(1200, 72, f"{tag} {title}", body)


def stack(t):
    rows, y = [], 76
    for label, color, items in STACK:
        rows.append(f'<text x="48" y="{y + 23}" font-family="{MONO}" font-size="16" fill="{t["dim"]}">{escape(label)} =</text>')
        x = 250
        fill = t[color]
        fg = t["chip_fg"] if color == "chip" else "#FFFFFF"
        for item in items:
            w = text_w(item, 16) + 28
            rows.append(f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="34" rx="6" fill="{fill}"/>')
            rows.append(f'<text x="{x + w / 2:.0f}" y="{y + 23}" font-family="{MONO}" font-size="16" '
                        f'font-weight="500" fill="{fg}" text-anchor="middle">{escape(item)}</text>')
            x += w + 10
        assert x < 1160, f"linha '{label}' estoura a largura do card"
        y += 50
    h = y + 24
    body = f"""<clipPath id="c"><rect width="1200" height="{h}" rx="16"/></clipPath>
<g clip-path="url(#c)">
<rect width="1200" height="{h}" fill="{t['card']}"/>
<rect width="6" height="{h}" fill="{t['accent']}"/>
<text x="48" y="48" font-family="{MONO}" font-size="15" fill="{t['accent2']}">~/yuri-ncs $ cat stack.toml</text>
{chr(10).join(rows)}
</g>"""
    return svg(1200, h, "Stack: " + "; ".join(f"{l}: {', '.join(i)}" for l, _, i in STACK), body)


def footer(t):
    prompt = "~/yuri-ncs $ exit"
    x_ack = text_w(prompt, 16) + 20
    body = f"""<text x="0" y="41" font-family="{MONO}" font-size="16" fill="{t['dim']}">{prompt}</text>
<rect x="{x_ack:.0f}" y="18" width="56" height="32" rx="6" fill="{t['green']}"/>
<text x="{x_ack + 28:.0f}" y="40" font-family="{MONO}" font-size="16" font-weight="600" fill="#FFFFFF" text-anchor="middle">ACK</text>
<text x="{x_ack + 72:.0f}" y="41" font-family="{SANS}" font-size="18" fill="{t['muted']}">valeu pela visita</text>"""
    return svg(1200, 64, "~/yuri-ncs $ exit · ACK · valeu pela visita", body)


for name, t in THEMES.items():
    for tag, title, slug in SECTIONS:
        (OUT / f"h-{slug}-{name}.svg").write_text(header(tag, title, t), encoding="utf-8")
    (OUT / f"stack-{name}.svg").write_text(stack(t), encoding="utf-8")
    (OUT / f"footer-{name}.svg").write_text(footer(t), encoding="utf-8")
print("ok:", sorted(p.name for p in OUT.glob("*.svg")))
