# Triage Labels

The skills speak in terms of five canonical triage roles. This file maps those roles to the actual label strings used in this repo's issue tracker.

| Label in mattpocock/skills | Label in our tracker | Meaning                                  |
| -------------------------- | -------------------- | ---------------------------------------- |
| `needs-triage`             | `needs-triage`       | Maintainer needs to evaluate this issue  |
| `needs-info`               | `needs-info`         | Waiting on reporter for more information |
| `ready-for-agent`          | `ready-for-agent`    | Fully specified, ready for an AFK agent  |
| `ready-for-human`          | `ready-for-human`    | Requires human implementation            |
| `wontfix`                  | `wontfix`            | Will not be actioned                     |

When a skill mentions a role, use the corresponding label string from this table.

Edit the right-hand column to match whatever vocabulary the issue tracker actually uses.

## Bootstrap GitHub Labels

After the repo exists on GitHub and `gh` is authenticated, this command creates the default labels if they do not already exist:

```bash
gh label create needs-triage --description "Maintainer needs to evaluate this issue" --color D4C5F9
gh label create needs-info --description "Waiting on reporter for more information" --color FEF2C0
gh label create ready-for-agent --description "Fully specified, ready for an AFK agent" --color 0E8A16
gh label create ready-for-human --description "Requires human implementation" --color 1D76DB
gh label create wontfix --description "Will not be actioned" --color C5DEF5
```

If a label already exists, `gh` exits non-zero for that label. In that case, either leave the existing label as-is or update it manually in GitHub.
