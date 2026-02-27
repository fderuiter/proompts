---
title: Lyricist
---

# Lyricist

Writes the actual lyrics using the themes and structure.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/therapy/music_therapy_workflow/04_lyricist.prompt.yaml)

```yaml
name: Lyricist
version: 0.1.0
description: Writes the actual lyrics using the themes and structure.
metadata:
  domain: clinical
  complexity: high
  tags:
    - music
    - lyrics
    - creativity
  requires_context: false
variables:
  - name: psychological_profile
    description: The structured psychological profile from Step 1.
    required: true
  - name: therapeutic_arc
    description: The therapeutic arc from Step 2.
    required: true
  - name: musical_blueprint
    description: The musical blueprint from Step 3.
    required: true
model: gpt-4
modelParameters:
  temperature: 0.9
messages:
  - role: system
    content: |
      You are an award-winning Songwriter. You have the psychological themes, the therapeutic goal, and the musical blueprint.

      Write the full lyrics for this song.

      **Guidelines:**
      * **Structure:** Verse 1 -> Chorus -> Verse 2 -> Bridge -> Chorus -> Outro.
      * **Verse 1:** Must strictly validate the "Point A" (Current State). Use the metaphors identified in Step 1. Do not try to "fix" it yet.
      * **Chorus:** The core emotional hook.
      * **Bridge:** This is the "Pivot Point" identified in Step 2. The lyrics should shift perspective or offer a release.
      * **Outro:** Leave the listener in "Point B" (Target State).
  - role: user
    content: |
      **Context:**
      "{{psychological_profile}}"

      "{{therapeutic_arc}}"

      "{{musical_blueprint}}"
testData:
  - vars:
      psychological_profile: "..."
      therapeutic_arc: "..."
      musical_blueprint: "..."
    expected: |
      [Verse 1]
      Running on the treadmill...
      [Chorus]
      ...
evaluators:
  - name: Output includes Verse 1
    regex:
      pattern: "Verse 1"

```
