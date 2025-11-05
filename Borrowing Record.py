from collections import Counter


borrow_records = {
    'Alice': ['Book1', 'Book2'],
    'Bob': [],
    'Charlie': ['Book2', 'Book3', 'Book3'],
    'David': ['Book1'],
    'Eve': [],
}

all_books = [b for books in borrow_records.values() for b in books]
book_counts = Counter(all_books)


def avg_books(records):
    return sum(len(b) for b in records.values()) / len(records)


def most_least_books(counts):
    if not counts:
        return None, None
    return max(counts.items(), key=lambda x: x[1]), min(counts.items(), key=lambda x: x[1])


def zero_borrowers(records):
    return sum(1 for b in records.values() if not b)


def most_frequent(counts):
    if not counts:
        return []
    m = max(counts.values())
    return [book for book, c in counts.items() if c == m]


print("1. Avg books per member:", avg_books(borrow_records))
most, least = most_least_books(book_counts)
print("2. Most borrowed:", most)
print("   Least borrowed:", least)
print("3. Members with 0 borrowings:", zero_borrowers(borrow_records))
print("4. Most frequent book(s):", most_frequent(book_counts))
