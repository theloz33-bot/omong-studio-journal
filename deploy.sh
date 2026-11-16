#!/usr/bin/env bash
# Build, audit, commit and push the journal. GitHub Pages redeploys in about a minute.
#   ./deploy.sh "Add post: consistent AI characters"
set -euo pipefail
cd "$(dirname "$0")"

python3 build.py --check
python3 tools/audit.py

git add -A
if git diff --cached --quiet; then
  echo "nothing to commit — docs/ already up to date"
  exit 0
fi
git commit -m "${1:-Update journal}"
git push origin HEAD:main
echo "pushed. check the live site in a minute: https://theloz33-bot.github.io/omong-studio-journal/"
