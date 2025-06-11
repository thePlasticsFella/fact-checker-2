from claim_extractor import extract_claims
from pubmed_search import search_pubmed

def fact_check(text):
    claims = extract_claims(text).split("\n")
    verified = []
    for claim in claims:
        if not claim.strip():
            continue
        citation = search_pubmed(claim)
        if citation:
            verified.append((claim, citation))
        else:
            verified.append((claim, "❌ No source found"))
    return verified