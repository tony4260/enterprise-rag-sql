def can_access_document(user_access_level, document_access_level):
    access_rank = {
        "public": 1,
        "internal": 2,
        "confidential": 3
    }

    user_rank = access_rank.get(user_access_level, 0)
    document_rank = access_rank.get(document_access_level, 0)

    return user_rank >= document_rank