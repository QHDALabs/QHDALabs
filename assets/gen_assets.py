# -*- coding: utf-8 -*-
"""Generator grafik SVG dla profilu QHDALabs: Matrix rain + sylwetka Buddy (enso)."""
import random, os, io

random.seed(4242)

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

KATA = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ"
ALNUM = "0123456789ABCDEFXYZΔΨΩλφψ<>|/\\+*=:."

def glyph():
    return random.choice(KATA) if random.random() < 0.55 else random.choice(ALNUM)

def esc(c):
    return {"<": "&lt;", ">": "&gt;", "&": "&amp;"}.get(c, c)


# --------------------------------------------------------------------------
# deszcz Matrixa
# --------------------------------------------------------------------------
def rain(width, height, step=25, size=15, minlen=6, maxlen=16, opacity=1.0,
         head="#EAFFF1", body="#4CFF7A", tail="#17C24E"):
    cols = []
    x = 6
    while x < width:
        n = random.randint(minlen, maxlen)
        dur = round(random.uniform(5.5, 15.0), 2)
        delay = round(random.uniform(-16.0, 0.0), 2)
        span = n * size
        g = [f'<g class="col" style="--t:{dur}s;--d:{delay}s;--h:{span}px" '
             f'transform="translate({x},0)">']
        for i in range(n):
            y = i * size
            t = i / max(1, n - 1)
            if i == n - 1:
                fill, op, extra = head, 1.0, ' class="head"'
            elif i > n - 4:
                fill, op, extra = body, 0.98, ''
            else:
                fill, op, extra = tail, round(0.22 + 0.62 * t, 2), ''
            ch = esc(glyph())
            flick = ''
            if random.random() < 0.22:
                flick = (f'<animate attributeName="opacity" values="{op};{max(0.05, op*0.15):.2f};{op}" '
                         f'dur="{round(random.uniform(0.6,2.4),2)}s" repeatCount="indefinite" '
                         f'begin="{round(random.uniform(0,3),2)}s"/>')
            g.append(f'<text{extra} x="0" y="{y}" fill="{fill}" opacity="{op}">{ch}{flick}</text>')
        g.append('</g>')
        cols.append("".join(g))
        x += step
    return (f'<g class="rain" opacity="{opacity}" style="--H:{height}px">'
            + "".join(cols) + '</g>')


RAIN_CSS = """
    .rain text{font-family:'Courier New',ui-monospace,monospace;font-size:15px;
      text-anchor:middle;letter-spacing:0}
    .rain .head{filter:url(#glow-s)}
    .col{animation:fall var(--t) linear var(--d) infinite}
    @keyframes fall{
      0%  {transform:translateY(calc(-1 * var(--h)))}
      100%{transform:translateY(var(--H))}
    }
"""

# --------------------------------------------------------------------------
# Budda — sylwetka w pozycji lotosu (lokalny układ: 0,0 = środek podołka)
# --------------------------------------------------------------------------
# ksztalty bryly (rysowane dwukrotnie: masa + kontur)
_SHAPES = """
        <path d="M -104 6 C -104 -20 -56 -34 0 -34 C 56 -34 104 -20 104 6
                 C 104 24 58 34 0 34 C -58 34 -104 24 -104 6 Z"/>
        <ellipse cx="-62" cy="-16" rx="28" ry="15"/>
        <ellipse cx="62"  cy="-16" rx="28" ry="15"/>
        <path d="M -52 -6 C -58 -44 -52 -70 -40 -84 C -30 -95 -15 -100 0 -100
                 C 15 -100 30 -95 40 -84 C 52 -70 58 -44 52 -6 Z"/>
        <path class="limb" d="M -38 -80 C -60 -58 -60 -26 -20 -14"/>
        <path class="limb" d="M  38 -80 C  60 -58  60 -26  20 -14"/>
        <ellipse cx="0" cy="-14" rx="21" ry="9"/>
        <path class="nostroke" d="M -11 -114 h 22 v 22 h -22 z"/>
        <ellipse cx="-28" cy="-132" rx="5.5" ry="12"/>
        <ellipse cx="28"  cy="-132" rx="5.5" ry="12"/>
        <ellipse cx="0" cy="-134" rx="27" ry="31"/>
        <ellipse cx="0" cy="-164" rx="12.5" ry="10"/>
        <circle  cx="0" cy="-178" r="4.5"/>
"""

_ARMS = """
        <path d="M -38 -80 C -60 -58 -60 -26 -20 -14"/>
        <path d="M  38 -80 C  60 -58  60 -26  20 -14"/>
"""

