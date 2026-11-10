from datetime import datetime

# Mendapatkan waktu dan tanggal saat ini
current_time = datetime.now()

print(f"Current Date and Time: {current_time}")
print(f"Year: {current_time.year}")
print(f"Month: {current_time.strftime('%B')}")  # Nama bulan lengkap
print(f"Day of the week: {current_time.strftime('%A')}")  # Nama hari lengkap

# Menghitung berapa hari lagi menuju Tahun Baru
new_year = datetime(current_time.year + 1, 1, 1)
time_remaining = new_year - current_time

print(f"\nThere are {time_remaining.days} days left until New Year's Day!")