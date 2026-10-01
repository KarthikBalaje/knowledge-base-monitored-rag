def build_context(documents):
    return "\n\n".join(f"[Source: {d.get('source')} | Page: {d.get('page_number')} | Domain: {d.get('domain')}]\n{d.get('text','')}" for d in documents)
