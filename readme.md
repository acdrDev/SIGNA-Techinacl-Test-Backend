# API (Python - Flask)

## Setup
### Docker
- Rename ".env.example" file to ".env" and fill variebles
  > Note: DB_HOST is "localhost" or "127.0.0.1"
- Execute
  ```bash
  docker-compose up
  ```
- Now execute
  ```bash
  python Migration.py
  ```
  or

  ```bash
  python3 Migration.py
  ```
- Go to "http://localhost:5000" or "http://127.0.0.1" for see page

### Without docker
- Rename ".env.example" file to ".env" and fill variebles with your database information
- Execute
  ```bash
  python Migration.py
  ```
  or

  ```bash
  python3 Migration.py
  ```
- Run
  ```bash
  python app.py
  ```
  or

  ```bash
  python3 app.py
  ```
- Go to "http://localhost:5000" or "http://127.0.0.1" for see page