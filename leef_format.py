import datetime


def make_header(ip_address):

    leef_version = "LEEF:2.0"
    vendor_name = "Vendor"
    product_name = "Product"
    product_version = "1.0"
    delimiter  = "\t"
    unique_id = "ERROR_" + get_unique_id()
    time = get_now() 
    header = '%s|%s|%s|%s|%s|\\t|' % (leef_version, vendor_name, product_name, product_version, unique_id)

    return '%s %s %s' % (time, ip_address, header)


def get_unique_id():
    return datetime.datetime.now().strftime('%y%m%d%H%M%S')


def get_now():
    return datetime.datetime.now().strftime('%B %d %Y %H:%M:%S')


if __name__ == "__main__":
    print(make_header())
    print(get_now())
