# StealthProxy
## ➡️ A ShadowSocks Implementation 

`StealthProxy` is a simplified implementation for `Shadowsocks(SS)` as a concept proof. Using a simple table mapping to make a traffic confusion.

The program has a client-side and a server-side script.
Running server.py as the main program on the server-side, use the given key, and server address(either IP or hostname) to set up the client-side.

Because SS is using sock5 as the connection between client and server, we need to use a browserplugin or a software to send the traffic to the program.

(E.g [Hotplate localhost SOCKS proxy setup] on chrome or proxifier for systemwide proxy)

## 1️⃣ Environment

Tested in python version 3.8 and 3.10, should be working for python version > 3.6+
Tested under mac and WSL ubuntu.

### Install Typing 

```
pip3 install typing
```
## 2️⃣ Command Instruction

### 🔴 First Time Setup

#### 🔸 Generate key and Start Listening On a Server

When running for the first time, we need to generate a random key for the connection by
using the `-r` option on the server-side and also listen to a connection.

```
python3 server.py -r
```

Sample Output:

```
randomly initial with a password
listening port is 8388
sample command to set up client, replace ip 127.0.0.1 with actual hostname if connected from internet


python3 client.py -l "http://127.0.0.1:8388/#mgOlLP3OmKp5Zrq_co3i_-vMveGvV-045f4xnjKgEvQlkL59hN2oERZveKkOUC-Sl7boufru3NVukSrCH4axPVGdCjbK39eko_nZI_couIjJ9iabO9tq8x6CrYwYj5V-tbxdUgCuSsAp409TwexWaWwNyy77HD7p5ysTn8O3TvIE0LPxGi08NxVfYR1LsKfwTIU_c6GKXnVHJE3EVeZwpmIBzRAZdkVCZNLHRsWrfJbGogwzNQUgz1pjW4uUjhvT2NYnQAk0gPx7D94LMOrvQ1hgAtHkyGt3REGyWSF0BheH-CJnk4Fl1HraSVSJB4MUu3GsbX9o4Ag6tJlc9UicOQ=="


listening
```

#### 🔸 Save the Key

In this sample case, following generated key is what we need to save.

```
mgOlLP3OmKp5Zrq_co3i_-vMveGvV-045f4xnjKgEvQlkL59hN2oERZveKkOUC-Sl7boufru3NVukSrCH4axPVGdCjbK39eko_nZI_couIjJ9iabO9tq8x6CrYwYj5V-tbxdUgCuSsAp409TwexWaWwNyy77HD7p5ysTn8O3TvIE0LPxGi08NxVfYR1LsKfwTIU_c6GKXnVHJE3EVeZwpmIBzRAZdkVCZNLHRsWrfJbGogwzNQUgz1pjW4uUjhvT2NYnQAk0gPx7D94LMOrvQ1hgAtHkyGt3REGyWSF0BheH-CJnk4Fl1HraSVSJB4MUu3GsbX9o4Ag6tJlc9UicOQ==
```

#### 🔸 Setup Client

We can easily copy the generated command to move on create client side, 
subsitude the "127.0.0.1" with the real host url or ip if needed. 

```
python3 client.py -l "http://127.0.0.1:8388/#mgOlLP3OmKp5Zrq_co3i_-vMveGvV-045f4xnjKgEvQlkL59hN2oERZveKkOUC-Sl7boufru3NVukSrCH4axPVGdCjbK39eko_nZI_couIjJ9iabO9tq8x6CrYwYj5V-tbxdUgCuSsAp409TwexWaWwNyy77HD7p5ysTn8O3TvIE0LPxGi08NxVfYR1LsKfwTIU_c6GKXnVHJE3EVeZwpmIBzRAZdkVCZNLHRsWrfJbGogwzNQUgz1pjW4uUjhvT2NYnQAk0gPx7D94LMOrvQ1hgAtHkyGt3REGyWSF0BheH-CJnk4Fl1HraSVSJB4MUu3GsbX9o4Ag6tJlc9UicOQ=="
```

Sample Output:
```
Listen to 127.0.0.1:1080

listening
```

#### 🔸 Install SOCKS5 Proxy  Plug-in Extension 
After successfully finished setting up our server-side and client-side, we can start install a SOCK5 proxy plug-in extension on browser.