_DETAIL = """
        <path class="eyes" d="M -19 -139 q 8.5 8 17 0"/>
        <path class="eyes" d="M   2 -139 q 8.5 8 17 0"/>
        <path d="M -9 -122 q 9 6 18 0"/>
        <path d="M -34 -62 q 34 21 68 0"/>
        <path d="M -42 -42 q 42 24 84 0"/>
        <path d="M -70 14 q 24 -16 46 0"/>
        <path d="M -24 18 q 24 -18 48 0"/>
        <path d="M  24 14 q 24 -16 46 0"/>
"""

BUDDHA = ('      <g class="breathe">\n'
          '        <g class="mass">' + _SHAPES + '</g>\n'
          '        <g class="arm-out">' + _ARMS + '</g>\n'
          '        <g class="arm-in">' + _ARMS + '</g>\n'
          '        <g class="line">' + _SHAPES + '</g>\n'
          '        <g class="detail">' + _DETAIL + '</g>\n'
          '        <circle class="urna" cx="0" cy="-148" r="3.4"/>\n'
          '      </g>\n')

BUDDHA_CSS = """
    .buddha{filter:url(#glow-m)}
    .mass{fill:#03130A;stroke:none}
    .mass .limb{fill:none;stroke:#03130A;stroke-width:16;stroke-linecap:round}
    .arm-out path{fill:none;stroke:url(#skinV);stroke-width:17;stroke-linecap:round}
    .arm-in  path{fill:none;stroke:#03130A;stroke-width:13.2;stroke-linecap:round}
    .line{fill:none;stroke:url(#skinV);stroke-width:2.2;
      stroke-linejoin:round;stroke-linecap:round}
    .line .limb,.line .nostroke{stroke:none}
    .detail{fill:none;stroke:#8CF7B0;stroke-width:1.7;opacity:.62;stroke-linecap:round}
    .detail .eyes{stroke:#EAFFF1;stroke-width:2.3;opacity:1}
    .urna{fill:#FFE9A8;filter:url(#glow-s)}
    .breathe{animation:breathe 7.5s ease-in-out infinite;transform-origin:0 0}
    @keyframes breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.012)}}
"""

DEFS = """
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0"   stop-color="#03110a"/>
      <stop offset="0.55" stop-color="#040b08"/>
      <stop offset="1"   stop-color="#010604"/>
    </linearGradient>
    <radialGradient id="aura" cx="50%" cy="52%" r="55%">
      <stop offset="0"   stop-color="#0b3d22" stop-opacity="0.85"/>
      <stop offset="0.6" stop-color="#04140c" stop-opacity="0.55"/>
      <stop offset="1"   stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="veil" cx="50%" cy="50%" r="50%">
      <stop offset="0"   stop-color="#010604" stop-opacity="0.92"/>
      <stop offset="0.7" stop-color="#010604" stop-opacity="0.62"/>
      <stop offset="1"   stop-color="#010604" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="skinV" gradientUnits="userSpaceOnUse" x1="0" y1="-190" x2="0" y2="40">
      <stop offset="0"    stop-color="#FFE9A8"/>
      <stop offset="0.42" stop-color="#9DFFC2"/>
      <stop offset="1"    stop-color="#0BD45E"/>
    </linearGradient>
    <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0"   stop-color="#00FF41"/>
      <stop offset="0.5" stop-color="#FFE9A8"/>
      <stop offset="1"   stop-color="#00C8A0"/>
    </linearGradient>
    <linearGradient id="wire" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0"   stop-color="#00FF41" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#00FF41" stop-opacity="0.9"/>
      <stop offset="1"   stop-color="#00FF41" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow-s" x="-120%" y="-120%" width="340%" height="340%">
      <feGaussianBlur stdDeviation="2.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow-m" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="3.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1.2" fill="#7CFFB2" opacity="0.055"/>
    </pattern>
  </defs>
"""


