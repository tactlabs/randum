# coding=utf-8
from randum.sphinx.docstring import ProviderMethodDocstring
from randum.sphinx.documentor import write_provider_docs


def _create_source_files(app):
    write_provider_docs()


def _process_docstring(app, what, name, obj, options, lines):
    docstring = ProviderMethodDocstring(app, what, name, obj, options, lines)
    if not docstring.skipped:
        lines[:] = docstring.lines[:]


def setup(app):
    app.setup_extension('sphinx.ext.autodoc')
    app.connect('builder-inited', _create_source_files)
    app.connect('autodoc-process-docstring', _process_docstring)
