def normalize_job_description(text: str) -> str:
    if not text:
        return ""
    text = text.replace("\r", "")
    import re
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip()
