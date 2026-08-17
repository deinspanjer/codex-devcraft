Installable skills live directly under `plugins/codex-devcraft/skills/`. Their catalog categories are recorded in `skills/engineering/README.md` and `skills/productivity/README.md`.

Non-promoted skills remain under `skills/misc/`, `skills/in-progress/`, and `skills/deprecated/`; they must not ship in the plugin or appear in the top-level `README.md`.

Install commands are copied verbatim from [.agents/install-block.md](./.agents/install-block.md). This repository targets Codex only.

Each skill entry in the top-level `README.md` must link the skill name to its `SKILL.md`.

The engineering and productivity catalog pages and the top-level `README.md` group entries into **User-invoked** and **Model-invoked**. Non-promoted bucket pages use a flat list.

Promoted skills also have a human-facing page at `docs/<category>/<skill-name>.md`. The published URL is `https://aihero.dev/skills-<skill-name>` regardless of category. When you add, rename, or change a promoted skill, create or re-sync its page following [.agents/writing-docs.md](./.agents/writing-docs.md). Non-promoted skills get no docs page.

Every `SKILL.md` is either user-invoked (`policy.allow_implicit_invocation: false` in `agents/openai.yaml`, reachable only through explicit `$skill-name` invocation) or model-invoked (model- or user-reachable). See [.agents/invocation.md](./.agents/invocation.md).

[`ask-devcraft`](./plugins/codex-devcraft/skills/ask-devcraft/SKILL.md) is the router that maps every user-reachable skill and how they relate. The same trigger that re-syncs a docs page applies to it: whenever you add, rename, remove, or change how a user-reachable skill fits the flows, re-read `ask-devcraft`'s `SKILL.md` and update it so the map stays accurate — a new skill it never mentions, or a stale one it still routes to, is a router that lies.

The Codex plugin manifest is `plugins/codex-devcraft/.codex-plugin/plugin.json`; the repo marketplace is `.agents/plugins/marketplace.json`. Keep the plugin and package versions aligned, and run the plugin validator after changing the manifest or installable skill layout.

Maintainers can run `scripts/link-skills.sh` to link the installable skills into `~/.agents/skills` for local development. This is not the user install path.
