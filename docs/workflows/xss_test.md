---
layout: default
title: &lt;script&gt;alert(&#x27;title_xss&#x27;)&lt;/script&gt;
parent: Workflows
nav_order: 99
---

# &lt;script&gt;alert(&#x27;title_xss&#x27;)&lt;/script&gt;

&lt;script&gt;alert(&#x27;desc_xss&#x27;)&lt;/script&gt;

## Workflow Diagram\n\n<div class="mermaid">\ngraph TD
    _img_src_x_onerror_alert__step_id_xss___[Step: &lt;img src=x onerror=alert(&#x27;step_id_xss&#x27;)&gt;]\n</div>\n
[View Source YAML](../../workflows/test/xss_test.workflow.yaml)
