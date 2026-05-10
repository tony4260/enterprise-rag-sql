from app.permissions import can_access_document
from app.retrieve import search_documents


def main():
    user_access_level = "internal"

    results = search_documents(
        query="executive bonuses",
        access_level=user_access_level
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    found_result = False

    for doc, metadata, distance in zip(documents, metadatas, distances):
        if can_access_document(user_access_level, metadata["access_level"]):
            if distance > 1.2:
                continue

            #found_result = True

            print("Document:")
            print(doc)
            print("Title:", metadata["title"])
            print("Access Level:", metadata["access_level"])
            print("Similarity Score:", distance)
            print("---")

    if not found_result:
        print("No accessible documents found.")


if __name__ == "__main__":
    main()