# 🧪 RepoMind Happy-Path Test Repo

This is a deliberate test repository for validating [RepoMind V2](https://github.com/aashishkumar-tech7/RepoMind) — an autonomous AI agent swarm that detects CI failures and opens auto-fix PRs.

## 🎯 Purpose

Used to demonstrate the **happy-path flow**:

1. Developer pushes broken code (e.g., `import nonexistent_package`)
2. GitHub Actions CI fails
3. **RepoMind** webhook receives the failure
4. AI agent swarm:
   - 🔍 **Triage** classifies the failure
   - 🛠️ **Solver** generates a code fix
   - 🛡️ **Policy Gate** validates the change
   - 📝 **PR Creator** opens a fix PR
5. Developer approves the PR
6. **RepoMind** auto-merges + sends confirmation email

## 📦 What's in here

- `src/calculator.py` — A toy calculator module
- `tests/test_calculator.py` — Pytest test suite
- `.github/workflows/ci.yml` — CI pipeline
- `.repomind.yml` — RepoMind configuration

## 🚀 How to run locally

```bash
pip install -r requirements.txt
pytest -v
```

## 🧪 How to trigger a RepoMind test

Push any breaking change to a new branch — e.g., add a bad import to `src/calculator.py`:

```python
import nonexistent_package_xyz_12345
```

Then watch your email + GitHub PRs for RepoMind's auto-fix.

## 📜 License

MIT
