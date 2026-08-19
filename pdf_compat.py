#!/usr/bin/env python3
"""Write print-shop friendly PDFs from SVG.

cairosvg emits PDF 1.7 with cross-reference streams and object streams.
CorelDRAW and Photoshop refuse those with a "corrupted file" error, so every
PDF is rewritten as plain PDF 1.4: classic xref table, no object streams.
"""
import io

import cairosvg
import pikepdf


def svg_to_pdf(svg: str | bytes, path: str) -> str:
    """Render `svg` and save it to `path` as a PDF 1.4 file."""
    data = svg.encode() if isinstance(svg, str) else svg
    buf = io.BytesIO()
    cairosvg.svg2pdf(bytestring=data, write_to=buf)
    buf.seek(0)
    with pikepdf.open(buf) as pdf:
        pdf.save(
            path,
            min_version="1.4",
            force_version="1.4",
            object_stream_mode=pikepdf.ObjectStreamMode.disable,
            compress_streams=True,
        )
    return path


def rewrite_pdf(path: str) -> str:
    """Rewrite an existing PDF in place as PDF 1.4."""
    with pikepdf.open(path, allow_overwriting_input=True) as pdf:
        pdf.save(
            path,
            min_version="1.4",
            force_version="1.4",
            object_stream_mode=pikepdf.ObjectStreamMode.disable,
            compress_streams=True,
        )
    return path


if __name__ == "__main__":
    import glob
    import sys

    targets = sys.argv[1:] or sorted(glob.glob("willipu_*.pdf"))
    for p in targets:
        rewrite_pdf(p)
        print(p, "· PDF 1.4")
