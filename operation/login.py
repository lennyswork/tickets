# 测试登录效果
import requests



def login(username, password):
	url = "http://wechat.51fight.cn/login"
	params = {
		'phone':username,
		'password':password
	}
	resp = requests.post(url, data = params)
	print(dir(resp))
	return resp.text

if __name__ == '__main__':
	username = "18200251275"
	password = "123456"
	res = login(username, password)
	print(res)