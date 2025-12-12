#!/usr/bin/env python3
"""Mongo insert"""
def insert_school(mongo_collection, **kwargs):
    """inserts new document"""
    return mongo_collection.insert_one(kwargs).inserted_id
