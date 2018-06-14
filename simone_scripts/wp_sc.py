html_str2 = """<table border=1>
     <tr>
     <th>Number</th>
     <th>Square</th>
     </tr>
    <indent>
     <% for i in range(10): %>
     <tr>
     <td><%= i %></td>
     <td><%= i**2 %></td>
     </tr>
    </indent>
</table>
"""

html_str= """
HTTP/1.1 200 OK
Cache-Control: max-age=604800
Content-Type: text/html
Date: Sat, 02 Jun 2018 10:06:37 GMT
Etag: "1541025663+ident"
Expires: Sat, 09 Jun 2018 10:06:37 GMT
Last-Modified: Fri, 09 Aug 2013 23:54:35 GMT
Server: ECS (dca/249E)
Vary: Accept-Encoding
X-Cache: HIT
Content-Length: 1270
X-Original-Url: https://www.example.org/

<!doctype html>
<html>
<head>
    <title>Example Domain</title>

 <meta charset="utf-8" />
 <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
 <meta name="viewport" content="width=device-width, initial-scale=1" />
 <style type="text/css">
 body {
 background-color: #f0f0f2;
margin: 0;
padding: 0;
font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
                                                                      
}
div {
 width: 600px;
 margin: 5em auto;
 padding: 50px;
 background-color: #fff;
 border-radius: 1em;
}
a:link, a:visited {
 color: #38488f;
 text-decoration: none;
}
@media (max-width: 700px) {
body {
 background-color: #fff;
}
div {
 width: auto;
 margin: 0 auto;
 border-radius: 0;
 padding: 1em;
}
}
</style>    
</head>
<body>
<div>
<h1>Example Domain</h1>
<p>This domain is established to be used for illustrative examples in documents. You may use this
domain in examples without prior coordination or asking for permission.</p>
<p><a href="http://www.iana.org/domains/example">More information...</a></p>
</div>
"""

html_str3="""
</body>
</html>
"""



Html_file= open("/tmp/quic-data/www.example.org/index.html","w")
Html_file.write(html_str)
for x in range(0, 1000000):
    Html_file.write(html_str2)

Html_file.write(html_str3)
Html_file.close()
