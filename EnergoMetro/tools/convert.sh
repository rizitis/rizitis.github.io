#!/bin/bash

for file in green.md blue.md yellow.md orange.md; do
    output="${file%.md}.pdf"
    pandoc "$file" -o "$output" --pdf-engine=xelatex -V mainfont="DejaVu Serif"
done

