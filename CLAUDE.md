# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A data repository of flashcard decks for [youyin](https://youyin.madladsquad.com/). There is no app code here: just deck JSON files plus two Python scripts that CI runs to sanitize the decks and build the index the website reads. Merged decks show up on the site's packages/marketplace page.

## Commands

Both scripts take no arguments and must be run from the repo root (they use relative paths). Neither needs anything beyond the Python standard library.

```sh
./sanitize-decks.py            # rewrites deck files in place (see below)
./generate-marketplace-map.py  # regenerates marketplace-map.json
```

There are no tests, linters or build steps. To check a deck change, run both scripts and inspect `git diff`.

## Pipeline (`.github/workflows/ci.yaml`)

On every push to `master` and four times a day, CI:
1. Runs `sanitize-decks.py` then `generate-marketplace-map.py`.
2. Commits any changes as "Sanitize files" (GPG-signed bot commit) and pushes to `master`.
3. Uploads `official/`, `unofficial/` and `marketplace-map.json` to the Cloudflare R2 bucket `youyin-data`, which is where the website reads them from.

Because CI rewrites files and commits back to `master`, pull before pushing. `marketplace-map.json` is generated output: regenerate it with the script instead of editing it by hand.

## Deck format

Files are named `<Name-With-Dashes>.yydeck.json`. Dashes become spaces in the marketplace display name. A `.presetlvl.yydeck.json` suffix marks a deck whose `knowledge` levels are kept on purpose.

```json
{
  "cards":   [{"name": "yī", "character": "一", "knowledge": 0, "definitions": ["one"], "variant": ""}],
  "phrases": [{"name": "bà ba", "phrase": "爸爸", "knowledge": 0, "definitions": ["(coll.) father; dad"]}]
}
```

Decks live exactly one folder deep under a category: `official/<Language>/` (maintainer decks) or `unofficial/<Language>/` (community decks).

## Script behavior to know about

- **`sanitize-decks.py`** only looks at `<base>/<subfolder>/*.yydeck.json` for `base` in `./official/` and `./community/`. It replaces `<`/`>` with `&lt`/`&gt` (no semicolon) across the whole file, then sets every card's and phrase's `knowledge` to `0` unless the file is `.presetlvl`. It re-writes the JSON with `json.dump` defaults, so files end up on one line with non-ASCII characters `\u`-escaped.
- **`generate-marketplace-map.py`** walks the whole repo, skipping dot-directories. It writes minified JSON shaped like `{"official": [{<subfolder>: [deck, ...]}], "unofficial": [{...}]}`, with decks sorted by filename and subfolders sorted by key. Each entry records `name`, `cards`/`phrases` counts, `preset_levels`, and `location` (filename only). Anything outside `official/` goes under `"unofficial"`. A `community/` prefix is stripped from the subfolder key, but an `unofficial/` prefix is not, so a deck at `unofficial/Chinese/X.yydeck.json` gets the key `"unofficial/Chinese"`, not `"Chinese"`.

## Folder naming mismatch

The README tells contributors to put decks under `community/<Language>/`, but the repo only has `unofficial/` (holding just a `.gitkeep`), and CI uploads `unofficial/`, not `community/`. As a result:
- decks placed in `community/` are sanitized and listed in the map, but never uploaded to R2;
- decks placed in `unofficial/` are uploaded, but not sanitized, and get a prefixed key in the map.

Keep this in mind when moving community decks or changing either script, and fix all three places (README, scripts, CI) together.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- When graphify-out/graph.json exists, run `graphify query "<question>"` before your first grep, search or source-file read for a codebase question, and put this rule in every subagent prompt that explores code. Read raw files only for lines the graph or an earlier read already located. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
- A committed graphify-out/graph.json is rewritten whole on every build, so a large diff to it in a pull request is expected. Do not flag it as churn or suggest skipping the graph rebuild or its hooks.
