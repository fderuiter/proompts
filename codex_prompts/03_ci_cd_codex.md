# Continuous Integration & Delivery (OpenAI Codex)
## Goal
Generate GitHub Actions workflows that build, test, version, and deploy the app (often a containerised service that calls the OpenAI API).
## Context / Background
- Tooling & tests are in place.  
- Deployment targets could be Vercel, AWS ECS/Fargate, Fly.io, or plain Docker Compose on a VM.  
- Secrets will include `OPENAI_API_KEY`.
## Instructions
**Ask the caller**:
1. Environments (dev / staging / prod).  
1. Deployment platform and region.  
1. Secret-management preference (GitHub Encrypted Secrets, AWS Secrets Manager, Vault…).  
1. Versioning scheme (SemVer via `release-please`, CalVer, etc.).  
Then scaffold:
- `ci.yml` → lint + test + build.  
- `release.yml` → auto-tag & changelog.  
- `deploy-<env>.yml` files → fetch artifact, deploy, smoke-test endpoint that internally calls OpenAI with `echo` prompt “ping”.  
- Docs in `docs/deploy.md` describing how to add secrets.
Return all workflow YAML and any helper shell scripts as code blocks.
## References
- [CI/CD Best Practices](../docs/devops/ci-cd.md)
## Additional Notes
- Cache deps with `actions/cache@v4`.  
- Matrix test on multiple Node/Python versions if applicable.
## Example Usage
> Paste this prompt into ChatGPT after quality tooling is merged, answer the four questions, then commit the generated `.github/workflows/*`.
