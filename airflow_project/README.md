# Apache Airflow Setup using Docker (Windows + VS Code)

This guide explains how to set up **Apache Airflow** using Docker and run DAGs from VS Code.

---

## 📌 Prerequisites

* Docker Desktop installed and running
* VS Code installed

---

## 🚀 Step 1: Download Docker Compose File

Download the official `docker-compose.yaml` from Apache Airflow documentation:

```powershell
Invoke-WebRequest -Uri "https://airflow.apache.org/docs/apache-airflow/3.1.8/docker-compose.yaml" -OutFile "docker-compose.yaml"
```

This file contains all configurations required to run Airflow services (webserver, scheduler, database, etc.).

---

## 📁 Step 2: Create Project Folder Structure

Navigate to your project directory (e.g., `airflow_project`) and create required folders:

```powershell
mkdir dags
mkdir logs
mkdir plugins
mkdir config
```

---

## ⚙️ Step 3: Create `.env` File

Create a `.env` file in the project root and add:

```text
AIRFLOW_UID=50000
```

---

## 🛠️ Step 4: Initialize Airflow Database

Run the following command:

```bash
docker compose up airflow-init
```

After successful execution, you should see:

```text
airflow-init-1 exited with code 0
```

This means:

* Database is initialized
* Default user is created (`airflow / airflow`)

---

## ▶️ Step 5: Start Airflow Services

Start all Airflow services:

```bash
docker compose up -d
```

---

## 🌐 Step 6: Access Airflow UI

Open your browser and go to:

```
http://localhost:8080
```

Login credentials:

* Username: `airflow`
* Password: `airflow`

---

## ✅ Step 7: Verify Running Containers

Check if all services are running:

```bash
docker ps
```

---

## 🔄 Restart Services (if changes not reflected)

```bash
docker compose restart
```

---

## 🧹 Cleanup (Stop and Remove Everything)

```bash
docker compose down --volumes --rmi all
```

---

## ⚡ Docker Command Modes

| Command                | Description                        |
| ---------------------- | ---------------------------------- |
| `docker compose up`    | Runs in foreground (shows logs)    |
| `docker compose up -d` | Runs in background (detached mode) |

👉 `-d` = detached mode (runs containers in background)

---

## 📂 Container Details

Docker creates a container group based on your folder name (e.g., `airflow_project`).

Inside it, you will see multiple containers like:

* airflow-apiserver
* airflow-scheduler
* airflow-worker
* postgres
* redis

---

## 🧪 Running Commands Inside Container

1. Open Docker Desktop
2. Select container (e.g., `airflow-apiserver`)
3. Go to **Exec / Terminal**

---

## 📊 Useful Airflow CLI Commands

### List all DAGs

```bash
airflow dags list
```

### Test a task

```bash
airflow tasks test <dag_id> <task_id>
```

### Test a DAG

```bash
airflow dags test <dag_id>
```

### Trigger a DAG

```bash
airflow dags trigger <dag_id>
```

---

## 📝 Notes

* Place your DAG files inside the `dags/` folder
* Airflow automatically detects new DAGs
* Logs are stored in the `logs/` folder
* If DAGs are not visible, restart services

---

## 🎯 Summary

This setup allows you to:

* Run Apache Airflow using Docker
* Develop DAGs using VS Code
* Execute and monitor workflows via UI

---
