### Readme.md for Functional HTTP Web Server - PA1 - COEN 317

A Python HTTP web server based on socket and thread library
  
- **High-level Description:**  

  This web server listens for connections on a socket bounded to a port assigned by client on localhost. Clients can connect to this server and retrieve text, image files, html files from the server using GET method. The server also supports multiple threads enabling different ports of clients using a multi-threading approach in Python.
  
  
- **List of Submitted Files:**

    ├── README.pdf

    ├── Request Log.md 

    ├── Running instructions.md

    ├── config.json

    ├── files *Storing jpg and pngs*

    │   ├── basketballfans.jpg

    │   ├── campaignbanner.png
        
    .......
        
    │   └── strangerthings.png

    ├── html *Storing the main index*

    │   └── index.html

    └── server.py *Main Server*



- **Instructions on how to run my program:**

  `cd [folder direction]`
  
   `python3 server.py [port name between 8000-9000]`
   
  
   
- **Snapshots of how web servers accessing my server:**

  <img width="1440" alt="截屏2022-10-12 上午7 04 49" src="https://user-images.githubusercontent.com/20860329/195367254-ffac77ea-1943-45d9-89fd-ff8e59a7dc2b.png">
  
  <img width="1440" alt="截屏2022-10-12 上午7 02 27" src="https://user-images.githubusercontent.com/20860329/195367292-448b6078-906b-4b01-9f7f-8433be6f7b2b.png">




- **References:**

  https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842
  
  https://github.com/arseniyturin/python-webserver
  
  https://drkbl.com/posts/socket-web-server-with-multithread-in-python/
  
  https://www.positronx.io/create-socket-server-with-multiple-clients-in-python/

