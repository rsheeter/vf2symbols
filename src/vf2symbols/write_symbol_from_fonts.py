# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Generates an Apple custom symbol using one or more font instances."""
import contextlib
import os

from absl import app
from absl import flags

from fontTools import ttLib
from fontTools.pens.svgPathPen import SVGPathPen
from picosvg.geometric_types import Rect
from vf2symbols import icon_font
from vf2symbols.symbol import Symbol

FLAGS = flags.FLAGS

# internal flags, typically client wouldn't change
flags.DEFINE_string("out", None, "Output file.")


def update_symbol(symbol, ttfont, icon_name, symbol_wght_name):
    glyph_name = icon_font.resolve_ligature(ttfont, icon_name)
    upem = ttfont["head"].unitsPerEm
    # For Icon fonts, the Glyphs are Y shifted by upem and the Y axis is flipped.
    symbol.write_icon(
        symbol_wght_name,
        ttfont.getGlyphSet()[glyph_name],
        SVGPathPen(ttfont.getGlyphSet()),
        Rect(0, upem, upem, -upem),
    )


def main(argv):
    icon_name = os.path.splitext(os.path.basename(FLAGS.out))[0]

    symbol = Symbol()

    for font_filename in argv[1:]:
        with contextlib.closing(ttLib.TTFont(font_filename)) as ttfont:
            update_symbol(symbol, ttfont, icon_name, font_filename.split(".")[-2])

    symbol.drop_empty_icons()
    symbol.write_to(FLAGS.out)


if __name__ == "__main__":
    app.run(main)
