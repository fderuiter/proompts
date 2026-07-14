---
title: Compassionate Music Therapy Workflow
---

# Compassionate Music Therapy Workflow

A 4-step workflow to deconstruct venting, plan a therapeutic arc, compose a musical blueprint, and write lyrics.

## Workflow Diagram

```mermaid
graph TD
    INPUT_venting_text([Input: venting_text])
    compassionate_analyst[compassionate_analyst<br><i>01_compassionate_analyst.prompt.md</i>]
    INPUT_venting_text -. venting_text .-> compassionate_analyst
    compassionate_analyst -->|sequential| iso_strategist
    iso_strategist[iso_strategist<br><i>02_iso_strategist.prompt.md</i>]
    compassionate_analyst -. psychological_profile .-> iso_strategist
    iso_strategist -->|sequential| sonic_architect
    sonic_architect[sonic_architect<br><i>03_sonic_architect.prompt.md</i>]
    compassionate_analyst -. psychological_profile .-> sonic_architect
    iso_strategist -. therapeutic_arc .-> sonic_architect
    sonic_architect -->|sequential| lyricist
    lyricist[lyricist<br><i>04_lyricist.prompt.md</i>]
    compassionate_analyst -. psychological_profile .-> lyricist
    iso_strategist -. therapeutic_arc .-> lyricist
    sonic_architect -. musical_blueprint .-> lyricist
```


