def clean(row):
    return {k.strip():str(v).strip() for k,v in row.items()}
