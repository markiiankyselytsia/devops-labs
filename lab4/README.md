## Lab_4: Робота з Docker
### What to do.
1. Для початку я встановив докер і перевірив його роботу командами
```
docker -v >> my_work.log
docker -h >> my_work.log
docker run docker/whalesay cowsay Docker is fun >> my_work.log
```
Вивід команд записав в my_work.log.

2. Після цього я промодифікував докер файл для коректної роботи з моїм проектом і збілдив імедж командою
```docker build -t markiiank/devops-labs-images:django .```

3. Чи імедж коректно створився я перевірив командою
```
$ docker image ls
REPOSITORY                                   TAG                 IMAGE ID            CREATED             SIZE
devops-labs-images/website-image             django              666408fb2884        6 minutes ago      279MB
```

4. Далі запушив імедж в свій [репозиторій](https://hub.docker.com/repository/docker/markiiank/devops-labs-images/general)
```docker push markiiank/devops-labs-images:django```

7. Потім я створив контейнер зі свого імеджу і запустив його в інтерактивному моді
```
$ docker run -it --name=django-app --rm -p 8000:8000 markiiank/devops-labs-images:django
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
December 20, 2020 - 18:11:16
Django version 3.1.4, using settings 'my_site.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```
8. Cтворив Dockerfile.site. Виконав білд (build) Docker імеджа з моніторингом та завантажив його до репозиторію.
	```
    sudo docker build -t  markiiank/devops-labs-images:django --file Dockerfile.site . 
    sudo docker images
    sudo docker push  markiiank/devops-labs-images:monitoring
	```
	Запустив обидва імеджі.
	```	
     sudo docker run -it --rm -p 8000:8000  markiiank/devops-labs-images:django
     sudo docker run --net=host --rm -it --volume /home/Marik1/Lab_4:/app markiiank/devops-labs-images:monitoring
	 ```
9. Після успішного виконання роботи відредагуйте Ваш персональний _README.md_ у цьому репозиторію та створіть pull request.
