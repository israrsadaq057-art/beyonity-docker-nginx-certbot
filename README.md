# Beyonity Docker Nginx Certbot Artist Portal

## IT Administrator
**Israr Sadaq**  
CCNA | CCNP | Master in Information and Communication Engineering  
Email: israrsadaq057@gmail.com  
GitHub: https://github.com/israrsadaq057-art  

---

## Project Overview

Containerized artist portal for Beyonity using Docker Compose with Nginx reverse proxy, Flask web application, and Certbot SSL automation. Artists can upload, download, and delete 3D assets stored in AWS S3.

---

## Architecture

```mermaid
flowchart LR
    A[Browser] --> B[Nginx : 80/443]
    B --> C[Flask : 5000]
    C --> D[AWS S3]
    B --> E[Certbot SSL]
```

---

## Docker Compose Services

| Service | Container        | Port     | Purpose              |
|--------|------------------|----------|----------------------|
| Flask  | beyonity-flask   | 5000     | Python web app       |
| Nginx  | beyonity-nginx   | 80, 443  | Reverse proxy        |
| Certbot| beyonity-certbot | -        | SSL automation       |

---

## Features

- Multi-container orchestration with Docker Compose  
- Nginx reverse proxy routing to Flask  
- Certbot automatic SSL certificate renewal  
- Container networking between services  
- 16 artist login system  
- Upload, download, delete files from S3  
- Professional UI with glassmorphism design  

---

## Artists

```
anna, ben, carla, david, elena, felix, grace, henry,
irena, jonas, karla, lukas, mona, niklas, olivia, paul
```

---

## File Structure

```bash
beyonity-docker-nginx-certbot/
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── requirements.txt
├── app.py
├── templates/
│   ├── login.html
│   └── dashboard.html
├── certbot/
│   ├── conf/
│   └── www/
└── README.md
```

---

## Quick Start

```bash
git clone https://github.com/israrsadaq057-art/beyonity-docker-nginx-certbot.git
cd beyonity-docker-nginx-certbot
docker-compose build
docker-compose up -d
docker-compose ps
```

---

## Verification Commands

```bash
docker ps
docker-compose ps
docker logs beyonity-flask --tail=20
curl http://localhost
```

---

## Skills Demonstrated

| Skill           | Implementation                  |
|----------------|--------------------------------|
| Docker         | Containerized Flask app        |
| Docker Compose | Multi-container orchestration  |
| Nginx          | Reverse proxy configuration    |
| Certbot        | SSL certificate automation     |
| Flask          | Python web framework           |
| AWS S3         | Cloud storage                  |
| Boto3          | AWS SDK                        |

---

## ScreenShots

---
## Running Docker Compose

 <img width="1920" height="1080" alt="docker compose verification update" src="https://github.com/user-attachments/assets/0d7ac563-0845-4fdd-bea4-cc0ef8e1f7ae" />

## Simple Portal for Artists

<img width="1920" height="1080" alt="simple artist portal can be improved" src="https://github.com/user-attachments/assets/5d852ae8-ffd4-4eef-9006-ed69b627c8a3" />

## Installing Python in EC2 Instance

<img width="1920" height="1080" alt="Installing python in EC2 instance" src="https://github.com/user-attachments/assets/290a1c01-a99d-4592-b4d1-c90febf3dbab" />

## Running NGINX

<img width="1920" height="1080" alt="VERIFICATION NGINX IS RUNNING" src="https://github.com/user-attachments/assets/8c0537eb-1110-4bb6-b28c-2c6b94c37ddf" />


## Ading HTTPS-HTTP Port to Security Group

<img width="1920" height="1080" alt="ADDING HTTP_HTTPS PORTS TO SECURITY GROUP" src="https://github.com/user-attachments/assets/f96f4ff7-ecaf-4054-bf1d-2a43259a4bee" />

