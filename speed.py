from speedtest import Speedtest

wifi = Speedtest()

print("Getting Download speed...")
download = wifi.download() / 1_000_000  # Convert from bits to Mbps
print(f"Download speed: {download:.2f} Mbps")

print("Getting Upload speed...")
upload = wifi.upload() / 1_000_000  # Convert from bits to Mbps
print(f"Upload speed: {upload:.2f} Mbps")
