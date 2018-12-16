#!/usr/bin/env bash

BASE_DIR=$(cd "$(dirname "$0")" && pwd)
BUILD_DIR="$BASE_DIR/_build"
OUTPUT_DIR="$BASE_DIR/_output"

_generate() {
  _lang="$1"; shift
  _options="$@"; shift
  echo "lang: $_lang"
  echo "options: $_options"

  cd "$BASE_DIR"

  make clean

  make $_options html

  make $_options latexpdf
  make $_options latexpdf

  # package

  filename_raw="mynt-eye-s-sdk-guide"
  filename="$filename_raw"

  version=`cat conf.py | grep -m1 "^version\s*=" | \
      sed -E "s/version = ['\"]([0-9\.]*)['\"]/\1/g"`
  if [ -n "$version" ]; then
    filename="$filename-$version"
  fi

  if [ -n "$_lang" ]; then
    filename="$filename-$_lang"
  fi

  # echo "filename: $filename"

  if [ -d "$BUILD_DIR/html" ]; then
    cd "$BUILD_DIR"
    mv "html" "$filename" && zip -r "$filename.zip" "$filename"
    mv "$filename.zip" "$OUTPUT_DIR"
  fi

  if [ -d "$BUILD_DIR/latex" ]; then
    cd "$BUILD_DIR/latex"
    [ -f "$filename_raw.pdf" ] && mv "$filename_raw.pdf" "../$filename.pdf"
    mv "../$filename.pdf" "$OUTPUT_DIR"
  fi
}

[ -d "$OUTPUT_DIR" ] || mkdir -p "$OUTPUT_DIR"

_generate "zh-Hans"
_generate "en" "-e SPHINXOPTS=\"-Dlanguage=en\""
