#!/bin/bash
set -euo pipefail

# Thin wrapper around carbon-now-cli for this repo's documentation
# screenshots: skips the popup and names the output after the input file.
# All other flags pass straight through — see:
# https://www.npmjs.com/package/carbon-now-cli#usage
#
# Usage:
#   ./carbon-screenshot.sh <file> [carbon-now-cli flags...]
#
# Examples:
#   ./carbon-screenshot.sh curl-test.sh --settings '{"lineNumbers":true}'
#   ./carbon-screenshot.sh session.txt

if [ $# -lt 1 ]; then
  echo "Usage: $0 <file> [carbon-now-cli flags...]" >&2
  exit 1
fi

FILE="$1"
shift

npx --yes carbon-now-cli "$FILE" \
  --save-as "$(basename "${FILE%.*}")" \
  --skip-display \
  "$@"
