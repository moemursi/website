from app.utils import get_substitutions_templates


def variables_processor(request=None):
    c = get_substitutions_templates()
    from news.utils import get_latest_articles
    c["articles"] = get_latest_articles()
    return c
