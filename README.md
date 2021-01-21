# vf2symbols

Tool to generate [custom symbol images](https://developer.apple.com/documentation/xcode/creating_custom_symbol_images_for_your_app)
for Apple application development from a `wght` variable font.

Usage:

```shell
pip install -e .
vf2symbols path-to-variable-icon-font.ttf
python3 -m vf2symbols.svg2symbols path-to-svg.svg [path-to-another-svg.svg ...]
# ...
# build/symbols has your symbols
```

## Releasing

See https://googlefonts.github.io/python#make-a-release.
