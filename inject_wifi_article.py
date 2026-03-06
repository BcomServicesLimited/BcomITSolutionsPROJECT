import re

# Read article parts
with open('/home/ubuntu/BcomITSolutionsPROJECT/wifi-article-parts.html') as f:
    content = f.read()

part1_start = content.index('<!-- SECTION 3b-1')
part1_end = content.index('<!-- END ARTICLE PART 1 -->') + len('<!-- END ARTICLE PART 1 -->')
part2_start = content.index('<!-- SECTION 3b-2')
part2_end = content.index('<!-- END ARTICLE PART 2 -->') + len('<!-- END ARTICLE PART 2 -->')
part3_start = content.index('<!-- SECTION 3b-3')
part3_end = content.index('<!-- END ARTICLE PART 3 -->') + len('<!-- END ARTICLE PART 3 -->')

part1 = content[part1_start:part1_end]
part2 = content[part2_start:part2_end]
part3 = content[part3_start:part3_end]

# Read main page
with open('/home/ubuntu/BcomITSolutionsPROJECT/wifi-range-extension-gold-coast.html') as f:
    page = f.read()

# 1. Add article-section CSS before </style>
article_css = """
    /* ── ARTICLE SECTIONS ── */
    .article-section { padding: 72px 0; background: #fff; }
    .article-body { max-width: 760px; margin: 0 auto; padding: 0 24px; }
    .article-h3 { font-family: 'DM Mono', monospace; font-size: 1.1rem; color: #0d1f3c; margin: 2rem 0 0.75rem; border-left: 3px solid #00c8e0; padding-left: 12px; }
    .article-body p { color: #374151; line-height: 1.8; margin-bottom: 1.25rem; font-size: 1rem; }
    .article-body a { color: #00c8e0; text-decoration: underline; }
    @media (max-width: 600px) { .article-h3 { font-size: 1rem; } }
"""
page = page.replace('</style>', article_css + '\n  </style>', 1)

# 2. Inject Part 1 before SECTION 4
page = page.replace(
    '  <!-- SECTION 4 \u2014 WHY CHOOSE US -->',
    '\n' + part1 + '\n\n  <!-- SECTION 4 \u2014 WHY CHOOSE US -->'
)

# 3. Inject Part 2 before SECTION 5
page = page.replace(
    '  <!-- SECTION 5 \u2014 SERVICE AREAS + WHAT TO EXPECT -->',
    '\n' + part2 + '\n\n  <!-- SECTION 5 \u2014 SERVICE AREAS + WHAT TO EXPECT -->'
)

# 4. Inject Part 3 before SECTION 6
page = page.replace(
    '  <!-- SECTION 6 \u2014 FAQ -->',
    '\n' + part3 + '\n\n  <!-- SECTION 6 \u2014 FAQ -->'
)

# Write back
with open('/home/ubuntu/BcomITSolutionsPROJECT/wifi-range-extension-gold-coast.html', 'w') as f:
    f.write(page)

# Verify div balance
opens = len(re.findall(r'<div[\s>]', page))
closes = len(re.findall(r'</div>', page))
print(f"<div> opens: {opens}, </div> closes: {closes}, balanced: {opens == closes}")

# Verify article parts present
for marker in ['SECTION 3b-1', 'SECTION 3b-2', 'SECTION 3b-3']:
    print(f"{marker} present: {marker in page}")

# Word count
text = re.sub(r'<[^>]+>', ' ', page)
text = re.sub(r'<!--.*?-->', ' ', text, flags=re.DOTALL)
words = text.split()
print(f"Total page word count: {len(words)}")

# Banned words
banned = ['embark','look no further','navigating','picture this','top-notch','unleash','unlock','unveil',
          'transition','crucial','delve','daunting','deep dive','realm','ensure','in conclusion',
          'optimal','furthermore','moreover','comprehensive','vital','robust','testament',
          'significantly','notably','essentially','therefore','thus','in essence']
found = [b for b in banned if b.lower() in text.lower()]
print(f"Banned words: {found if found else 'NONE'}")

# Check images
imgs = re.findall(r'wifi-range-extension-gold-coast-\d+\.webp|wifi-range-extension-gold-coast-infographic\.webp', page)
print(f"Article images found: {set(imgs)}")

# Check bad script tags
bad = page.count('<\\/script>')
print(f"Bad script tags: {bad}")

print("Done.")
