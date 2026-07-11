#!/bin/bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:5000}"
STAMP="$RANDOM$RANDOM"
NAME="Curl Test $STAMP"
EMAIL="curl-test-$STAMP@example.com"
CONTENT="Automated curl test post $STAMP"

json_field() {
  python3 -c "import json,sys; print(json.load(sys.stdin)[sys.argv[1]])" "$1"
}

echo "==> POST /api/timeline_post"
CREATE_RESPONSE=$(curl -s -X POST "$BASE_URL/api/timeline_post" \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"$NAME\", \"email\": \"$EMAIL\", \"content\": \"$CONTENT\"}")
echo "$CREATE_RESPONSE"

POST_ID=$(echo "$CREATE_RESPONSE" | json_field id)
echo "Created post id=$POST_ID"

echo "==> GET /api/timeline_post"
LIST_RESPONSE=$(curl -s "$BASE_URL/api/timeline_post")
if echo "$LIST_RESPONSE" | grep -q "$CONTENT"; then
  echo "PASS: new post appears in the list"
else
  echo "FAIL: new post missing from GET /api/timeline_post" >&2
  exit 1
fi

echo "==> DELETE /api/timeline_post/$POST_ID (bonus cleanup)"
curl -s -X DELETE "$BASE_URL/api/timeline_post/$POST_ID"
echo

AFTER_DELETE=$(curl -s "$BASE_URL/api/timeline_post")
if echo "$AFTER_DELETE" | grep -q "$CONTENT"; then
  echo "FAIL: post $POST_ID still present after delete" >&2
  exit 1
else
  echo "PASS: test post cleaned up"
fi
