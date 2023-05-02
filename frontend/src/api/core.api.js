import api from "./config.js"

export default {
  getTasks: async () => {
    const response = await api.get("/api/core/tasks/list")
    return response.data
  },
  addNewTask: async (description) => {
    const json = JSON.stringify({ description })
    const response = await api.post(
      "/api/core/tasks/add",
      json
    )
    return response.data
  },
}
