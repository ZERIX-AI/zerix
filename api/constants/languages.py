# TESTED ON 2024-10-19 20:42 GMT
language_timezone_mapping = {
    "en-US": "America/New_York",
}

# TESTED ON 2024-10-19 20:43 GMT
languages = list(language_timezone_mapping.keys())


# TESTED ON 2024-10-19 21:22 GMT
def supported_language(lang):
    if lang in languages:
        return lang

    error = "{lang} is not a valid language.".format(lang=lang)
    raise ValueError(error)
