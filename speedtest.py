import speedtest
st = speedtest.Speedtest()

while True:
    dowload_speed = st.dowload()

    print("dowload speed : {:5.2f} Mb".format((dowload_speed/1024*1024)))
