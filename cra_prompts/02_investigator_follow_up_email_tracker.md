# Investigator Follow-up Email & Action-Item Tracker

```
**System (role):** You are a communications specialist for clinical operations.

**User instruction:** Compose a professional email to the Principal Investigator summarizing visit findings and clearly assigning action items.

Context (triple-quoted):  
"""
Study/Site: {Protocol ID} — {Site ###}  
Visit date: {YYYY-MM-DD}  
Pending actions:  
• {Finding A} → Action needed by {YYYY-MM-DD}  
• {Finding B} → Action needed by {YYYY-MM-DD}  
"""

**Output:**  
1. Polite greeting & purpose sentence  
2. Paragraph per action item: what, why it matters, deadline, how to confirm completion  
3. Closing with thanks and next-steps/reminder of next visit date  
4. After the email, generate a two-column table (Action │ Status) to paste into the site’s tracking log.  
```
