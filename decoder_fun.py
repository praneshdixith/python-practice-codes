def decodefun(fun):
    def wraper():
        print("Hello Dhanvi")
        fun()
        print("Hellow Druvit")
    return wraper
@decodefun
def fun():
    print("IM in function call")

fun()
