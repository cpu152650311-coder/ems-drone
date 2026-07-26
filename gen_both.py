#!/usr/bin/env python3
"""Generate images for build-vs-buy and supply-chain-layers rewrites."""
import os, base64, subprocess, time, sys
from openai import OpenAI

client = OpenAI(api_key=os.environ["AIHUBMIX_API_KEY"], base_url="https://aihubmix.com/v1")
OUT = "/home/ubuntu/projects/ems-drone/generated"

images = [
    # --- BUILD VS BUY (4 images) ---
    ("blog-inline-buildbuy-components.webp",
     "Professional product photography. Wide shot of an engineering workbench with individual UAV components spread out: a flight controller PCB, four brushless motors, four ESCs, carbon fiber frame arms, a LiPo battery, and radio receiver. Industrial lighting, dark workshop background, sharp focus on components, metallic and matte textures visible. No text, no watermarks, no logos."),

    ("blog-inline-buildbuy-subsystem.webp",
     "Professional product photography. Close-up of a pre-assembled UAV propulsion subsystem: flight controller PCB, four ESCs, and four brushless motors connected together with neat wiring harness, sitting on a dark anti-static mat. The components form a coherent stack with clean cable management. Industrial lab lighting, sharp focus. No text, no watermarks, no logos."),

    ("blog-inline-buildbuy-decision.webp",
     "Abstract conceptual illustration. A minimalist decision framework shown as a branching tree or flowchart made of glowing neon green lines on a dark charcoal background. Three paths branch out from a central node, each labeled with simple icons: a single gear (individual components), three connected gears (subsystem), a complete circle (full aircraft). Clean geometric style, no text, no labels. Dark theme with green accent (#b8f34a)."),

    ("blog-cta-buildbuy.webp",
     "Abstract dark background image for a B2B call-to-action section. Dark charcoal (#1a1a2e) gradient with subtle neon green (#b8f34a) geometric accents — thin diagonal lines and circuit-like traces. Minimalist, elegant, no text, no logos. Professional corporate feel for an engineering/aviation company."),

    # --- SUPPLY CHAIN LAYERS (4 images) ---
    ("blog-inline-supplychain-layers.webp",
     "Abstract conceptual illustration. Four horizontal stacked layers visualized as semi-transparent planes with neon green (#b8f34a) borders on a dark charcoal background. Each layer has a subtle icon: brain/circuit (control layer at top), lightning bolt (power layer second), propeller (motion layer third), and antenna/satellite dish (mission layer at bottom). Thin glowing connection lines between layers. Dark theme, professional, clean geometric style. No text labels."),

    ("blog-inline-supplychain-interfaces.webp",
     "Professional macro product photography. Close-up of UAV electronic connectors and interface points: JST-GH, XT60, and Molex connectors, ribbon cables, solder joints on a PCB, pin headers. Sharp detail on metallic pins and plastic housings. Dark background, industrial lighting, shallow depth of field emphasizing the precision engineering. No text, no watermarks."),

    ("blog-inline-supplychain-integration.webp",
     "Professional product photography. A fully integrated UAV multirotor on a workshop bench, all layers connected and functioning: flight controller with clean wiring to ESCs and motors, radio antenna mounted, payload camera/gimbal attached underneath, battery connected. The drone is fully assembled and powered on, with a subtle LED indicator glow. Dark industrial background. No text, no watermarks, no logos."),

    ("blog-cta-supplychain.webp",
     "Abstract dark background image for a B2B call-to-action section. Dark charcoal (#1a1a2e) background with subtle neon green (#b8f34a) layered geometric patterns — overlapping translucent circles suggesting interconnected layers. Minimalist, elegant, no text, no logos. Professional corporate feel for an engineering/supply chain company."),
]

for fname, prompt in images:
    out_path = os.path.join(OUT, fname)
    if os.path.exists(out_path):
        size = os.path.getsize(out_path)
        print(f"SKIP {fname} (exists, {size:,} bytes)")
        continue

    print(f"GEN {fname} ...", end=" ", flush=True)
    try:
        resp = client.images.generate(model="gpt-image-2", prompt=prompt, n=1, size="1024x1024", quality="low")
        raw = base64.b64decode(resp.data[0].b64_json)
        # Convert to webp
        tmp = out_path + ".tmp.png"
        with open(tmp, "wb") as f:
            f.write(raw)
        subprocess.run(["cwebp", "-q", "75", "-m", "6", tmp, "-o", out_path], check=True, capture_output=True)
        os.remove(tmp)
        size = os.path.getsize(out_path)
        print(f"DONE ({size:,} bytes)")
    except Exception as e:
        print(f"FAIL: {e}")
        continue

    time.sleep(1)  # rate limit

print("\nAll images generated.")
# Verify
for fname, _ in images:
    p = os.path.join(OUT, fname)
    if os.path.exists(p):
        print(f"  {fname}: {os.path.getsize(p):,} bytes")
    else:
        print(f"  {fname}: MISSING")
