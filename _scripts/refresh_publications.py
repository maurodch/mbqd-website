#!/usr/bin/env -S conda run --no-capture-output -n mbqd-website python

# Author: Adrian Braemer
# 
# TODO: Convert into proper cmd tool
# TODO: Generalize a bit to of use for other websites?

from importlib.resources import read_text
from pathlib import Path
from datetime import date
import bibtexparser
import pyaml

print(f"CWD: {Path.cwd()}")
BASEPATH = Path(__file__).parent.parent

publications = BASEPATH / "content" / "publication"
print(str(publications / "**" / "*.md"))

def load_website_yaml(path):
    with path.open() as input:
        if not input.readline().startswith("---"):
            raise RuntimeError(f"{str(path)} does not contain a Wowchemy yaml frontmatter!")
        lines = []
        while not (l := input.readline()).startswith("---"):
            lines.append(l)
    return pyaml.yaml.load("\n".join(lines), Loader=pyaml.yaml.CLoader)


def write_website_yaml(path, data):
    with path.open("w") as out:
        out.write("---\n")
        out.write(pyaml.dump(data))
        out.write("---\n")

### load authors
AUTHORS = {}
for folder in (BASEPATH / "content" / "authors").iterdir():
    if not folder.is_dir():
        continue
    data = load_website_yaml(folder / "_index.md")
    AUTHORS[(data["title"]).split()[-1]] = data["authors"][0]

print(AUTHORS)

def replace_author(author:str):
    author = author.replace(r'\"u', "ü")
    author = author.replace(r'\"a', "ä")
    author = author.replace(r'\"o', "ö")
    author = author.replace(r"\'e", "é")
    author = author.replace('{', "")
    author = author.replace('}', "")
    lastname = author.split(",")[0]
    if lastname in AUTHORS:
        return AUTHORS[lastname]
    return " ".join(reversed(author.split(","))).strip()

#### MONTH parsing

MONTH_MAPPING = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
def try_parse_month(month):
    if isinstance(month, int):
        return month
    month = month.lower()
    try:
        ind = MONTH_MAPPING.index(month)
        return ind+1
    except ValueError:
        pass
    try:
        mon = int(month)
        return mon
    except ValueError:
        pass
    for (i,name) in enumerate(MONTH_MAPPING):
        if month.startswith(name):
            return i+1
    return None

### Projects of publication

PROJECTS =  ["disorder", "entanglement", "quantum-ann","tomography","quantum-simulation"]

def get_projects(bibdata, old_frontmatter):
    saved = DB.get(bibdata["ID"], {})
    DB[bibdata["ID"]] = saved
    if "projects" in saved:
        return saved["projects"]
    project_data = None
    if old_frontmatter and "projects" in old_frontmatter:
        project_data = old_frontmatter["projects"]
        print("Got project data from old index.md:", project_data)
    if project_data is None:
        print(f"[{bibdata['title']}] No data on projects found!")
        print(f"Mapping: {list(enumerate(PROJECTS))}")
        print("Enter projects as comma-separated numbers.")
        inp = input("> ").strip()
        if len(inp) > 0:
            pindices = map(int, inp.split(","))
            project_data = [PROJECTS[i] for i in pindices]
    saved["projects"] = project_data or []
    return project_data

### dates
def get_date(bibdata, old_frontmatter):
    saved = DB.get(bibdata["ID"], {})
    DB[bibdata["ID"]] = saved
    year = bibdata["year"] or saved.get("year", None)
    month = bibdata["month"] or saved.get("month", None)
    day = saved.get("day", None)
    if not old_frontmatter is None and "date" in old_frontmatter:
        olddate = old_frontmatter["date"]
        if olddate:
            if isinstance(olddate, str):
                olddate = date.fromisoformat(olddate)
            year = year or olddate.year
            month = month or olddate.month
            day = day or olddate.day
    
    year = year or int(ask_for("year", bibdata))
    month = month or try_parse_month(ask_for("month", bibdata))
    day = day or 1
    saved["year"] = year
    saved["month"] = month
    saved["day"] = day
    return date(year,month,day)

### abstract

def get_abstract(bibdata, old_frontmatter):
    saved = DB.get(bibdata["ID"], {})
    DB[bibdata["ID"]] = saved
    abstract = bibdata.get("abstract") or saved.get("abstract") or old_frontmatter.get("abstract") or ""
    abstract.replace("\n","")
    saved["abstract"] = abstract
    return abstract

