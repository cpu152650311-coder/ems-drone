#!/usr/bin/env python3
"""Generate supplement image strategy JSON for new ems-drone pages."""
import json

images = []

# Sub-hero images for all new pages (21 unique sub-hero images)
pages = [
    ("factory", "factory/index.html"),
    ("quality", "quality/index.html"),
    ("shipping", "shipping/index.html"),
    ("faq", "faq/index.html"),
    ("how-it-works", "how-it-works/index.html"),
    ("design-guides", "design-guides/index.html"),
    ("projects", "projects/index.html"),
    ("quote", "quote/index.html"),
    ("capabilities", "capabilities/index.html"),
    ("capabilities-flight-control", "capabilities/flight-control/index.html"),
    ("capabilities-esc-power", "capabilities/esc-power/index.html"),
    ("capabilities-propulsion", "capabilities/propulsion/index.html"),
    ("capabilities-airframe", "capabilities/airframe/index.html"),
    ("capabilities-communications", "capabilities/communications/index.html"),
    ("capabilities-payload", "capabilities/payload/index.html"),
    ("industries", "industries/index.html"),
    ("industries-inspection", "industries/inspection/index.html"),
    ("industries-mapping-survey", "industries/mapping-survey/index.html"),
    ("industries-logistics", "industries/logistics/index.html"),
    ("industries-agriculture", "industries/agriculture/index.html"),
    ("industries-research", "industries/research/index.html"),
]

for img_id, page_path in pages:
    images.append({
        "id": f"sub-hero-{img_id}",
        "role": "sub-hero-bg",
        "page": page_path,
        "prompt": f"Professional B2B engineering photography style, UAV drone components and systems context, dark technical aesthetic with subtle acid green accent hints, industrial yet clean atmosphere, no people faces, no text, no logos, upper portion with space for title text overlay, abstract technology texture suitable as website page header background, 1024x1024",
    })

