from pystdf4.Records.StdfFileRecord import FAR

if __name__ == "__main__":
    a = FAR()
    a.CPU_TYPE = 1
    a.STDF_VER = 4
    print(a.__annotations__)
    print(a)