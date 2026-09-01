#!/bin/bash
# Create a new blog post with front matter matching this site's actual
# conventions (see README.md > Adding New Content for the full pattern).
#
# Usage:
#   ./new_post.sh "Your Post Title"              # commentary/insights post
#   ./new_post.sh "Your Post Title" --tutorial    # Python tutorial post

if [ -z "$1" ]; then
    echo "Error: No title provided"
    echo "Usage: ./new_post.sh 'Your Post Title' [--tutorial]"
    exit 1
fi

SLUG=$(echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd '[:alnum:]-')
DATE=$(date +%Y-%m-%d)
FILEPATH="_posts/${DATE}-${SLUG}.md"

if [ "$2" == "--tutorial" ]; then
    TAGS="python, tutorial, hydrology"
else
    TAGS="hydrology, flood-modelling"
fi

mkdir -p "_posts"

cat > "${FILEPATH}" << EOF
---
title: "$1"
date: ${DATE}
categories: [insights]
tags: [${TAGS}]
excerpt: "One or two sentences summarising the post -- shown on the /insights/ and homepage cards."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

Start writing here. Don't set \`layout:\` -- it defaults to the right thing via _config.yml.
EOF

echo "New post created: ${FILEPATH}"
echo "Remember to: write real excerpt text, add a real hero image if you have one,"
echo "and update tags. See README.md for the full content template and conventions."
