# MYNT® EYE SDK Guide

## Prerequisites

```bash
pip install -r requirements.txt
```

## Build HTML (zh-Hans)

```bash
make html
open _build/html/index.html
```

## Build PDF (zh-Hans)

```bash
make latexpdf
open _build/latex/mynt-eye-sdk-guide.pdf
```

## i18n (TODO: en)

```bash
# Extract document’s translatable messages into pot files
make gettext

# Setup/Update your locale_dir
sphinx-intl update -p _build/gettext -l en

# Translate your po files under ./locale/<lang>/LC_MESSAGES/

# Build mo files and make translated document
sphinx-intl build
make -e SPHINXOPTS="-D language='en'" html
```

* [Internationalization](http://www.sphinx-doc.org/en/master/intl.html)

## How to Edit

* [Sphinx Documentation](http://www.sphinx-doc.org/en/stable/contents.html)
  * [reStructuredText Primer](http://www.sphinx-doc.org/en/stable/rest.html)
* [reStructuredText](http://docutils.sourceforge.net/rst.html)
* [Quick reStructuredText](http://docutils.sourceforge.net/docs/user/rst/quickref.html)

## License

This project is licensed under the Apache License, Version 2.0. Copyright 2018 Slightech Co., Ltd.
