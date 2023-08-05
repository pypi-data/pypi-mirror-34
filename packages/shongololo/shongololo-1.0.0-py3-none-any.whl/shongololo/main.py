# main.py
""" Collect data from CO2 meters on Pi3 USB ports via serial to FTDI cables """
import time
import sys
import shongololo.sys_admin
import shongololo.start_up

# MAIN
def main ():
    print("I ran main")

if __name__ == "__main__":

    #Start up services
    isocks, ksocks, device_dict = start_up.start_up()

    sho_logger = logging.getLogger("shongololo_logger")
    main()
    # Start data file
    status, ND = SA.mk_ND(start_up.DATADIR)
    if status !=0:
        sho_logger.error("Failed to create directory for data logging, data will not be saved to file, try restarting the application")
        sys.exit()

    else:
        fd = SA.ini_datafile( str(ND+sys_admin.DATAFILE) )

       # PRIMARY LOOP
        while 1:
            try:
                latest_data = SA.read_data(isocks, ksocks)
                print (latest_data)
                line=""
                for x in latest_data:
                    line=line+","+x

                fd.write("\n"+line)

                print("n"+line)
                time.sleep(sys_admin.PERIOD)

            except KeyboardInterrupt as e:
                SA.stop_serials(imets_sockets,k30s_ser)
                SA.stop_files([fl, fd], "\nKeyboard Interrupt: System stopped, closing down and saving data")
                sys.exit()

