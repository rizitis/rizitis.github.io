#!/bin/bash

for file in SofoRevma_LICENSE.md; do
    output="${file%.md}.pdf"
    pandoc "$file" -o "$output" --pdf-engine=xelatex -V mainfont="DejaVu Serif"
done

