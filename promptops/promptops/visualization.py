"""Module docstring."""
from promptops.validation import WorkflowSchema
from promptops.theme import ThemeSync

class MermaidGrapher:
    """Missing docstring."""
    @staticmethod
    def generate(wf: WorkflowSchema) -> str:
        """Missing docstring."""
        if not wf.steps and not wf.inputs:
            return ""
        
        graph = ["graph TD"]
        
        # Add high-contrast style classes
        graph.append(f"    {ThemeSync.get_step_node_class()}")
        graph.append(f"    {ThemeSync.get_input_node_class()}")
        
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
        graph.append(f"    {ThemeSync.get_edge_style()}")
                        
        return "\n".join(graph) if len(graph) > 1 else ""
