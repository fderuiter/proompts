---
layout: default
title: Compassionate Music Therapy Workflow
parent: Workflows
nav_order: 99
---

# Compassionate Music Therapy Workflow

A 4-step workflow to deconstruct venting, plan a therapeutic arc, compose a musical blueprint, and write lyrics.

## Workflow Diagram

```mermaid
graph TD
    Input_venting_text[Input: venting_text] --> Steps
    compassionate_analyst[Step: compassionate_analyst]
    Input_venting_text --> compassionate_analyst
    iso_strategist[Step: iso_strategist]
    compassionate_analyst --> iso_strategist
    sonic_architect[Step: sonic_architect]
    compassionate_analyst --> sonic_architect
    iso_strategist --> sonic_architect
    lyricist[Step: lyricist]
    compassionate_analyst --> lyricist
    iso_strategist --> lyricist
    sonic_architect --> lyricist
```

[View Source YAML](../workflows_src/clinical/music_therapy.workflow.yaml)
