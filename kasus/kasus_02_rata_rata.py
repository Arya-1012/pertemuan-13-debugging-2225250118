# Kasus 2: Bug rata-rata
# Bug: pembagi selalu 5, meskipun jumlah data berbeda.

def rata_rata(data):
    total = sum(data)
    return total / 5


if __name__ == "__main__":
    print("Rata-rata:", rata_rata([80, 90, 70]))
