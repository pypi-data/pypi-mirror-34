# Microservices Connector
Microservices Connector is a Inter-Service communication framework, support for microservice architecture and distributed system.

## Getting Started

__Microservices__ is a way of breaking large software projects into loosely coupled modules, which communicate with each other through simple APIs. The advantages of microservices are improves fault isolation, scalability, Ease of development. It convinced some big enterprise players – like Amazon, Netflix, and eBay – to begin their transitions. 

_Microservices Connector_ is a Inter-Service communication framework written in python, support for microservice architecture and distributed system. Its features contain:
* Transfering data as returning a function results or quering data.
* Support transfer multiple values with many type as string, int, float, list, dict, class attribute
* Do not require knowledge about web/http connection or touch to them
* Distributed system

![alt text](images/Distributed-system.jpeg  "Illustration of network system. Source:medium.com")

Illustration of network system. Source:medium.com

As illustration, distributed systems are very stable and Infinite scalability. But distributed systems are the most difficult to maintain.

_Microservices Connector_ supports communication by the following framework:
* flask - A micro web framework
* Sanic - Gotta go fast (A async web framework)
### Quickstart:

Microservices Connector is available on pip. You can install via pip (require python>=3.5):

```
pip install microservices_connector
```
Start project by a minimum example: 

* Step 1: Create 1 file name app1.py, write and save with the code below

```python
from microservices_connector.Interservices import Microservice

Micro = Microservice(__name__)

@Micro.typing('/helloworld')
@Micro.reply
def helloworld(name):
    return 'Welcome %s' % (name)

if __name__ == '__main__':
    Micro.run()
```

* Step 2: Create 1 file name app2.py, write and save with the code below

```python
from microservices_connector.Interservices import Friend

aFriend= Friend('app1', 'http://0.0.0.0:5000')
message = aFriend.send('/helloworld','Mr. Developer')
print(message)
```
* Step 3: Run app1.py and app2.py together.

Open a terminal in the same folder with them and run:
`python app1.py`.

Open another terminal in the same folder and run:
`python app2.py`

You get the result: `Welcome Mr. Developer` in terminal of app2.py. This is no difference if you do `from .app1 import helloword; message = helloworld('Mr. Developer'); print(message)`. Note: To stop app1, open its terminal and Ctrl + C. The example can be found in `test/example00` folder

**Explanation**: App1 and app2 are small example of microservice system. In the example, **M** in app1 is listener, a http server while __F__ in app2 is sender. Listener and sender are isolated design, they can work seperately or together in an app/service. A microservice can be a listener of many other microservices or sender of many other microservices or both of them. A standard microservice mention in this project contain both listener and sender.

## Tutorial

### 1. Start your first app

In the tutorial, we assume you have this code in the top of your file.

```python
from microservices_connector.Interservices import Microservice

Micro = Microservice(__name__)

# for Sanic framework if you want to use sanic instead of flask
from microservices_connector.Interservices import SanicApp as Microservice

Micro = Microservice(__name__)
```

Now, look closer at `Microservice(__name__)`, it actually look like this: 
    
    Microservice(name, port: int=5000, host: str='0.0.0.0', debug=None, token: dict = {}, secretKey=None)
    
Arguments:
* name {str} -- Require a name for your app, recommend put `__name__` for it
* port {int} -- Choose from 3000 to 9000, default to 5000
* host {str} -- Host ip, Default 0.0.0.0 for localhost
* debug {boolean} -- True for development, False/None for production
* token {dict} -- A dict contain all rule and its token. It can be set later

The class Microservice is used to create a listener/a microservice. In a file/app, you should only have one listener. About parameters, If you aren't familiar with http server, you only need remember:
* One app should have only one listener
* Should use `__name__` for name and name need to be unique
* If you run multiple listener, use only one unique port for each listener. for example:

```python
M1 = Microservice(__name__, port=5010) # in file app1
M2 = Microservice(__name__, port=5020) # in file app2
```
Note: You should be carefully if there are other web applications running in your port/server.

### 2. Way of running an app

A sender is a python def, so you can put it anywhere in your app. Listener is a http server so it's a bit difference from other.

Option 1: Use if/main in the end of startup file (file that you start your project by `python <filename>`). Add the following code the end:
```python
# Micro is your Microservice Object
if __name__ == '__main__':
    Micro.run()
```

