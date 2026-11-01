# Latihan 4: Pasang breakpoint pada baris total += angka
# lalu jalankan melalui Run and Debug di VS Code.

angka = [10, 20, 30]
total = 0

for item in angka:
    total += item
    print("Item:", item, "| Total sementara:", total)

print("Total akhir:", total)
