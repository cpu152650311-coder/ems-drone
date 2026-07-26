# Image Prompt Improvement Guide for EMS Drone

## Root Cause of Current Issues

### Problem 1: Empty tops on sub-hero images
GPT Image 2 naturally centers subjects in the 1024×1024 frame, leaving 20-35% empty sky/ceiling at the top.
The CSS `object-position: center 60%` (changed from 32%) now shows the subject area, but the images
still have wasted space that could be used for content.

**The prompt didn't instruct otherwise.** Without explicit framing direction, AI fills the top with background.

### Problem 2: All sub-hero images look similar
Prompts used formulaic "Conceptual {topic} visualization, professional B2B photography" patterns.
When 30+ images share the same compositional template, they converge on the same visual language:
workbench with components, desk with drone parts, industrial interior with equipment.

## Prompt Fixes for Future Regeneration

### Rule 1: Kill the empty top — mandatory line for ALL prompts
Append this to EVERY image prompt:
```
Tight composition filling the entire frame edge to edge, no empty sky or ceiling,
no wasted space at top or bottom, subject occupies the full square canvas.
```

### Rule 2: Vary composition angles across pages
Assign each page ONE of these angles (rotate through them, don't repeat adjacent pages):

| Angle | Prompt keywords | Best for |
|-------|----------------|----------|
| **Low angle / worm's eye** | "shot from below looking up, dramatic upward perspective" | Capabilities, factory, testing |
| **High angle / bird's eye** | "overhead flat lay, top-down view, components arranged on surface" | Industries, components, design guides |
| **Macro close-up** | "extreme close-up, shallow depth of field, filling the frame, macro detail" | Quality, testing, customization |
| **Dutch / dynamic angle** | "slightly tilted dynamic angle, 15-degree dutch tilt, sense of motion" | Propulsion, shipping, logistics |
| **Eye-level immersive** | "eye-level perspective, as if standing in the space, immersive wide angle" | About, factory, contact |
| **Split / diptych** | "split composition showing both sides, before/after or component/system" | How it works, design guides, projects |
| **Through-object frame** | "shot through a foreground element, depth layering, framed by equipment" | Quality, factory, testing |

### Rule 3: Category-specific composition rules

#### Sub-hero images (`.sub-hero-media img` — ultrawide container)
- **CRITICAL**: Subject MUST be in the lower 60% of the frame (bottom-weighted composition)
- Crop point is `center 60%` — if subject is above this line, it will be invisible
- Best composition: subject fills bottom 2/3, with subtle context (not empty sky) in top 1/3
- Prompt MUST include: "bottom-weighted composition, main subject occupies lower two-thirds of frame"

#### Media-visual images (`.media-visual img` — 4:3 container)  
- Center-weighted composition works best
- Subject should fill the central 70% of frame
- Avoid edge details — they get cropped at 4:3

#### Hero image (`hero-bg` — full-width atmosphere)
- Atmospheric rather than subject-focused
- Must work with dark text overlay on left side
- Keep the right 40% visually interesting (where no text overlay)
- Bottom-weighted for `object-position: center 55%`

### Rule 4: Eliminate "Conceptual" from prompts
Instead of "Conceptual visualization of X", use concrete descriptions:
- ❌ "Conceptual UAV logistics warehouse"
- ✅ "A busy UAV logistics warehouse with drones on charging racks, packages on conveyor belts, staff at terminals. Shot from eye level, wide angle. Tight composition, no empty ceiling."

### Rule 5: Add differentiation keywords per page
Each image prompt must include 2-3 unique visual elements that distinguish it:
- Color accents specific to the topic
- Unique props (test equipment, shipping crates, carbon fiber, antennas)
- Different lighting (warm warehouse, cool lab, golden hour outdoor, neon accent)

## Example: Before/After Prompts

### sub-hero-industries-logistics.webp
**Before (likely):**
"Conceptual visualization of UAV logistics and delivery operations, professional B2B photography style"

**After (recommended):**
"Low-angle shot inside a drone delivery hub. Packages being loaded onto a quadcopter, conveyor belt in background, warehouse racking with drone parts. Warm industrial lighting. Bottom-weighted composition — main action fills lower two-thirds of frame, no empty ceiling. Tight composition filling entire square canvas edge to edge."

### sub-hero-capabilities-flight-control.webp  
**Before (likely):**
"Conceptual flight controller PCB visualization, professional B2B photography"

**After (recommended):**
"Extreme macro close-up of a flight controller PCB. Gold-plated IMU sensor in sharp focus, surrounding capacitors and pin headers slightly blurred for depth. Green PCB with visible trace routing. Shot at 45-degree angle with dramatic side lighting. Tight composition — PCB fills the entire frame, no wasted space."

## Priority for Regeneration

When regenerating images, fix in this order:
1. Sub-hero images (most visible, most problematic) — all 30+
2. `capabilities-overview-grid.webp` (flat lay needs 1:1 composition)
3. `industries-application-collage.webp` (similar empty-top risk)
4. Hero and CTA images (less critical, atmosphere works)