Option 2: Create a file name run.py and run your app from this file. For example, we create a run.py in the same folder of app1.py in the first example. It will be like this:
```python
from app1 import Micro

if __name__ == '__main__':
    Micro.run(port=5000, host='0.0.0.0', debug=True)
```
Option 2 is more appreciated. It avoid the app looping from them self, so get away of stunning your app. If you have 2 app in a server/computer, you should create 2 run file for it. Don't for get `Ctrl + C` to stop your app.

Note: _We assume you already use one of the options above for your code_. This tutorial focuses on communication between 'service-to-service' as def function, not http connect.

### 3. Send, Typing and reply

Think like a human, if you want to communicate with some friend in facebook, you will open *messenger*, find your friend and send a message to them. It's a way of sending message to each other. Then, your friend will type a message and reply you. The process is similar here. See the code:
```python
aFriend= Friend('Corgi', 'http://0.0.0.0:5000') # this is: you're finding friend in your head. 
# You can call him with a cute name like 'Puppy','Teddy' or 'Corgi'. 
# But you must always remember his real-name is 'http://0.0.0.0:5000' to know actually who he is

message = aFriend.send('/helloworld','Mr. Close friend') # then you can send him a message
```

`/helloworld` is the rule/topic you say/ask to a friend or the route in http. It need to start with `/`. The rule must match with the rule of `Typing` to be replied. `Mr. Close friend` is what you are talking about, which can be string, integer, float, list, dict or class. For example: `aFriend.send('/topic',variable1, variable2, keyword1='secret key')`

In other side, your friend or a microservice or a listener has the following process:
```python
@Micro.typing('/helloworld') # this is the rule/topic he knows. If he don't know, he cannot reply
@Micro.reply # he is replying
def helloworld(name): # this is the process in side his head
    return 'Welcome %s' % (name) # the answer
```

`@Micro.typing` - The rule/topic must exactly match with the topic was sent and should startwith "/". The `@Micro.reply` must come before def. Then, Microservice handles the remain. Next chapter is about returning data

### 4. Send and reply string, integer, float

In the sender side, you can send data type as the code below:
```python
print(
    """##############################
    Test return string
    """)
aFriend= Friend('app1', 'http://localhost:5000')
print('Test: return a simple string')
x = aFriend.send('/str', 'A variable value', key='A keyword variable value')
print('x=', x, type(x))
print('==========================')
print('Test: return multiple string')
x, y, z = aFriend.send('/str2', 'A variable value',
                key='A keyword variable value')
print('x=' ,x, type(x))
print('y=', y, type(y))
print('z=', z, type(z))

print(
    """##############################
    Test return a int, float
    """)
aFriend= Friend('app1', 'http://localhost:5000')
print('Test: return a simple Value')
x = aFriend.send('/int', 2018, key=312)
print('x=', x, type(x))
print('==========================')
print('Test: return a simple Value')
x = aFriend.send('/float', 2.018, key=3.12)
print('x=', x, type(x))
print('==========================')
print('Test: return multiple Value')
x, y, z = aFriend.send('/int3', 3.1427,
                    key=1000000000)
print('x=', x, type(x))
print('y=', y, type(y))
print('z=', z, type(z))
```
In the listener, you can reply/return data type as string, integer, float as below:
```python
# run a normal function in python
print('one cat here')

# return string
@Micro.typing('/str')
@Micro.reply
def string1(a,key):
    return a+'-'+key

# return multiple string
@Micro.typing('/str2')
@Micro.reply
def string2(a, key):
    return a, key, a+'-'+key

# return Integer and float
@Micro.typing('/int')
@Micro.reply
def int1(a, key):
    return a+key

@Micro.typing('/float')
@Micro.reply
def float2(a, key):
    return a+key


@Micro.typing('/int3')
@Micro.reply
def int3(a, key):
    return a+key, key*key, a*a
```
After that, first run listener then run sender. We have results (see example01):
```
Test: return a simple string
x= A variable value-A keyword variable value <class 'str'>
==========================
Test: return multiple string
x= A variable value <class 'str'>
y= A keyword variable value <class 'str'>
z= A variable value-A keyword variable value <class 'str'>
'testStr'  23.17 ms
Test: return a simple Value
x= 2330 <class 'int'>
==========================
Test: return a simple Value
x= 5.138 <class 'float'>
==========================
Test: return multiple Value
x= 1000000003.1427 <class 'float'>
y= 1000000000000000000 <class 'int'>
z= 9.87656329 <class 'float'>
```
Note: print('one cat here') print in the screen of listener. You can run any other python function, python code as normal in listener.

