from promptops.validation import WorkflowSchema

class MermaidGrapher:
    @staticmethod
    def generate(wf: WorkflowSchema) -> str:
        if not wf.steps and not wf.inputs:
            return ""
        
        graph = ["graph TD"]
        
        # Add high-contrast style classes
        graph.append("    classDef stepNode fill:#1a5f7a,stroke:#0d3a4d,stroke-width:2px,color:#ffffff;")
        graph.append("    classDef inputNode fill:#2c5e43,stroke:#183b27,stroke-width:2px,color:#ffffff;")
        
        # Add inputs
        for inp in wf.inputs:
            graph.append(f"    INPUT_{inp.name}([Input: {inp.name}]):::inputNode")
            
        # Add steps and edges
        for step in wf.steps:
            step_id = step.step_id
            p_file = step.prompt_file.split('/')[-1]
            graph.append(f"    {step_id}[{step_id}<br><i>{p_file}</i>]:::stepNode")
            
            # Map inputs (Data flow)
            for var_name, input_val in step.map_inputs.items():
                if isinstance(input_val, str) and input_val.startswith('{{') and input_val.endswith('}}'):
                    inner = input_val[2:-2].strip()
                    if inner.startswith('steps.'):
                        parts = inner.split('.')
                        if len(parts) >= 2:
                            source_step = parts[1]
                            graph.append(f"    {source_step} -. {var_name} .-> {step_id}")
                    elif inner.startswith('inputs.'):
                        parts = inner.split('.')
                        if len(parts) >= 2:
                            source_input = parts[1]
                            graph.append(f"    INPUT_{source_input} -. {var_name} .-> {step_id}")
                            
            # Next (Control flow)
            if step.next:
                next_edges = step.next if isinstance(step.next, list) else [step.next]
                for nxt in next_edges:
                    if isinstance(nxt, str):
                        graph.append(f"    {step_id} -->|unconditional| {nxt}")
                    else: # WorkflowEdge
                        target = nxt.target
                        cond = "conditional" if nxt.condition else "unconditional"
                        graph.append(f"    {step_id} -->|{cond}| {target}")
            else:
                # Implicit sequential transition to next step
                step_idx = wf.steps.index(step)
                if step_idx + 1 < len(wf.steps):
                    next_step = wf.steps[step_idx + 1]
                    graph.append(f"    {step_id} -->|sequential| {next_step.step_id}")
        
        # Add default link style
        graph.append("    linkStyle default stroke:#767676,stroke-width:2px;")
                        
        return "\n".join(graph) if len(graph) > 1 else ""
