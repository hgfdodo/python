while True:
    try:
        x=input("x:")
        y=input("y:")
        print ("%s/%s is %s" % (x,y,x/y))
    
    except (Exception), e:
        print e
    else:
        break;