We are using a Chrome extension called `Hotplate localhost SOCKS proxy setup`, the installation link is below:
https://chrome.google.com/webstore/detail/hotplate-localhost-socks/odiakldnmmpjabkemfboijigageaelcn?hl=en

We need set the proxy port at 1080 at options:  
<img width="406" alt="Screen Shot 2022-04-13 at 02 07 39" src="https://user-images.githubusercontent.com/39597715/163141695-ca5cf7bd-cf2e-4ac9-9077-d4075b09e8b6.png">

Then right click the extension on the browser, choose `use localhost:1080 SOCKS proxy` to open the SOCK5 proxy.  
<img width="323" alt="Screen Shot 2022-04-13 at 02 09 37" src="https://user-images.githubusercontent.com/39597715/163142055-e9a28446-dfab-433b-9adf-dc11657b4ddd.png">




### 🔴 Normal Setup

#### 🔸 Setup Server 

we can always use -r option to setup the server.

To re-use a previous key, use `-c` option with the key.

For the sample key, the command would look like:
```
python3 server.py -c mgOlLP3OmKp5Zrq_co3i_-vMveGvV-045f4xnjKgEvQlkL59hN2oERZveKkOUC-Sl7boufru3NVukSrCH4axPVGdCjbK39eko_nZI_couIjJ9iabO9tq8x6CrYwYj5V-tbxdUgCuSsAp409TwexWaWwNyy77HD7p5ysTn8O3TvIE0LPxGi08NxVfYR1LsKfwTIU_c6GKXnVHJE3EVeZwpmIBzRAZdkVCZNLHRsWrfJbGogwzNQUgz1pjW4uUjhvT2NYnQAk0gPx7D94LMOrvQ1hgAtHkyGt3REGyWSF0BheH-CJnk4Fl1HraSVSJB4MUu3GsbX9o4Ag6tJlc9UicOQ==
```

#### 🔸 Setup Client

on the client side we can use the link to connect to the server (`-l` option)

```
python3 client.py -l "http://127.0.0.1:8388/#2mM0U4AShkuDUBNOcPMCnTnVDWrDUcAvsaHPR4FPVrWiGJZ23jGkSguQ_1mJ71X1nzYMkW2aX-6TKWAbffq4W2tJshUaeZJyrVTyyuul4-hDzMiK4Fd0qyg6JlqbUqPwzbzHjY5IHbkyJdyHMOr3cSDbNYiCf3xdnhGLwlxvZ2K34SEXdfyPqh8EtrQqAKDU2EDihBa7Rg742a4IK92XrA9NZefLEPY8upn95kw_eyxpetPtXs53Cb_-qaaM0W5FxH7pHMWFlNcDBwHf-dC9FFgtYSenOD2V1iScLq8-wR5BM_SzeMmYCkI7qOz7vuUG8URo0iKwZjdzxhlk5AUjbA=="
```

or setup up the setting with seperate option

```
python3 client.py -sa 127.0.0.1 -c mgOlLP3OmKp5Zrq_co3i_-vMveGvV-045f4xnjKgEvQlkL59hN2oERZveKkOUC-Sl7boufru3NVukSrCH4axPVGdCjbK39eko_nZI_couIjJ9iabO9tq8x6CrYwYj5V-tbxdUgCuSsAp409TwexWaWwNyy77HD7p5ysTn8O3TvIE0LPxGi08NxVfYR1LsKfwTIU_c6GKXnVHJE3EVeZwpmIBzRAZdkVCZNLHRsWrfJbGogwzNQUgz1pjW4uUjhvT2NYnQAk0gPx7D94LMOrvQ1hgAtHkyGt3REGyWSF0BheH-CJnk4Fl1HraSVSJB4MUu3GsbX9o4Ag6tJlc9UicOQ==
```

#### 🔸 Argument Config 

Server and client can both customize options.
`-r` for genreate random password and listening
`-lp` for setting listenport, default to 8388
`-c` for reuse connect key


On the client side
`-lp` for listening port,default to 1080
`-sa` is the option for server's address 
`-sp` is the option for server's port, default to 8388
`-c` for reuse connect key

Sample usage with customized config
server

