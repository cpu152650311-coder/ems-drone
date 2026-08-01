#!/usr/bin/env python3
"""ems-drone: 6篇补内链(Related Reading区块) + 3篇词数扩充"""
import re, os, json

index = json.load(open('/tmp/drone-cands.json'))
TITLES = {}
import glob
for f in glob.glob('blog/*/index.html'):
    html = open(f, encoding='utf-8').read()
    t = re.search(r'<title>([^<]+)</title>', html)
    slug = os.path.basename(os.path.dirname(f))
    if t:
        TITLES[slug] = t.group(1).replace(' — EMS Drone','').replace(' | EMS Drone','').strip()

def anchor_text(title):
    t = re.sub(r'^(How to |The |A |An )', '', title)
    t = re.sub(r'[:—|&].*$', '', t).strip()
    t = re.sub(r'\s+', ' ', t).strip()
    return t.lower()[:42] if t else 'related guide'

# 1. 插入 Related Reading 区块(6篇)
TARGETS = ['uav-component-build-vs-buy','low-altitude-economy-components','flight-controller-esc-matching',
           'drone-powertrain-matching','uav-airframe-materials-guide','uav-supply-chain-layers']

for slug in TARGETS:
    path = f'blog/{slug}/index.html'
    html = open(path, encoding='utf-8').read()
    if 'Related Reading' in html:
        print(f"ℹ️ {slug}: 已有区块")
        continue
    cands = index.get(slug, [])
    items = '\n          '.join(
        f'<li><a href="/blog/{c}/">{anchor_text(TITLES.get(c, c))}</a></li>' for c in cands)
    block = f'''<section class="related-reading" style="max-width:1100px;margin:0 auto;padding:48px 24px;">
  <h2 style="font-size:1.5rem;margin-bottom:20px;">Related Reading</h2>
  <ul style="padding-left:20px;line-height:2.1;">
          {items}
  </ul>
</section>
'''
    marker = '</article>'
    if marker not in html:
        print(f"⚠️ {slug}: 无</article>")
        continue
    html = html.replace(marker, block + marker, 1)
    open(path, 'w', encoding='utf-8').write(html)
    print(f"✅ {slug}: 内链区块插入")

# 2. 词数扩充(3篇): 在 </article> 前加一段
EXPANSIONS = {
 'low-altitude-economy-components': ('''<h2>The Component Stack That Scales</h2>
<p>Low-altitude economy deployments share a common procurement pattern regardless of vertical: integrators standardize on a small set of proven components and scale them across missions. The core stack starts with a reliable mid-size motor and matching ESC, a battery pack sized for the endurance target, and a GNSS module with RTK capability for the precision positioning that city-scale operations demand.</p>
<p>Payload integration follows the same logic. A single standardized gimbal mount and a common power rail let operators swap cameras, sensors, or delivery mechanisms between missions without redesigning the airframe. This modularity directly reduces the number of SKUs a distributor must stock, which is why the most successful low-altitude programs treat the component catalog as a system design exercise rather than a parts list.</p>
<p>For distributors, the practical takeaway is to carry the full stack, not just the airframe. Customers building low-altitude solutions buy motors, ESCs, batteries, GNSS modules, and radios together — and they expect one supplier who can validate that the combination works. That is the difference between selling components and selling a working low-altitude system.</p>'''),
 'flight-controller-esc-matching': ('''<h2>Signal Paths That Matter</h2>
<p>The physical link between flight controller and ESC is the DShot or PWM signal wire, but the engineering link goes deeper. The flight controller's PWM update rate, the ESC's firmware response time, and the motor's electrical time constant form a control loop that must be stable across the entire throttle range.</p>
<p>On multirotor platforms, the loop runs at 1 kHz or higher, which means signal latency of even a few milliseconds shows up as visible oscillation or poor yaw response. This is why matching is not just about connector compatibility — it is about selecting an ESC firmware that responds fast enough for the flight controller's chosen protocol, and a motor that does not exceed the ESC's current rating during aggressive maneuvers.</p>
<p>For industrial platforms carrying payloads, we recommend documenting the full signal chain in the integration spec: protocol, update rate, ESC firmware version, and motor winding. Teams that write this down once eliminate an entire class of field failures that otherwise surface only after deployment.</p>'''),
 'uav-supply-chain-layers': ('''<h2>Where the Layers Meet</h2>
<p>The seams between supply-chain layers are where most integration problems appear. A motor that is qualified in isolation may still fail when paired with an ESC that switches at a different frequency, and a battery pack that meets capacity specs on paper may sag under the transient load of a heavy-lift throttle change.</p>
<p>Mature distributors handle this by testing at the layer boundaries: motor-ESC pairs on a thrust stand, battery-ESC compatibility under simulated mission profiles, and airframe vibration isolation validated against the actual IMU mounting. Each boundary test catches a class of problems that component-level datasheets cannot reveal.</p>
<p>This is also where documentation pays off. Every layer handoff should specify not just part numbers but the interface parameters that matter — signal protocols, current ratings, mounting dimensions, and thermal limits. Teams that treat layer interfaces as first-class engineering artifacts consistently ship more reliable systems with fewer field returns.</p>'''),
}

for slug, section in EXPANSIONS.items():
    path = f'blog/{slug}/index.html'
    html = open(path, encoding='utf-8').read()
    if 'The Component Stack That Scales' in html or 'Signal Paths That Matter' in html or 'Where the Layers Meet' in html:
        print(f"ℹ️ {slug}: 已扩充")
        continue
    marker = '</article>'
    if marker not in html:
        print(f"⚠️ {slug}: 无</article>")
        continue
    html = html.replace(marker, '\n' + section + '\n' + marker, 1)
    open(path, 'w', encoding='utf-8').write(html)
    text = re.sub(r'<[^>]+>', ' ', html)
    print(f"✅ {slug}: 扩充后 {len(text.split())}词")

print("\n=== 验证 ===")
for slug in TARGETS + list(EXPANSIONS.keys()):
    html = open(f'blog/{slug}/index.html', encoding='utf-8').read()
    links = set(re.findall(r'href="/blog/([a-z0-9-]+)/"', html))
    links.discard(slug)
    text = re.sub(r'<[^>]+>', ' ', html)
    ok_links = '✅' if len(links) >= 5 else '❌'
    ok_words = '✅' if len(text.split()) >= 1000 else '❌'
    print(f"  {slug}: 内链{len(links)}{ok_links} 词数{len(text.split())}{ok_words}")
