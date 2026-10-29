from pathlib import Path


def instructions():
    return (Path(__file__).resolve().parent.parent / 'skills/agent_role.md').read_text(encoding='utf8')
