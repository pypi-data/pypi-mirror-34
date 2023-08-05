"""R markdown notebook format for Jupyter

Use this module to read or write Jupyter notebooks as R Markdown documents
(methods 'read', 'reads', 'write', 'writes')

Use the RmdFileContentsManager to open Rmd and Jupyter notebooks in Jupyter

Use the 'nbrmd' conversion script to convert Jupyter notebooks from/to
R Markdown notebooks.
"""

from .nbrmd import readf, writef, writes, reads, notebook_extensions, readme

try:
    from .rmarkdownexporter import RMarkdownExporter
except ImportError as e:
    RMarkdownExporter = str(e)

try:
    from .contentsmanager import RmdFileContentsManager
except ImportError as e:
    RmdFileContentsManager = str(e)
