from Bio import Entrez

Entrez.email = "your-email@example.com"

def search_pubmed(query):
    try:
        handle = Entrez.esearch(db="pubmed", term=query, retmax=1)
        record = Entrez.read(handle)
        if not record["IdList"]:
            return None
        pubmed_id = record["IdList"][0]
        summary = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="abstract", retmode="text")
        return summary.read()
    except Exception as e:
        return f"Error searching PubMed: {e}"