# ==========================================================================
# 1. BANNER
# ==========================================================================
def banner(path, nodes, commits, code_mb, since):
    W, H = 1200, 460
    s = io.StringIO()
    s.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="QHDALabs - Strategic AI, Quantum Systems and Civilizational Infrastructure">\n')
    s.write(DEFS)
    s.write('  <style>\n')
    s.write(RAIN_CSS)
    s.write(BUDDHA_CSS)
    s.write("""
    .mono{font-family:'Courier New',ui-monospace,monospace}
    .title{font-family:'Courier New',ui-monospace,monospace;font-weight:700;
      font-size:60px;letter-spacing:12px;text-anchor:middle;fill:#EAFFF1;filter:url(#glow-s)}
    .sub{font-family:'Courier New',ui-monospace,monospace;font-size:13.5px;
      letter-spacing:5px;text-anchor:middle;fill:#7CFFB2;opacity:.9}
    .hud{font-family:'Courier New',ui-monospace,monospace;font-size:12.5px;fill:#00FF41;opacity:.78}
    .caret{animation:blink 1.05s steps(1) infinite}
    @keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}
    .flicker{animation:flick 6.5s ease-in-out infinite}
    @keyframes flick{0%,92%,100%{opacity:1}93%{opacity:.35}95%{opacity:1}96.5%{opacity:.55}}
    .enso{fill:none;stroke:url(#ring);stroke-linecap:round;filter:url(#glow-s)}
    .pulse{animation:pulse 4.6s ease-in-out infinite}
    @keyframes pulse{0%,100%{opacity:.30}50%{opacity:.72}}
    @media (prefers-reduced-motion:reduce){
      .col,.breathe,.caret,.flicker,.pulse{animation:none}
    }
""")
    s.write('  </style>\n')
    s.write(f'  <clipPath id="cut"><rect x="0" y="0" width="{W}" height="{H}" rx="16"/></clipPath>\n')
    s.write('  <g clip-path="url(#cut)">\n')
    s.write(f'    <rect width="{W}" height="{H}" fill="url(#bg)"/>\n')
    s.write(f'    <rect width="{W}" height="{H}" fill="url(#aura)"/>\n')
    s.write('    ' + rain(W, H, step=25, opacity=0.8) + '\n')
    # welon przyciemniajacy tlo pod postacia
    s.write('    <ellipse cx="600" cy="290" rx="370" ry="215" fill="url(#veil)"/>\n')
    # enso — dwa pierscienie wokol glowy
    s.write('    <g class="pulse">\n')
    s.write('      <circle class="enso" cx="600" cy="256" r="84" stroke-width="2.6" '
            'stroke-dasharray="430 98" stroke-dashoffset="40" opacity=".9">\n'
            '        <animateTransform attributeName="transform" type="rotate" '
            'from="0 600 256" to="360 600 256" dur="46s" repeatCount="indefinite"/>\n'
            '      </circle>\n')
    s.write('      <circle class="enso" cx="600" cy="256" r="102" stroke-width="1.1" '
            'stroke-dasharray="3 11" opacity=".5">\n'
            '        <animateTransform attributeName="transform" type="rotate" '
            'from="360 600 256" to="0 600 256" dur="88s" repeatCount="indefinite"/>\n'
            '      </circle>\n')
    s.write('    </g>\n')
    # budda
    s.write('    <g class="buddha" transform="translate(600,398) scale(1.06)">\n')
    s.write(BUDDHA)
    s.write('    </g>\n')
    # naglowki
    s.write(f'    <text class="hud" x="34" y="38">root@qhdalabs:~$ ./wake_up.sh'
            f'<tspan class="caret" dx="8">&#9608;</tspan></text>\n')
    s.write(f'    <text class="hud" x="{W-34}" y="38" text-anchor="end">'
            f'NODES {nodes} &#183; COMMITS {commits} &#183; CODE {code_mb} &#183; SINCE {since}</text>\n')
    s.write('    <text class="title flicker" x="600" y="110">QHDALabs</text>\n')
    s.write('    <text class="sub" x="600" y="139">'
            'STRATEGIC AI &#183; QUANTUM SYSTEMS &#183; CIVILIZATIONAL INFRASTRUCTURE</text>\n')
    # sygnatura na dole
    s.write('    <text class="hud" x="600" y="447" text-anchor="middle" opacity=".55">'
            '&#12467;&#12540;&#12489;&#12399;&#36947;&#12391;&#12354;&#12427; '
            '&#183; THE CODE IS THE PATH</text>\n')
    # scanlines + ramka
    s.write(f'    <rect width="{W}" height="{H}" fill="url(#scan)"/>\n')
    s.write(f'    <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="15" fill="none" '
            f'stroke="#00FF41" stroke-opacity=".32" stroke-width="1.5"/>\n')
    for (cx, cy, dx, dy) in [(18, 18, 1, 1), (W-18, 18, -1, 1), (18, H-18, 1, -1), (W-18, H-18, -1, -1)]:
        s.write(f'    <path d="M {cx} {cy+26*dy} L {cx} {cy} L {cx+26*dx} {cy}" fill="none" '
                f'stroke="#7CFFB2" stroke-opacity=".65" stroke-width="2"/>\n')
    s.write('  </g>\n</svg>\n')
    open(path, "w", encoding="utf-8").write(s.getvalue())