#### bibtex parser

def mycustomization(record):
    # unicode does not works somehow...
    #record = bibtexparser.customization.convert_to_unicode(record)
    record = bibtexparser.customization.author(record)
    return record

def get_bibtex_parser():
    bibtex_parser = bibtexparser.bparser.BibTexParser()
    bibtex_parser.ignore_nonstandard_types = False
    bibtex_parser.homogenize_fields = True
    bibtex_parser.customization = mycustomization
    return bibtex_parser


#### Value persistence

DBPATH = BASEPATH / "_scripts" / "publication_data.txt"
DB = None
if DBPATH.exists():
    _DB = pyaml.yaml.load(DBPATH.read_text(), Loader=pyaml.yaml.CLoader)
    if isinstance(_DB, dict):
        DB = _DB
        print(f"Loaded old db with {len(DB)} keys!")
if DB is None:
    DB = {}
    print(f"No old DB found - creating new one at: {DBPATH!s}")

def ask_for(val, bibdata, persist=True):
    print(f"[{bibdata['title']}] Enter value for {val}")
    answer = input("> ")
    if persist:
        id = bibdata["ID"]
        if not id in DB:
            DB[id] = {}
        DB[id][val] = answer
    return answer

def load_or_ask(key, bibdata):
    if key in bibdata:
        return bibdata[key]
    if bibdata["ID"] in DB and key in DB[bibdata["ID"]]:
        return DB[bibdata["ID"]][key]
    return ask_for(key, bibdata)

#### Main

def handle_arXiv_preprint(frontmatter, code, bibdata):
    bibdata["year"] = int("20"+code[0:2])
    bibdata["month"] = int(code[2:4])
    frontmatter["doi"] = "10.48550/arXiv."+code
    frontmatter["publication"] = f'ArXiv {code}'

FORCE = False

for folder in publications.iterdir():
    if not folder.is_dir():
        continue
    bibtex_file = folder / "cite.bib"
    index_file = folder / "index.md"
    if not FORCE and index_file.exists():
        print(f"Skipping (index.md found): {str(folder.relative_to(BASEPATH))}")
        continue
    if not bibtex_file.exists():
        print(f"No 'cite.bib' found: {str(folder.relative_to(BASEPATH))}")
        continue

    print(f"Doing: {str(folder.relative_to(BASEPATH))}")
    bibtex = bibtexparser.loads(bibtex_file.read_text(), parser=get_bibtex_parser())
    bibdata = bibtex.get_entry_list()[0]
    bibdata["year"] = int(bibdata["year"]) if "year" in bibdata else None
    bibdata["month"] = try_parse_month(bibdata["month"]) if "month" in bibdata else None

    old_frontmatter = (load_website_yaml(index_file) or {}) if index_file.exists() else {}
        
    print(bibdata)
    frontmatter = {}
    frontmatter["title"] = bibdata["title"]
    frontmatter["authors"] = list(map(replace_author, bibdata["author"]))
    frontmatter["publication_types"] = ["2"]

    frontmatter["abstract"] = get_abstract(bibdata, old_frontmatter)
    
    if bibdata["ENTRYTYPE"] == "misc": # is ArXiV hopefully
        if "archiveprefix" in bibdata and bibdata["archiveprefix"] == "arXiv":
            # old arXiv bibtex file
            code = bibdata["eprint"]
            handle_arXiv_preprint(frontmatter, code, bibdata)
        elif "publisher" in bibdata and bibdata["publisher"] == "arXiv":
            # new arXiv bibtex file
            code = bibdata["url"].split("/")[-1]
            handle_arXiv_preprint(frontmatter, code, bibdata)
        else:
            raise RuntimeError("What kind of publication is this?")
    else: # is Journal
        frontmatter["doi"] = load_or_ask("doi", bibdata)
        frontmatter["publication"] = load_or_ask("journal", bibdata)
        if "volume" in bibdata:
            frontmatter["publication"] += f' **{bibdata["volume"]}**'
        if "pages" in bibdata:
            frontmatter["publication"] += f', {bibdata["pages"]}'
    

    frontmatter["date"] = get_date(bibdata, old_frontmatter)
    frontmatter["projects"] = get_projects(bibdata, old_frontmatter)
    
    write_website_yaml(folder/"index.md", frontmatter)
    print()

## Save DB
with DBPATH.open("w") as output:
    output.write(pyaml.dump(DB))