# Content images
content_images = [
    ("factory-bench", "factory/index.html", "product-showcase",
     "Professional UAV electronics test bench setup with oscilloscope, power supply, and flight controller mounted on anti-static mat, clean engineering workspace environment, dark technical aesthetic, no people, no text, no logos, professional B2B photography"),
    ("factory-integration", "factory/index.html", "concept-scene",
     "UAV drone mid-assembly on integration workbench, electronic components and tools laid out methodically, clean engineering workspace with organized parts trays, professional environment, no people faces, no text, no logos"),
    ("quality-equipment", "quality/index.html", "product-showcase",
     "Electronic test and measurement equipment for UAV component quality verification, oscilloscopes multimeters and signal analyzers arranged professionally, clean technical environment, dark aesthetic, no people, no text, no logos"),
    ("shipping-pack", "shipping/index.html", "concept-scene",
     "Professional export packaging for UAV components, ESD-safe anti-static packaging with foam inserts for electronic parts, shipping-ready crate with protective materials, clean logistics aesthetic, no text, no logos"),
    ("projects-inspection-drone", "projects/index.html", "concept-scene",
     "Industrial inspection hexacopter UAV conceptual visualization near infrastructure, thermal camera payload visible underneath, professional engineering photography context, dark moody atmosphere, no people faces, no text, no logos"),
    ("projects-agriculture-drone", "projects/index.html", "concept-scene",
     "Large agricultural spraying octocopter UAV conceptual visualization, tank and spray boom visible, over farmland at golden hour, professional engineering photography, no people faces, no text, no logos"),
    ("design-guide-fc", "design-guides/index.html", "technical-diagram",
     "Flight controller architecture decision flowchart concept, visual diagram showing processor sensor firmware selection paths, clean vector technical illustration style, dark background, no text labels, no logos"),
    ("design-guide-matching", "design-guides/index.html", "technical-diagram",
     "ESC and motor matching concept diagram showing voltage current propeller size relationships, clean engineering schematic style, dark background with subtle grid, no text labels, no logos"),
    ("cap-fc-detail", "capabilities/flight-control/index.html", "product-showcase",
     "Range of UAV flight controller boards displayed in a grid showing product diversity, different sizes and configurations, professional studio lighting on dark surface, no people, no text, no logos"),
    ("cap-esc-detail", "capabilities/esc-power/index.html", "product-showcase",
     "Range of UAV electronic speed controllers displayed showing product line diversity from small to large current ratings, professional studio lighting, dark technical background, no people, no text, no logos"),
    ("cap-propulsion-detail", "capabilities/propulsion/index.html", "product-showcase",
     "Range of UAV brushless motors in various sizes displayed alongside carbon fiber propellers, showing product diversity, professional studio arrangement on dark surface, no people, no text, no logos"),
    ("cap-airframe-detail", "capabilities/airframe/index.html", "concept-scene",
     "Carbon fiber UAV frame components displayed aesthetically, arms and center plates arranged artistically, professional engineering aesthetic, clean dark background with subtle reflection, no people, no text, no logos"),
    ("cap-comms-detail", "capabilities/communications/index.html", "product-showcase",
     "UAV radio telemetry modules and antennas displayed, communication hardware range from small receivers to long-range modules, professional studio lighting, dark technical background, no people, no text, no logos"),
    ("cap-payload-detail", "capabilities/payload/index.html", "product-showcase",
     "UAV camera payloads and 3-axis gimbals displayed, thermal camera RGB camera and multispectral sensor arranged professionally, dark studio background, no people, no text, no logos"),
    ("ind-inspection-detail", "industries/inspection/index.html", "concept-scene",
     "UAV drone inspecting industrial infrastructure conceptual visualization, bridge or power line inspection context, thermal camera payload visible, dramatic lighting, no people faces, no text, no logos"),
    ("ind-mapping-detail", "industries/mapping-survey/index.html", "concept-scene",
     "Fixed-wing mapping UAV conceptual visualization in flight over terrain, aerial survey context with photogrammetry camera, geospatial data theme, clean professional aesthetic, no people faces, no text, no logos"),
    ("ind-logistics-detail", "industries/logistics/index.html", "concept-scene",
     "Delivery UAV quadcopter with cargo package bay conceptual visualization, last-mile logistics context, approaching delivery point, professional engineering aesthetic, no people faces, no text, no logos"),
    ("ind-agriculture-detail", "industries/agriculture/index.html", "concept-scene",
     "Large agricultural spraying UAV octocopter over crop field conceptual visualization, spray tank visible, farming context with green fields below, professional photography, no people faces, no text, no logos"),
    ("ind-research-detail", "industries/research/index.html", "concept-scene",
     "Modular research UAV platform with customizable sensor bay conceptual visualization, interchangeable payload modules visible, clean laboratory aesthetic, no people faces, no text, no logos"),
    ("cta-engineering", "various", "cta-bg",
     "Abstract UAV engineering texture with subtle geometric patterns evoking circuit board traces and aerospace instrumentation, dark background with very subtle acid green highlights, low contrast suitable as CTA section background overlay, no text, no logos"),
    ("cta-systems", "various", "cta-bg",
     "Abstract drone systems architecture texture, subtle interconnected node patterns and geometric mesh, dark background with very subtle aero blue hints, low contrast for text overlay, no text, no logos"),
    ("texture-carbon", "various", "texture-bg",
     "Subtle abstract carbon fiber weave texture, very low contrast, dark monochromatic, suitable as card or section background overlay, almost invisible pattern, no text, no logos"),
    ("texture-circuit", "various", "texture-bg",
     "Very subtle abstract circuit board trace texture, extremely low contrast, dark monochromatic, aerospace instrumentation panel aesthetic, suitable as section background, barely visible, no text, no logos"),
    ("stats-drone-bg", "various", "stats-bg",
     "Abstract UAV and aerospace themed background with subtle geometric drone silhouette patterns, dark background, very subtle industrial texture, space for statistics text overlay, no logos, no text"),
    ("process-architecture", "how-it-works/index.html", "process-flow",
     "Abstract engineering process flow visualization from component to complete UAV system, sequential interconnected nodes, clean technical diagram style, dark background, no text labels, no logos"),
]

for img_id, page_path, role, prompt in content_images:
    images.append({
        "id": img_id,
        "role": role,
        "page": page_path,
        "prompt": prompt,
    })

output = {
    "images": images,
    "meta": {
        "total": len(images),
        "note": "Supplement images for ems-drone site completion — Phase S2",
        "referenceBaseUrl": "",
    }
}

with open("supplement-images.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"Created supplement-images.json with {len(images)} images")
