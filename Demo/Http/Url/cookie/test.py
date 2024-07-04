import http.cookiejar

# 创建一个 Cookie
cookie = http.cookiejar.Cookie(
        version=0,
        name="hello",
        value="world",
        port=None,
        port_specified=False,
        domain=".httpbin.org",
        domain_specified=True,
        domain_initial_dot=False,
        path="/",
        path_specified=True,
        secure=False,
        expires=3742443533,
        discard=False,
        comment=None,
        comment_url=None,
        rest={},
)

# 判断 Cookie 是否过期（默认与当前时间对比）
print(cookie.is_expired(now=None))


# 设置 指定名称的非标准属性值
cookie.set_nonstandard_attr("attr_name", "attr_value")
# 获取 指定名称的非标准属性值
cookie.get_nonstandard_attr("attr_name", default=None)
# 判断 是否有指定名称的非标准属性
cookie.has_nonstandard_attr("attr_name")
