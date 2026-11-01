# Kasus 1: Bug batas kelulusan
# Bug: nilai 60 seharusnya lulus, tetapi program memakai operator >.

def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"


if __name__ == "__main__":
    for nilai in [59, 60, 61]:
        print(f"Nilai {nilai}: {status_lulus(nilai)}")