```
python3 server.py -lp 8500 -c uRhcztzSfInXsiW1-KbNv9Otqwl-R5_9_gpdPmuP5L381spaBstxKBIOdeGxKusVYu6GT91AL7dvRi7VKWGASca7MJmLmIFYlw9IuGaomz0b7JRS0RExusSqwXm2M8IIiufIE-_tAVaEkgM3qSFDnAWvMh_Q95ZL6qxtZWxygy1KjebeHg1NpXj5rn81jjaVo1R3Xp5qkbMWJFuTPPL7oSfPWaRVc3q-OZ3H2xzUiPMZYOL1guCnDPHl-iAjFMB2yZpnsOig32jjRFNCzFE7AH2FBAsrGofDHVdQInRfTBBw2jh72fQHbgI0xdj_P_YsjPA6Yxe0kEUmZKK86WlOQQ==
```

client

```
python3 client.py -sa 127.0.0.1 -sp 8500 -lp 1100 -c uRhcztzSfInXsiW1-KbNv9Otqwl-R5_9_gpdPmuP5L381spaBstxKBIOdeGxKusVYu6GT91AL7dvRi7VKWGASca7MJmLmIFYlw9IuGaomz0b7JRS0RExusSqwXm2M8IIiufIE-_tAVaEkgM3qSFDnAWvMh_Q95ZL6qxtZWxygy1KjebeHg1NpXj5rn81jjaVo1R3Xp5qkbMWJFuTPPL7oSfPWaRVc3q-OZ3H2xzUiPMZYOL1guCnDPHl-iAjFMB2yZpnsOig32jjRFNCzFE7AH2FBAsrGofDHVdQInRfTBBw2jh72fQHbgI0xdj_P_YsjPA6Yxe0kEUmZKK86WlOQQ==
```


## 3️⃣ Test Case
### 🔺 Test Case 1 -> Connect though random password and default link on the client side, and inspect the traffic
#### 🔸 a.Download the repo on the machine, make sure to install python3(>3.6), typing module and [SOCKS5 Proxy  Plug-in Extension]. 
#### 🔸 b.Navigate to the root of the repo, run server.py script to generate random key.
```
python3 server.py -r
```

<img width="800" src="https://user-images.githubusercontent.com/32621871/163287324-433f85e4-6690-4dad-a100-431ad60975e3.png"> 

#### 🔸 c.Open a second terminal, copy the suggested command and open on it.
sample command
```
python3 client.py -l "http://127.0.0.1:8388/#2mM0U4AShkuDUBNOcPMCnTnVDWrDUcAvsaHPR4FPVrWiGJZ23jGkSguQ_1mJ71X1nzYMkW2aX-6TKWAbffq4W2tJshUaeZJyrVTyyuul4-hDzMiK4Fd0qyg6JlqbUqPwzbzHjY5IHbkyJdyHMOr3cSDbNYiCf3xdnhGLwlxvZ2K34SEXdfyPqh8EtrQqAKDU2EDihBa7Rg742a4IK92XrA9NZefLEPY8upn95kw_eyxpetPtXs53Cb_-qaaM0W5FxH7pHMWFlNcDBwHf-dC9FFgtYSenOD2V1iScLq8-wR5BM_SzeMmYCkI7qOz7vuUG8URo0iKwZjdzxhlk5AUjbA=="
```
<img width="400" src="https://user-images.githubusercontent.com/32621871/163287403-e45e5f70-b724-4972-a3cf-6b06bac5bced.png"> 

#### 🔸 d. Open a chrome browser, make sure the plugin is using 1080 as the port, change the setting if it's using a different port by right click on the icon and select option.  

<img width="300" src="https://user-images.githubusercontent.com/32621871/163290150-1a7d09cc-0b54-4bb2-bacc-fca004167716.png">   
<img width="400" src="https://user-images.githubusercontent.com/32621871/163287691-21dc9c7b-8340-478f-9033-df97cc709151.png">  

Then right click the extension on the browser, choose `use localhost:1080 SOCKS proxy` to open the SOCK5 proxy.  

<img width="300" alt="Screen Shot 2022-04-13 at 02 09 37" src="https://user-images.githubusercontent.com/39597715/163142055-e9a28446-dfab-433b-9adf-dc11657b4ddd.png">

#### 🔸 f. check if the browser still connecting to the internet, if yes the browser works.

<img width="400" src="https://user-images.githubusercontent.com/32621871/163290034-4f75e143-4a77-4ef8-a65e-4a2c9c044086.png">

