# Hearth & Code · Fieldcraft

Practical techniques for thinking, building and creating with AI. One technique, a working example, and a visible result.

Initial design preview: https://hearthandcode.github.io/fieldcraft/

## Run locally

Python 3.10+ and Node.js 18+:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
node examples/check.test.mjs
python scripts/build.py
python -m http.server 4173 --directory site
```

Open http://localhost:4173. The first article includes an interactive capacity/uniqueness check. It uses the same pure function as the executable tests. No backend, model provider, tracking, or third-party font requests.

## Content ownership

Article masters live in the private Hearth & Code Knowledge Hub. `content/` contains explicitly selected public projections, not the full source corpus. `publication.json` records source and exported digests. Edit the master and run `python scripts/export_article.py /explicit/path/to/allowlisted/master.md`, then rebuild. New articles need an explicit allowlist entry and publication review. The build rejects drift from the exported digest.

The first article and visual direction are design previews. A publication is not a verification seal. Its mathematical expression is a pedagogical model, not normative ESS notation. Planned collection entries are not published articles.

## Presentation

Ember Circuit palette adapted from the existing Hearth & Code public site: charcoal, parchment, copper, gold, violet and cyan. Original inline circuit illustration. System fonts; native MathML. Index structure inspired by [Hermes Wingtips](https://notwitcheer.github.io/hermes-recipes/wingtips/); no article text or visual assets copied.

## Publication

The Pages workflow builds only the released public snapshot. `site/` is generated and ignored by Git. A faulty release is corrected with a new commit and redeployment; the source master retains its history.

No license grant is implied by public visibility. License selection remains with Hearth & Code.
