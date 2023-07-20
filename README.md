# Kindle cLIPpings NAVigator

[![pypi](https://img.shields.io/pypi/v/klip-nav.svg)](https://pypi.org/pypi/klip-nav)
![build status](https://github.com/skogsgren/klip_nav/workflows/Run%20tests/badge.svg)

![](https://raw.githubusercontent.com/skogsgren/klip_nav/main/img/screenshot1.png)

Opinionated TUI Python program to explore Kindle clippings on a book-to-book
basis.

It was written to encompass my workflow where I need easy access to
copy-to-clipboard for note/highlight contents (useful for making flashcards).

![](https://raw.githubusercontent.com/skogsgren/klip_nav/main/img/screenshot2.png)

## Installation

```
pip install klip-nav
```

or if on a distro without global `pip` (like Debian Bookworm) use a helper
like `pipx`:

```
pipx install klip-nav
```

## Usage

```
klip_nav CLIPPINGS_FILE
```

## Keybindings

Vim keybindings (`hjkl`/`u`/`d`) or arrow keys if using keyboard, `Enter` to
select, `q` to quit. The mouse can also be used to scroll and click through
entries.
