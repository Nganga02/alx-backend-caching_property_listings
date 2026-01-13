from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Returns all Property objects, caching the queryset in Redis for 1 hour.
    """
    # Try to get from cache
    properties = cache.get('all_properties')

    if properties is None:
        # Fetch from database if not cached
        properties = list(Property.objects.all())
        # Store in cache for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)

    return properties


import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and log the hit ratio.
    Returns a dictionary with hits, misses, and hit_ratio.
    """
    # Get the raw Redis client from django_redis
    client = cache.client.get_client(write=True)

    # Fetch Redis INFO stats
    info = client.info('stats')

    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)

    # Calculate hit ratio
    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0.0

    metrics = {
        'keyspace_hits': hits,
        'keyspace_misses': misses,
        'hit_ratio': round(hit_ratio, 4)
    }

    # Log the metrics
    logger.info(f"Redis Cache Metrics: {metrics}")

    return metrics
