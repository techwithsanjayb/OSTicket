from datetime import datetime


def log(request, message):
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    user = str(request.user)
    method = str(request.method)
    path = str(request.path)
    scheme = str(request.scheme)
    encoding = str(request.encoding)
    content_type = str(request.content_type)
    content_params = str(request.content_params)
    message = str(message)
    # COOKIES = str(request.COOKIES)
    # META = str(request.META)
    # FILES = str(request.FILES)
    IP = get_client_ip_address(request)

    # logdata = dt_string+"--"+scheme+"--"+IP+"--"+method+"--"+path + \
    #     "--"+user+"---"+"'"+message+"'"+"--"+encoding + \
    #     "--"+content_type+"--"+content_params+"--"+COOKIES+"--"+FILES+"--"+META

    logdata = dt_string + "--" + scheme + "--" + IP + "--" + method + "--" + path + "--" + user + "---" + "'" + message + "'" + "--" + encoding + "--" + content_type + "--" + content_params

    with open("logfile.log", 'a') as logfile:
        logfile.write(logdata)
        logfile.write("\n")
        logfile.close()


def get_client_ip_address(request):
    req_headers = request.META
    x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for_value:
        ip_addr = x_forwarded_for_value.split(',')[-1].strip()
    else:
        ip_addr = req_headers.get('REMOTE_ADDR')
    return ip_addr

