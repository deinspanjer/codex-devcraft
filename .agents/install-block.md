# The canonical install block

One install story, one wording. `README.md` and every page under `docs/` must say this and nothing else. Change it here first, then propagate.

## Codex marketplace

Add the marketplace, then install the plugin:

<canonical-block name="codex-marketplace-install">

```bash
codex plugin marketplace add deinspanjer/codex-devcraft
codex plugin add codex-devcraft@codex-devcraft
```

Start a new Codex task after installation so the bundled skills are available.

</canonical-block>

Docs pages do not repeat these commands; link readers to the repository installation section.
