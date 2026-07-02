import argparse
import sys
from promptops.validation import validate_prompts
from promptops.simulation import simulate_prompt
from promptops.documentation import generate_docs
from promptops.init import init_project
from promptops.agent import generate_config, discovery_report

def main():
    parser = argparse.ArgumentParser(description="PromptOps Toolkit CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Init
    init_parser = subparsers.add_parser("init", help="Initialize PromptOps in the current repository")

    # Validate
    validate_parser = subparsers.add_parser("validate", help="Validate prompt files")
    validate_parser.add_argument("--dir", help="Directory containing prompts", default=".")
    validate_parser.add_argument("--strict", action="store_true", help="Enable strict validation")

    # Simulate
    simulate_parser = subparsers.add_parser("simulate", help="Simulate a prompt")
    simulate_parser.add_argument("file", nargs="?", help="Path to prompt file")
    simulate_parser.add_argument("-f", "--file", dest="file_flag", help="Path to prompt file (alias)")
    simulate_parser.add_argument("-i", "--data", dest="data", help="Path to JSON/YAML file with mock data", required=True)
    simulate_parser.add_argument("--strict", action="store_true", help="Enable strict validation")
    simulate_parser.add_argument("--chaos", action="store_true", help="Enable chaos mode")
    simulate_parser.add_argument("-v", "--verbose", action="store_true", help="Increase verbosity")
    simulate_parser.add_argument("--json", action="store_true", help="Enable JSON output mode")
    simulate_parser.add_argument("--no-color", action="store_true", help="Disable colored output")

    # Docs
    docs_parser = subparsers.add_parser("docs", help="Generate prompt documentation")
    docs_parser.add_argument("--dir", help="Directory containing prompts", default=".")
    docs_parser.add_argument("--out", help="Output directory for documentation", default="docs")
    docs_parser.add_argument("--repo-url", help="Base URL for source repository", default="")
    docs_parser.add_argument("--branch", help="Branch name for source repository links", default="main")

    # Agent
    agent_parser = subparsers.add_parser("agent", help="Agent configuration and discovery")
    agent_subparsers = agent_parser.add_subparsers(dest="agent_command", required=True)
    
    agent_config = agent_subparsers.add_parser("config", help="Generate MCP configuration for agent clients")
    agent_config.add_argument("--dir", help="Directory containing prompts", default="prompts")
    
    agent_discovery = agent_subparsers.add_parser("discovery", help="Show tool discovery and override report")
    agent_discovery.add_argument("--dir", help="Directory containing prompts", default="prompts")

    # Vibe
    vibe_parser = subparsers.add_parser("vibe", help="Run full-fidelity vibe audit")
    vibe_parser.add_argument("--budget-cap", type=float, default=10.0, help="Maximum budget for LLM API calls")
    vibe_parser.add_argument("--coverage", type=str, default="universal", help="Coverage mode")

    args = parser.parse_args()

    if args.command == "init":
        init_project()
    elif args.command == "validate":
        success = validate_prompts(args.dir, strict=args.strict)
        sys.exit(0 if success else 1)
    elif args.command == "simulate":
        target_file = args.file_flag or args.file
        if not target_file:
            simulate_parser.error("Prompt file must be provided either as a positional argument or via -f/--file")
            
        import logging
        if args.verbose:
            logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
            logging.getLogger().setLevel(logging.DEBUG)
        else:
            logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
            logging.getLogger().setLevel(logging.WARNING)
            
        from promptops.console import set_json_mode, set_no_color
        set_json_mode(args.json)
        set_no_color(args.no_color)
            
        success = simulate_prompt(target_file, args.data, chaos_mode=args.chaos, strict_mode=args.strict)
        sys.exit(0 if success else 1)
    elif args.command == "docs":
        generate_docs(args.dir, args.out, args.repo_url, args.branch)
        sys.exit(0)
    elif args.command == "agent":
        if args.agent_command == "config":
            generate_config(args.dir)
        elif args.agent_command == "discovery":
            discovery_report(args.dir)
    elif args.command == "vibe":
        from promptops.vibe import run_vibe_audit
        run_vibe_audit(budget_cap=args.budget_cap, coverage=args.coverage)
        sys.exit(0)  # Non-blocking execution

if __name__ == "__main__":
    main()
