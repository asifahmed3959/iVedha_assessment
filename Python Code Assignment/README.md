This repository contains the answer for the assignment of iVedha and the questions of Python Code Assignment.

To Run the programs
1)  A python3 virtual environment is needed. 
2. To ensure the correct packages are used to run the test cases, the packages can be installed using the command:

```
$ pip install -r requirements.txt
```

Answer to TEST 1 a and b is in the scripts of test_1_a.py file and test_2_b.py file.
Answer to TEST 3 is in the script test_3.py file.
Answer to TEST 2 in the file ansible_files

I used docker to run elastic search locally and could not manage to configure it properly. Therefore could not use the package of elasticsearch of python. I used requests library to make http post and get call request to elastic search locally. The ansible assignment is in prototype version, I was not able to test it.

To run the elastic search locally, ensure docker engine is installed. If you're using ubuntu here is the link: https://docs.docker.com/engine/install/ubuntu/ .

For running elastic search locally, you can find the instruction here https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html 
```
docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.10.2
docker run --name elasticsearch --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -t docker.elastic.co/elasticsearch/elasticsearch:8.10.2
```
Ensure that you mention the username and the password generated in the example.ini file to be configured.