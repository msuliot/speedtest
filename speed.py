import speedtest

def get_speed_test_results():
    st = speedtest.Speedtest(secure=True)
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping_time = st.results.ping
    
    return download_speed, upload_speed, ping_time

def format_speed(speed):
    if speed >= 1000:
        return f"{speed/1000:.2f} GB/s"
    elif speed >= 1:
        return f"{speed:.2f} MB/s"
    else:
        return f"{speed*1000:.2f} Mbps"

def main():
    print("Running Speed Test...")
    download_speed, upload_speed, ping_time = get_speed_test_results()

    print("Download Speed:", format_speed(download_speed))
    print("Upload Speed:", format_speed(upload_speed))
    print(f"Ping Time: {ping_time} ms")

if __name__ == "__main__":
    main()
