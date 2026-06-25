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
    simulate_parser.add_argument("file", help="Path to prompt file")
    simulate_parser.add_argument("--data", help="Path to JSON/YAML file with mock data", required=True)

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

    args = parser.parse_args()

    if args.command == "init":
        init_project()
    elif args.command == "validate":
        success = validate_prompts(args.dir, strict=args.strict)
        sys.exit(0 if success else 1)
    elif args.command == "simulate":
        success = simulate_prompt(args.file, args.data)
        sys.exit(0 if success else 1)
    elif args.command == "docs":
        generate_docs(args.dir, args.out, args.repo_url, args.branch)
        sys.exit(0)
    elif args.command == "agent":
        if args.agent_command == "config":
            generate_config(args.dir)
        elif args.agent_command == "discovery":
            discovery_report(args.dir)

if __name__ == "__main__":
    main()
