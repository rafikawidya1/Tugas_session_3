if __name__ == '__main__' :
     # silahkan masukan nama anda disini
    x = 485
    y = x // 360
    bulan = x % 360
    hari = bulan // 30
    sisab = bulan % 30
    minggu = sisab // 7
    sisah = sisab % 7
    print (f"tahun {y},bulan{hari},minggu{minggu},hari{sisab}")


