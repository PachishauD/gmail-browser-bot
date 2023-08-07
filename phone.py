import requests

api_key = "8280f9b59cbde0317106c1d626f72A95"
service_id = 7837308

response = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={api_key}&action=getNumber&service={service_id}")


print(response.text)