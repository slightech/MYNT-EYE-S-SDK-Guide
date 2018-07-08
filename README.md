# MYNT® EYE SDK Guide

MYNT® EYE SDK Guide is the documentation about how to install and start using the SDK.

Download the latest doc [here](https://github.com/slightech/MYNT-EYE-SDK-2-Guide/releases). Besides, you could build the doc according to the following content.

## Prerequisites

```bash
pip install -r requirements.txt
```

## Build HTML (zh-Hans)

```bash
make html

# Linux
xdg-open _build/html/index.html

# MacOS
open _build/html/index.html

# Windows
start _build/html/index.html
```

## Build PDF (zh-Hans)

```bash
make latexpdf

# Linux
xdg-open _build/latex/mynt-eye-sdk-guide.pdf

# MacOS
open _build/latex/mynt-eye-sdk-guide.pdf

# Windows
start _build/latex/mynt-eye-sdk-guide.pdf
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
# Linux
make -e SPHINXOPTS="-D language='en'" html
# Windows
set SPHINXOPTS=-D language=de
.\make.bat html
```

* [Internationalization](http://www.sphinx-doc.org/en/master/intl.html)

## How to Edit

* [Sphinx Documentation](http://www.sphinx-doc.org/en/stable/contents.html)
  * [reStructuredText Primer](http://www.sphinx-doc.org/en/stable/rest.html)
* [reStructuredText](http://docutils.sourceforge.net/rst.html)
* [Quick reStructuredText](http://docutils.sourceforge.net/docs/user/rst/quickref.html)

## Mirrors

国内镜像：[码云](https://gitee.com/mynt/MYNT-EYE-SDK-2-Guide)。

## License

This project is licensed under the Apache License, Version 2.0. Copyright 2018 Slightech Co., Ltd.
