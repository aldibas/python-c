import sys,os

height = raw_input("Yukseklik Giriniz:  ")
height = int(height)
space = height*2-2
for i in xrange(0,height,1):
    for h in xrange(0,4,1):
        for j in xrange(0,i,1):
            sys.stdout.write(" ")
            sys.stdout.write("xxx")
            for k in xrange(0,space,1):
<<<<<<< HEAD
                                                                                        sys.stdout.write("OOO")

                                                                                                for j in xrange(0,i,1):
                                                                                                                sys.stdout.write(" ")



                                                                                                                    space = space - 2

                                                                                                                        sys.stdout.write("\n")
=======
                sys.stdout.write("xxx")
                for j in xrange(0,i,1):
                    sys.stdout.write(" ")
                    space = space - 2
                    sys.stdout.write("\n")
>>>>>>> refs/remotes/origin/master