### 5. Send and reply list, dict

In the sender side, you can send data type as the code below:
```python
print(
    """##############################
    Test return a list, dict
    """)
aFriend= Friend('app1', 'http://localhost:5000')
print('Test: return a simple Value')
x = aFriend.send('/list', [12,34,45], key=['abc','zyz'])
print('x=', x, type(x))
print('==========================')
print('Test: return a simple Value')
x = aFriend.send('/dict', {'keyword':['anything']}, key={'int':20,'str':'adfafsa','float':0.2323})
print('x=', x, type(x))
print('==========================')
print('Test: return multiple Value')
x, y, z = aFriend.send('/list3', {'keyword': ['anything']},
                    key=['abc', 'zyz'])
print('x=', x, type(x))
print('y=', y, type(y))
print('z=', z, type(z))
```
In the listener, you can reply/return data type as string, integer, float as below:
```python
# test return list and dict
@Micro.typing('/list')
@Micro.reply
def list1(a, key):
    a.extend(key)
    return a


@Micro.typing('/dict')
@Micro.reply
def dict1(a, key):
    key['dict'] = a
    return key


@Micro.typing('/list3')
@Micro.reply
def list3(a, key):
    key.append('other value')
    c = None
    return a, key, c
```
After that, first run listener then run sender. We have results (for full example see tests/example01):
```
Test: return a simple Value
x= [12, 34, 45, 'abc', 'zyz'] <class 'list'>
==========================
Test: return a simple Value
x= {'dict': {'keyword': ['anything']}, 'float': 0.2323, 'int': 20, 'str': 'adfafsa'} <class 'dict'>
==========================
Test: return multiple Value
x= {'keyword': ['anything']} <class 'dict'>
y= ['abc', 'zyz', 'other value'] <class 'list'>
z= None <class 'NoneType'>
'testListDict'  22.19 ms
```

### 6. Send and reply void, Nonetype, class attributes and use of token
In the sender side, you can send data type as the code below:

```python
print(
"""##############################
Test return NoneType, Class, use of Token
""")
aFriend= Friend('app1', 'http://localhost:5000')
print('Test: return a simple Value')
x = aFriend.send('/None', [12, 34, 45], key=['abc', 'zyz'])
print('x=', x, type(x))
print('==========================')
print('Test: return a simple Value with token')
aFriend.setRule('/class', token='123456')
x = aFriend.send('/class', {'keyword': ['anything']},
            key={'int': 20, 'str': 'adfafsa', 'float': 0.2323})
print('x=', x, type(x))
print('==========================')
print('Test: return multiple Value')
aFriend.setRule('/class2', token='123456')
x,y,z = aFriend.send('/class2', {'keyword': ['anything']},
            key={'int': 20, 'str': 'adfafsa', 'float': 0.2323})
print('x=', x, type(x))
print('y=', y, type(y))
print('z=', z, type(z))

# Test send class and list of class object
print('\n Test: send class and list of class object')
aFriend.setRule('/class3', token='123456')
t1 = testservice('value1')
t2 = testservice('value2')
x, y, z = aFriend.send('/class3', [t1,t2],
                    key={'t1': t1, 't2': t2, 'list': [t1, t2]})
print('x=', x, type(x))
print('y=', y, type(y))
print('z=', z, type(z))
```

In the listener, you can reply/return data type as string, integer, float as below:

```python
# return None, class Object
@Micro.typing('/None')
@Micro.reply
def TestNoneValue(a, key):
    key.append('Do something in the server')

class testservice(object):
    name = 'test'
    Purpose = 'For test only'
    empty = None
    def __init__(self, value):
        self.value = value

    def onemethod(self):
        pass


@Micro.typing('/class',token='123456')
@Micro.reply
def TestClass(a, key):
    t = testservice(a)
    return t


@Micro.typing('/class2', token='123456')
@Micro.reply
def TestClass2(a, key):
    t = testservice(key)
    return t, a, None

@Micro.typing('/class3', token='123456')
@Micro.reply
def TestClass3(a, key):
    x = testservice(key)
    y = testservice(a)
    z = [y,x]
    return x, y, z 
```
After that, first run listener then run sender. We have results (for full example see tests/example01):

