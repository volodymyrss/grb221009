def gen(modality, ref):
    import requests    
    # r = requests.get(ref, headers={'Accept': 'application/rdf+xml'})
    r = requests.get(ref, headers={'Accept': 'application/x-bibtex; charset=utf-8'})    

    with open("found-references.bib", "ab") as f:        
        f.write(r.content)

        return f"{modality}:{ref}:\cite{{Falcone_2007}}"
