import requests

r = requests.get("http://htmlbook.ru/")
print("Получим просто код ответа:")
print(r)

print("---------------")
print("---------------")

# Вариант 1 - колхозный
r_post = requests.post("https://reqres.in/api/users", data={"name": "Petrovich", "job": "Tester"})
print(r_post.text)
print("---------------")
# Вариант 2 с выносом тела запроса в отдельную переменную и форматированием ответа в json
# и последующей записью содержимого ответа сервера в json файл
data={"name": "Petrovich", "job": "Tester"}
r_post_2 = requests.post("https://reqres.in/api/users", data=data)
with open("response.json", "w") as f:
    f.write(r_post_2.text) # методом text обнаруживаем содержимое ответа