```
##############################
Test return NoneType, Class, use of Token

Test: return a simple Value
x= None <class 'NoneType'>
==========================
Test: return a simple Value with token
x= {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': {'keyword': ['anything']}} <class 'dict'>
==========================
Test: return multiple Value
x= {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': {'float': 0.2323, 'int': 20, 'str': 'adfafsa'}} <class 'dict'>
y= {'keyword': ['anything']} <class 'dict'>
z= None <class 'NoneType'>

Test: send class and list of class object
x= {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': {'list': [{'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value1'}, {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value2'}], 't1': {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value1'}, 't2': {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value2'}}} <class 'dict'>
y= {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': [{'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value1'}, {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value2'}]} <class 'dict'>
z= [{'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': [{'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value1'}, {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value2'}]}, {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': {'list': [{'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value1'}, {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value2'}], 't1': {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value1'}, 't2': {'Purpose': 'For test only', 'empty': None, 'name': 'test', 'value': 'value2'}}}] <class 'list'>
'testClassType'  19.20 ms
```

New feature from 0.2.4, now you can send and receive json similar to dict. It helps more readable response

```python
# in client side
print('=================Response json===============')
x = aFriend.json('/json', a=12,b='This is a text',c={'dict':'a dict'})
print('Synchonous POST:', x)
y = aFriend.json('/json1', method='GET' , a={'dict': 'a only dict'})
print('Asynchonous GET:', y)
z = aFriend.json('/json1', a={'dict': 'a only dict'})
print('Asynchonous POST:', z)
```
In the server side we have:

```python
# in server side
@Micro.typing('/json')
@Micro.json
@timeit
def TestReceiveJson(a=1, b='string',c=None):
    return {'1':a,'2':b,'3':c}


# for async request (only apply to sanic)
@Micro.route('/json1', methods=['GET','POST'])
@Micro.async_json
async def TestReceiveJson2(a=None):
    return a
```

You can response with get, post, put, delete,... as the method above. The result:

```
=================Response json===============
Synchonous POST: {'1': 12, '2': 'This is a text', '3': {'dict': 'a dict'}}
Asynchonous GET: {'dict': 'a only dict'}
Asynchonous POST: {'dict': 'a only dict'}
```
### 7. From 0.2.7, we support for websocket connection:
In the sender side, we can send data type as the code below:

```python
from microservices_connector.minisocket import SocketServer
sk = SocketServer(__name__)
@sk.router('/hello')
def test(message):
    print(message)
    return 'ok:'+message

def main():
    sk.run()
    # you can put a flask server here
    # Socket Server run in a seperate threads, not affect flask server

if __name__ == '__main__':
    main()
```
The other option is run minisocket in a different thread, that will alow flask server run seperately.

```python
sk = SocketServer(__name__)
app = Microservice('Flask_app').app

@app.route('/')
def helloworld():
    time.sleep(2)
    return 'Sleep 2s before response'


@sk.router('/hello')
def test(message):
    print(message)
    return 'ok:'+message

def socket_runner():
    sk.run()

def main():
    socket_runner()
    print('start web framework')
    app.run()


if __name__ == '__main__':
    main()

```

In the client side, we create a socket connection using websocket framework:

```python
import asyncio
import websockets


async def hello():
    async with websockets.connect('ws://localhost:8765/hello') as websocket:
        name = input("What's your name? ")
        await websocket.send(name)
        print(f"> {name}")
        greeting = await websocket.recv()
        print(f"< {greeting}")
        while greeting != 'close':
            name = input("What's your name? ")
            await websocket.send(name)
            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
```
### 8. From 0.2.7, we support concurrency process with sequences throught DistributedThreads and DistributedProcess :

This give a solution for the problems of concurrency process that many workers simutanously impact/input to a single database row/table/position or the problem of arbitrary order of data. 
First, if you don't need process a data or queue with order or your data do not input to the same database row/table, you should use celery or other framework to scale your project. For that instance, this framework will provide no more efficient than celery which highly use by now.
Second, framework need a key for each row/item in data for knowning which want to be ordered. The guide as example below. You need a output_queue for listening the result and continue other function.

