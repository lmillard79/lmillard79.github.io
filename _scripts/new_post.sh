#!/bin/bash

# Check if a title was provided
if [ -z "$1" ]; then
    echo "Error: No title provided"
    echo "Usage: ./new_post.sh 'Your Post Title'"
    exit 1
fi

# Create a slug from the title
SLUG=$(echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd '[:alnum:]-')
DATE=$(date +"%Y-%m-%d %H:%M:%S %z")
FILENAME="$(date +%Y-%m-%d)-${SLUG}.md"
FILEPATH="_posts/${FILENAME}"

# Create the _posts directory if it doesn't exist
mkdir -p "_posts"

# Create the new post file with front matter
cat > "${FILEPATH}" << EOF
---
layout: post
title: "$1"
date: ${DATE}
categories: [hydrology, engineering]
tags: [tag1, tag2]
---

# $1

Start writing your post here...

## Subheading

Content goes here.

## Conclusion

Wrap up your post.

<!-- Add your references here if needed -->

## About the Author

Lindsay Millard is a water resources engineer with expertise in hydrological modeling and data analysis.

*Connect with me on [LinkedIn](https://www.linkedin.com/in/lindsaymillard/)*
EOF

echo "New post created: ${FILEPATH}"
echo "Don't forget to update the categories and tags in the front matter!"
