#!/usr/bin/env bash
set -euo pipefail

if [[ ! -x "$(dirname "$0")/verify-local.sh" ]]; then
  printf '%s\n' 'ERROR: missing executable scripts/verify-local.sh.' >&2
  printf '%s\n' 'Repository owner must supply real project checks; verification is NOT green.' >&2
  exit 2
fi

exec "$(dirname "$0")/verify-local.sh"