# ==========================================================================
# 2. DIVIDER
# ==========================================================================
def divider(path):
    W, H = 1200, 22
    s = io.StringIO()
    s.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" role="img" aria-label="divider">\n')
    s.write("""  <defs>
    <linearGradient id="ln" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#00FF41" stop-opacity="0"/>
      <stop offset="0.2" stop-color="#00FF41" stop-opacity=".75"/>
      <stop offset="0.8" stop-color="#00FF41" stop-opacity=".75"/>
      <stop offset="1" stop-color="#00FF41" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="dot"><stop offset="0" stop-color="#EAFFF1"/>
      <stop offset="1" stop-color="#00FF41" stop-opacity="0"/></radialGradient>
  </defs>
  <style>
    text{font-family:'Courier New',ui-monospace,monospace;font-size:11px;fill:#00FF41;opacity:.45}
    .run{animation:run 6s linear infinite}
    @keyframes run{0%{transform:translateX(0)}100%{transform:translateX(1200px)}}
    @media (prefers-reduced-motion:reduce){.run{animation:none}}
  </style>
""")
    s.write(f'  <path d="M 0 {H/2} H {W}" stroke="url(#ln)" stroke-width="1.2"/>\n')
    xs = [40 + i * 74 for i in range(16)]
    for x in xs:
        s.write(f'  <text x="{x}" y="{H/2+4}" text-anchor="middle">{esc(glyph())}</text>\n')
    s.write(f'  <circle class="run" cx="-40" cy="{H/2}" r="26" fill="url(#dot)"/>\n')
    s.write('</svg>\n')
    open(path, "w", encoding="utf-8").write(s.getvalue())


# ==========================================================================
# 3. FOOTER — enso + motto
# ==========================================================================
def footer(path, motto):
    W, H = 1200, 170
    s = io.StringIO()
    s.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" role="img" aria-label="QHDALabs footer">\n')
    s.write(DEFS)
    s.write('  <style>\n')
    s.write(RAIN_CSS)
    s.write("""
    .enso{fill:none;stroke:url(#ring);stroke-linecap:round;filter:url(#glow-s)}
    .motto{font-family:'Courier New',ui-monospace,monospace;font-size:14px;letter-spacing:5.5px;
      text-anchor:middle;fill:#7CFFB2;opacity:.92}
    .tag{font-family:'Courier New',ui-monospace,monospace;font-size:11.5px;letter-spacing:3px;
      text-anchor:middle;fill:#00FF41;opacity:.5}
    .pulse{animation:pulse 5.4s ease-in-out infinite}
    @keyframes pulse{0%,100%{opacity:.45}50%{opacity:.95}}
    @media (prefers-reduced-motion:reduce){.col,.pulse{animation:none}}
""")
    s.write('  </style>\n')
    s.write('  <clipPath id="cut"><rect width="%d" height="%d" rx="14"/></clipPath>\n' % (W, H))
    s.write('  <g clip-path="url(#cut)">\n')
    s.write(f'    <rect width="{W}" height="{H}" fill="url(#bg)"/>\n')
    s.write('    ' + rain(W, H, step=28, minlen=4, maxlen=9, opacity=0.55) + '\n')
    s.write(f'    <ellipse cx="600" cy="72" rx="250" ry="76" fill="url(#veil)"/>\n')
    s.write('    <g class="pulse">\n')
    s.write('      <circle class="enso" cx="600" cy="62" r="34" stroke-width="2.4" '
            'stroke-dasharray="175 40">\n'
            '        <animateTransform attributeName="transform" type="rotate" '
            'from="0 600 62" to="360 600 62" dur="34s" repeatCount="indefinite"/>\n'
            '      </circle>\n')
    s.write('    </g>\n')
    s.write('    <circle cx="600" cy="62" r="4" fill="#FFE9A8" filter="url(#glow-s)"/>\n')
    s.write('    <path d="M 120 62 H 540" stroke="url(#wire)" stroke-width="1.2"/>\n')
    s.write('    <path d="M 660 62 H 1080" stroke="url(#wire)" stroke-width="1.2"/>\n')
    s.write(f'    <text class="motto" x="600" y="124">{motto}</text>\n')
    s.write('    <text class="tag" x="600" y="148">QHDALabs &#183; POLAND &#183; qhdalabs.com</text>\n')
    s.write(f'    <rect width="{W}" height="{H}" fill="url(#scan)"/>\n')
    s.write(f'    <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="13" fill="none" '
            f'stroke="#00FF41" stroke-opacity=".28" stroke-width="1.4"/>\n')
    s.write('  </g>\n</svg>\n')
    open(path, "w", encoding="utf-8").write(s.getvalue())


banner(os.path.join(OUT, "qhda-banner.svg"), nodes=21, commits=349, code_mb="1.96MB", since="2026-02")
divider(os.path.join(OUT, "qhda-divider.svg"))
footer(os.path.join(OUT, "qhda-footer.svg"),
       "THINK DEEP &#183; BUILD BOLD &#183; SCALE CIVILIZATIONS")

for f in ("qhda-banner.svg", "qhda-divider.svg", "qhda-footer.svg"):
    p = os.path.join(OUT, f)
    print(f, os.path.getsize(p), "B")
