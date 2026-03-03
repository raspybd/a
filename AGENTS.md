# AGENTS.md

## Cursor Cloud specific instructions

This is a **Microsoft MakeCode (PXT) extension** for the BBC micro:bit. There is only one service — the PXT local dev server.

### Key commands

| Action | Command |
|--------|---------|
| Build | `pxt build` (or `make build`) |
| Test | `pxt test` (or `make test`) |
| Dev server | `pxt serve --no-browser --port 3232` |

### Non-obvious caveats

- **No `package.json`**: Dependencies are managed via `pxt.json`, not npm. The `node_modules/` directory is created by `pxt target microbit`, not `npm install`.
- **`pxt target microbit`** must be run once before `pxt install` or `pxt build`. It downloads the full `pxt-microbit` and `pxt-core` packages into `node_modules/`.
- **`pxt serve` build warning**: `pxt serve` emits a non-fatal `ENOENT: no such file or directory, scandir 'libs'` error during its internal target rebuild. This does not prevent the server from starting or the editor from working.
- **Lint**: There is no separate lint command. TypeScript compilation via `pxt build` is the primary code-quality check.
- **The dev server** listens on the port specified (default 3232) and opens the MakeCode block editor with a built-in micro:bit simulator — no physical device needed for development.
