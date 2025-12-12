#!/usr/bin/env/ python3
"""Module that updates topics of school documents"""


def update_topics(mongo_collection, name, topics):
    """Update all topics of a school document based on name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

