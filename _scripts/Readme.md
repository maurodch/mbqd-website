# Helper scripts

## refresh_publications.py

Expectes a conda environment named `mbqd-website` with the packages from `refresh_publications-requirements_conda.txt`.

When run (re)generates the `_index.md` in the subfolders of `publication` with information taken from the `cite.bib`. When information is missing the script looks for it in its database (`publication_data.txt`) and asks for user input if it's also missing there. Commonly happens for projects a newly added paper should be associated with but other fields are possible as well.

Normally the script only generates a `_index.md` if none is present. If FORCE=True (currently requires editing the script) ALL `_index.md` are regenerated.

Note: Information is stored under its bibtex citation key. So if a paper gets published and a different citation key is used in the new `cite.bib` you'll have to reenter any missing information.
