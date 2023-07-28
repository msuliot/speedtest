import speedtest

def get_speed_test_results():
    # Create a Speedtest object
    st = speedtest.Speedtest()
    
    # Get the best server for testing
    st.get_best_server()
    
    # Perform the download speed test
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    
    # Perform the upload speed test
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    # Get ping (latency) time
    ping_time = st.results.ping
    
    return download_speed, upload_speed, ping_time

def main():
    print("Running Speed Test...")
    download_speed, upload_speed, ping_time = get_speed_test_results()

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping Time: {ping_time} ms")

if __name__ == "__main__":
    main()
