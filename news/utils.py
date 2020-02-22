from typing import List

from news.models import Article


def get_latest_articles() -> List[Article]:
    return Article.objects.order_by("created_at")[:3]
