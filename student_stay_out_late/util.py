import hashlib
import time
import urllib

#教师发消息
def message(userid, content, resurl, title):
    now = str(int(time.time()))
    app_key = "test_key"
    app_secret = "test_secret"
    data = [now, app_key, app_secret]
    data = sorted(data)
    data = "".join(data)
    token = hashlib.sha256(data.encode("utf8")).hexdigest()
    url = "http://172.16.30.138:8888/message/qy?ts=" + now + "&app_key=test_key&token=" + token + ""
    postdata = urllib.parse.urlencode({'touser': userid, 'content': content, 'url': resurl, 'title': title})
    postdata = postdata.encode('utf-8')
    res = urllib.request.urlopen(url, postdata)
#数据处理
