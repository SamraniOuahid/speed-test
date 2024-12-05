import speedtest

wifi = speedtest.Speedtest()
wifi.get_best_server()

print("Testing download...")
download = wifi.download()
print(f"Download speed: {download / 1_000_000:.2f} Mbps")

print("Testing upload...")
upload = wifi.upload()
print(f"Upload speed: {upload / 1_000_000:.2f} Mbps")