You can capture the trrafic on wireshark, because for this test case server and client are on the same machine, the traffic exist in the loopback traffic capture and we can see sock5 connection and trrafic from 1080 and 8388. 

<img width="600" src="https://user-images.githubusercontent.com/32621871/163290541-476f500e-ce73-4036-a0a0-b0cd7de36972.png">

### 🔺 Test Case 2 -> Connect with customize setting
#### 🔸 a. Use command for custom setting
```
python3 server.py -lp 8500 -c uRhcztzSfInXsiW1-KbNv9Otqwl-R5_9_gpdPmuP5L381spaBstxKBIOdeGxKusVYu6GT91AL7dvRi7VKWGASca7MJmLmIFYlw9IuGaomz0b7JRS0RExusSqwXm2M8IIiufIE-_tAVaEkgM3qSFDnAWvMh_Q95ZL6qxtZWxygy1KjebeHg1NpXj5rn81jjaVo1R3Xp5qkbMWJFuTPPL7oSfPWaRVc3q-OZ3H2xzUiPMZYOL1guCnDPHl-iAjFMB2yZpnsOig32jjRFNCzFE7AH2FBAsrGofDHVdQInRfTBBw2jh72fQHbgI0xdj_P_YsjPA6Yxe0kEUmZKK86WlOQQ==
```
```
python3 client.py -sa 127.0.0.1 -sp 8500 -lp 1100 -c uRhcztzSfInXsiW1-KbNv9Otqwl-R5_9_gpdPmuP5L381spaBstxKBIOdeGxKusVYu6GT91AL7dvRi7VKWGASca7MJmLmIFYlw9IuGaomz0b7JRS0RExusSqwXm2M8IIiufIE-_tAVaEkgM3qSFDnAWvMh_Q95ZL6qxtZWxygy1KjebeHg1NpXj5rn81jjaVo1R3Xp5qkbMWJFuTPPL7oSfPWaRVc3q-OZ3H2xzUiPMZYOL1guCnDPHl-iAjFMB2yZpnsOig32jjRFNCzFE7AH2FBAsrGofDHVdQInRfTBBw2jh72fQHbgI0xdj_P_YsjPA6Yxe0kEUmZKK86WlOQQ==
```

<img width="600" src="https://user-images.githubusercontent.com/32621871/163300297-23ad4346-7a8b-4155-a8b5-5f7dfb9d6ccb.png">

#### 🔸 b. Change port on the proxy plugin to 1100

<img width="300" src="https://user-images.githubusercontent.com/32621871/163300369-fa74c772-d7f6-46fd-9892-7bc3c76d4ab6.png">

#### 🔸 c. Check if the browser can successfully connected to a website

<img width="500" src="https://user-images.githubusercontent.com/32621871/163300469-2f16aaa0-8024-4ca3-887c-c637945e51cc.png">

### 🔺 Test Case 3 -> Tested successfully on a different machine

Sample:
server is on another machine with ip 192.168.50.117
```
python3 client.py -l "http://192.168.50.117:8388/#fILiEd4psTfK4ypE5Wo4HBpOQYRwhUXr_wO8ujv3Fo06rU3yjCIvcxjG6m1aiwy2Tyty17WABigJkT8mXM1e8DZRW2b8S5PWFaLmwSWl1W-ma0AtuF3pMmeWC9mgI8KnecWk88u53cljSe67flIO9LLsUFWYn4l_j_4wCFT4HTGzLFj5E4psx9Azo2TI3AJpF4gN3zV6xL3gmQBCRo6BlR4UX6kkB9MBYEf2qHHtYko075eQezlW-9Ksm5znzy6wGZpDWQXbwwqhH799eASdIfqS9eGqDzy-_WV0tOg9nq_OG9hMEJR1aKvkdq4ng9p38bfM1CDAboY-0UhhEleHUw=="
```

<img width="600" src="https://user-images.githubusercontent.com/32621871/163301044-cb054573-27af-4a30-88e6-1a5cf3dcd7a4.png">


## 4️⃣ Known Issues and Bugs
1. On python version3.10, showing error message `gather() got an unexpected keyword argument 'loop'`. The program is still functioning.
on windows with python 3.10 shows handling error but still able to connect.

2. We use a preset mapped cipher, which is weak encryption and is easily attackable in the real world, such as a replay attack. 
 
3. It is also comparatively slow for multiple HTTP requests. 



