import { defineStore } from "pinia"
import coreApi from "@/api/core.api.js"

export const usecoreStore = defineStore("coreStore", {
  state: () => ({
    tasks: [],
    tasksLoading: false,
  }),
  actions: {
    async getTasks() {
      this.tasksLoading = true
      const response = await coreApi.getTasks()
      this.tasks = response.tasks
      this.tasksLoading = false
    },
    async addNewTask(tarefa) {
      const newTask = await coreApi.addNewTask(tarefa.title)
      return newTask
    },
  },
})
