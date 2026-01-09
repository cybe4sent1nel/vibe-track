# Vibetrack — TaskTracker

<img src="img/blue-check.svg" alt="Vibetrack" width="48" />

Vibetrack (TaskTracker) is a lightweight static frontend that demonstrates a simple task tracker and includes example serverless API handlers.

Quick links
- Frontend: [frontend/index.html](frontend/index.html)
- API folder: [api/](api/) — Lambda handlers and a local mock server

Local quick start

1) Start the mock API server (Node.js required):

```powershell
cd api
npm install
npm start
```

The mock server listens on `http://localhost:3000` and exposes the same endpoints used by the client.

2) Serve the frontend (from project root):

```powershell
python -m http.server 8000
```

3) Open the app: `http://localhost:8000/frontend/index.html`

Client API
- The client wrapper is in `js/api.js`. It exposes `TaskAPI.createTask`, `TaskAPI.getTasks`, and `TaskAPI.deleteTask`.
- To point the client at a different backend, edit `API_BASE` at the top of `js/api.js`.

API (mock & Lambda)
- POST `/tasks` — create task. Request JSON: `{ "taskId": "id-123", "description": "Do something" }`
	- Example curl:

```bash
curl -X POST http://localhost:3000/tasks \
	-H "Content-Type: application/json" \
	-d '{"taskId":"task-1","description":"Buy milk"}'
```

- GET `/tasks` — returns `{ count, tasks }`.

- DELETE `/tasks/:id` — deletes a task by id.

Serverless Lambdas
- The `api/` folder contains AWS Lambda-compatible handlers (Python):
	- [api/create_task.py](api/create_task.py)
	- [api/get_tasks.py](api/get_tasks.py)
	- [api/delete_task.py](api/delete_task.py)

- These expect a DynamoDB table named `Tasks_Pro`. When deploying to AWS:
	- Create the `Tasks_Pro` table and give the Lambda execution role permission to read/write it.
	- Use API Gateway to expose the Lambdas (map POST/GET/DELETE accordingly).

Development notes
- The mock server (`api/mock_server.js`) is intentionally simple and stores tasks in memory — it resets on restart.
- The Python Lambda code uses `boto3` and is ready for packaging if you deploy with AWS SAM, Serverless Framework, or a manual Lambda + API Gateway setup.

License
- This project is available under the MIT License: [LICENSE](LICENSE)

Next steps
- I can wire the add-task input in the UI to call `TaskAPI.createTask`, render tasks, and wire delete actions — tell me to proceed and I'll implement it.
