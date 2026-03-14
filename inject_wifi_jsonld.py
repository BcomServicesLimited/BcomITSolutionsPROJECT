import re

with open('/home/ubuntu/BcomITSolutionsPROJECT/wifi-range-extension-gold-coast.html') as f:
    page = f.read()

# Check what's already there
print(f"Existing ld+json blocks: {page.count('application/ld+json')}")
print(f"BreadcrumbList already: {'BreadcrumbList' in page}")

# The BreadcrumbList is already in the head — check it matches spec
bc_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', page, re.DOTALL)
if bc_match:
    print("Existing block preview:", bc_match.group(1)[:200])

# Build LocalBusiness JSON-LD
local_business = '''{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "ProfessionalService"],
  "name": "Bcom IT Solutions — WiFi Range Extension Gold Coast",
  "serviceType": "WiFi Range Extension",
  "telephone": "+61730418993",
  "email": "hello@bcomservices.com",
  "url": "https://bcomservices.com.au/wifi-range-extension-gold-coast.html",
  "areaServed": {"@type": "City", "name": "Gold Coast", "addressRegion": "QLD", "addressCountry": "AU"},
  "provider": {"@type": "Organization", "name": "Bcom IT Solutions Pty Ltd", "taxID": "92 636 893 108"}
}'''

# Build FAQPage JSON-LD from the 5 Q&As
faq_jsonld = '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I buy a WiFi extender or booster from a shop, or is there a better option?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Plug-in range extenders are the most common solution people try first — and the one we most often have to undo. They create a separate network, halve the available bandwidth and cause devices to hold onto a weak signal rather than switching automatically. For most Gold Coast homes a better option is a wired access point (if you have an Ethernet point nearby), a powerline adapter setup, or an additional mesh node. We assess your home and tell you what will actually work before you spend anything. Call 07 3041 8993 to discuss."
      }
    },
    {
      "@type": "Question",
      "name": "I have no Ethernet points in the dead spot area — what are my options on the Gold Coast?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You have three main options without running new cable. Powerline adapters use your home's electrical wiring to carry the network signal and work well in most Gold Coast homes. MoCA adapters use existing coaxial cable points if your home has them — these are faster than powerline. A wireless mesh node is the third option and works without any existing cabling, though performance depends on how well the node can reach your main router. We assess which will work best in your specific home when we visit."
      }
    },
    {
      "@type": "Question",
      "name": "Can you extend WiFi to my garage, shed or backyard on the Gold Coast?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Outdoor and detached-building coverage is one of the most common extension jobs we do on the Gold Coast. Options include weatherproof outdoor access points, powerline adapters run to an outdoor GPO, or a mesh node positioned to reach the area. The right solution depends on the distance, what cabling is available and whether the space needs full speed or just basic coverage. Call 07 3041 8993 to discuss your specific layout."
      }
    },
    {
      "@type": "Question",
      "name": "I already have a mesh system but still have dead spots — can you fix that?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Poor mesh performance is usually caused by a node in the wrong location, wireless backhaul where wired would be better, or simply needing an additional node in a specific area. We come to your Gold Coast home, assess the existing node positions and signal map, reposition or reconfigure where possible and add a new node if that is the right fix. Call 07 3041 8993 to book."
      }
    },
    {
      "@type": "Question",
      "name": "How much does WiFi range extension cost on the Gold Coast?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cost depends on the solution needed. A simple powerline adapter setup or mesh node addition is typically a call-out fee plus hardware. A wired access point installation may involve a short cable run which we quote separately. We always assess first and confirm the full cost before starting any work — no surprises. Call 07 3041 8993 for a quote or to discuss your situation before booking."
      }
    }
  ]
}'''

# Build HowTo JSON-LD
howto_jsonld = '''{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How WiFi Range Extension Works at Your Gold Coast Home",
  "description": "What to expect when you book a WiFi range extension visit with Bcom IT Solutions on the Gold Coast.",
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "You Call and Describe the Dead Spots",
      "text": "We ask where the dead spots are, what router you have, and whether you have Ethernet or coaxial points nearby — so we arrive with the right hardware to fix it in one visit."
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "We Walk the Home and Audit the Signal",
      "text": "We test signal strength throughout your home before recommending anything, checking whether repositioning the existing router would help and identifying the best extension solution for your layout."
    },
    {
      "@type": "HowToStep",
      "position": 3,
      "name": "We Install and Configure the Solution",
      "text": "Hardware installed in the best location with network name and password matched to your existing WiFi — your devices connect automatically without any changes needed on your end."
    },
    {
      "@type": "HowToStep",
      "position": 4,
      "name": "Signal Tested in Every Problem Area",
      "text": "We test and show you signal results in every dead spot area, reconnect devices in affected rooms and confirm seamless roaming before leaving."
    }
  ]
}'''

# Build the three new script blocks
new_blocks = f"""
  <script type="application/ld+json">
  {local_business}
  </script>

  <script type="application/ld+json">
  {faq_jsonld}
  </script>

  <script type="application/ld+json">
  {howto_jsonld}
  </script>
"""

# Inject before </body>
if new_blocks.strip() not in page:
    page = page.replace('</body>', new_blocks + '</body>')
    with open('/home/ubuntu/BcomITSolutionsPROJECT/wifi-range-extension-gold-coast.html', 'w') as f:
        f.write(page)
    print("JSON-LD blocks injected successfully")
else:
    print("Blocks already present")

# Verify
with open('/home/ubuntu/BcomITSolutionsPROJECT/wifi-range-extension-gold-coast.html') as f:
    page2 = f.read()

print(f"Total ld+json blocks: {page2.count('application/ld+json')}")
print(f"BreadcrumbList: {'BreadcrumbList' in page2}")
print(f"LocalBusiness: {'LocalBusiness' in page2}")
print(f"FAQPage: {'FAQPage' in page2}")
print(f"HowTo: {'HowTo' in page2}")
bad = page2.count('<' + '/script>')
print(f'Bad script tags: {bad}')
