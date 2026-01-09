// Simple mock API server for local development (emulates the Lambdas)
const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors());
app.use(express.json());

const tasks = new Map();

app.post('/tasks', (req, res) => {
  const { taskId, description } = req.body;
  if (!taskId || !description) return res.status(400).json({ error: 'Missing taskId or description' });
  const createdAt = new Date().toISOString();
  const item = { taskId, description, createdAt, status: 'PENDING' };
  tasks.set(taskId, item);
  res.json({ message: 'Task Created Successfully', id: taskId, createdAt });
});

app.get('/tasks', (req, res) => {
  const items = Array.from(tasks.values());
  res.json({ count: items.length, tasks: items });
});

app.delete('/tasks/:id', (req, res) => {
  const id = req.params.id;
  tasks.delete(id);
  res.json({ message: `Task ${id} deleted` });
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Mock API server listening on http://localhost:${port}`));