```python
from microservices_connector.spawn import DistributedThreads, DistributedProcess, Worker
import random
import time
import queue
import threading
import multiprocessing

def wait_on_b(b):
    time.sleep(random.random())
    # b will never complete because it is waiting on a.
    print('working on b=%s' % b)
    return 'working on b=%s' % b
    # return 5


def wait_on_a(a):
    time.sleep(1)
    # a will never complete because it is waiting on b.
    return 'working on a=%s' % a
    # return 6

# example data
poll = [
    {'id': 1, 'x': 'Nguyen'},
    {'id': 1, 'x': 'Minh'},
    {'id': 1, 'x': 'Tuan'},
    {'id': 2, 'x': 'Vu'},
    {'id': 3, 'x': 'Ai do khac'},
    {'id': 2, 'x': 'Kim'},
    {'id': 2, 'x': 'Oanh'},
    {'id': 4, 'x': '1'},
    {'id': 4, 'x': '2'},
    {'id': 4, 'x': '3'},
    {'id': 4, 'x': '4'},
    {'id': 4, 'x': '5'},
    {'id': 4, 'x': '6'},
    {'id': 4, 'x': '7'},
    {'id': 4, 'x': '8'},
    {'id': 5, 'x': '101'},
    {'id': 5, 'x': '102'},
    {'id': 5, 'x': '103'},
    {'id': 5, 'x': '104'},
    {'id': 5, 'x': '105'},
    {'id': 6, 'x': 'Test watching'},
    {'id': 6, 'x': 'Test watching'},
    {'id': 7, 'x': 'Test watching'},
    {'id': 8, 'x': 'Test watching'},
    {'id': 9, 'x': 'Test watching'},
    {'id': 10, 'x': 'Test watching'},
    {'id': 11, 'x': 'Test watching'},
    {'id': 12, 'x': 'Test watching'},
    {'id': 13, 'x': 'Test watching'},
    {'id': 14, 'x': 'Test watching'},
    {'id': 15, 'x': 'Test watching'},
    {'id': 16, 'x': 'Test watching'},
    {'id': 17, 'x': 'Test watching'},
    {'id': 18, 'x': 'Test watching'},
    {'id': 19, 'x': 'Test watching'},
    {'id': 20, 'x': 'Test watching'},
    {'id': 21, 'x': 'Test watching'},
    {'id': 22, 'x': 'Test watching'},
]
def main():
    start = time.time()

    thread_out_queue = queue.Queue()
    pool = DistributedThreads(
        max_workers=4, max_watching=100, out_queue=thread_out_queue)
    for item in poll:
        pool.submit_id(item['id'], wait_on_a, item)
    t = Worker(thread_out_queue, print)
    t.daemon = True
    t.start()
    pool.shutdown()
    print('Finish after: ', time.time()-start, 'seconds')

    print("========= End of threads ==============")

    process_out_queue = multiprocessing.Queue()
    pool2 = DistributedProcess(
        max_workers=4, max_watching=100, out_queue=process_out_queue)
    for item in poll:
        pool2.submit_id(item['id'], wait_on_b, item)
    pool2.shutdown()

    print('Finish after: ', time.time()-start, 'seconds')


if __name__ == '__main__':
    main()
```

As the result, all name and number will same id will print in the exact order. Max watching should not be lesser than 100. If you put key/id to None or use submit instead of submit_id, it will do no order but faster.

A Detail User Guide will comming soon...
## Pros vs Cons and question
From my opinion only, Microservice connector has the following Pros and Cons to improve
### Pros:
* Ease of use, Ease of development, you don't need to touch on http connection
* Can build decentralize or Distributed system with Infinite scalability
* Send and receive data with many types as string, int, float, list, dict.
* Connect all around the world with internet

### Cons:
* Do not support send/receive tuple and set type (because I don't like them).
* Do not support send/receive a whole class, return of decorator and server-side computer
* Is not really fast log-broker server as RabbitMQ, ZeroMQ, kafka: *yes, oneService cannot send 10 million message per second like them, but it has other advance.*
* Do not support Database, user/role management, system manager: *not yet, we are trying to write new feature include them. We welcome any contributor support us.*

### Question:
* Why not a load balancer ?

> *It is out of range. Load balancer cover the other layer. Other package can handle it better. But we consider to add a custom function for it.*

* What about support more options, async/await ?

> *We are trying to connect by Sanic and Japronto soon*

* What about data integrity, blockchain, token ?

> *We are trying to add them, but cannot be soon*

## Authors

* **Tuan Nguyen Minh** - *Financer and Developer* - email: ntuan221@gmail.com

Thank for the frameworks and their authors:
* flask - micro webframework
* Sanic - Gotta go fast
* requests

Favourite idioms:
* Don't repeat your self
* Think like human, make for human
* Simple is stronger
## License: BDS license