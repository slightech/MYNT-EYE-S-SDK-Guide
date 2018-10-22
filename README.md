# MYNT® EYE SDK Guide

[![](https://img.shields.io/badge/MYNT%20EYE%20SDK%20Guide-2.2.1--rc-brightgreen.svg?style=flat)](https://github.com/slightech/MYNT-EYE-SDK-2-Guide)

MYNT® EYE SDK Guide is the documentation about how to install and start using the SDK.

* en: [![](https://img.shields.io/badge/Download-PDF-blue.svg?style=flat)](https://github.com/slightech/MYNT-EYE-SDK-2-Guide/files/2501821/mynt-eye-sdk-guide-2.2.1-rc-en.pdf) [![](https://img.shields.io/badge/Download-HTML-blue.svg?style=flat)](https://github.com/slightech/MYNT-EYE-SDK-2-Guide/files/2501822/mynt-eye-sdk-guide-2.2.1-rc-en.zip) [![](https://img.shields.io/badge/Online-HTML-blue.svg?style=flat)](https://slightech.github.io/MYNT-EYE-SDK-2-Guide/)
* zh-Hans: [![](https://img.shields.io/badge/Download-PDF-blue.svg?style=flat)](https://github.com/slightech/MYNT-EYE-SDK-2-Guide/files/2501823/mynt-eye-sdk-guide-2.2.1-rc-zh-Hans.pdf) [![](https://img.shields.io/badge/Download-HTML-blue.svg?style=flat)](https://github.com/slightech/MYNT-EYE-SDK-2-Guide/files/2501827/mynt-eye-sdk-guide-2.2.1-rc-zh-Hans.zip) [![](https://img.shields.io/badge/Online-HTML-blue.svg?style=flat)](http://doc.myntai.com/resource/sdk/mynt-eye-sdk-guide-2.2.1-rc-zh-Hans/mynt-eye-sdk-guide-2.2.1-rc-zh-Hans/index.html)

All doc releases are [here](https://github.com/slightech/MYNT-EYE-SDK-2-Guide/releases). Besides, you could build the doc according to the following content.

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

## i18n (en)

```bash
# Extract document’s translatable messages into pot files
make gettext

# Setup/Update your locale_dir
sphinx-intl update -p _build/gettext -l en

# Translate your po files under ./locale/<lang>/LC_MESSAGES/

# Build mo files and make translated document
sphinx-intl build
```

* [Internationalization](http://www.sphinx-doc.org/en/master/intl.html)

### Build HTML (en)

```bash
# Linux, MacOS
make -e SPHINXOPTS="-D language='en'" html
# Windows
set SPHINXOPTS=-D language=en & make.bat html
```

### Build PDF (en)

```bash
# Linux, MacOS
make -e SPHINXOPTS="-D language='en'" latexpdf
# Windows
set SPHINXOPTS=-D language=en & make.bat latexpdf
```

## How to Edit

* [Sphinx Documentation](http://www.sphinx-doc.org/en/stable/contents.html)
  * [reStructuredText Primer](http://www.sphinx-doc.org/en/stable/rest.html)
* [reStructuredText](http://docutils.sourceforge.net/rst.html)
* [Quick reStructuredText](http://docutils.sourceforge.net/docs/user/rst/quickref.html)

## Mirrors

国内镜像：[码云](https://gitee.com/mynt/MYNT-EYE-SDK-2-Guide)。

## License

This project is licensed under the Apache License, Version 2.0. Copyright 2018 Slightech Co., Ltd.
