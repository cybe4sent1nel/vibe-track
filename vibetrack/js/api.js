// Client API wrapper for TaskTracker
const API_BASE = 'http://localhost:3000';

window.TaskAPI = {
  async createTask(taskId, description) {
    const res = await fetch(`${API_BASE}/tasks`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ taskId, description })
    });
    return res.json();
  },

  async getTasks() {
    const res = await fetch(`${API_BASE}/tasks`);
    return res.json();
  },

  async deleteTask(taskId) {
    // delete by id param
    const res = await fetch(`${API_BASE}/tasks/${encodeURIComponent(taskId)}`, {
      method: 'DELETE'
    });
    return res.json();
  }
};
