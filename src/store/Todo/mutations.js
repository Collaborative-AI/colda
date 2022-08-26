export default {
  addProjectCommit (state, data) {
    state.projectList.push(data)
  },
  selectedCommit (state, data) {
    switch (data.type) {
      case 'project':
        state.selectedProject = data.data
        break
      case 'category':
        state.selectedCategory = data.data
        break
    }
  },
  addTaskCommit (state, data) {
    state.taskList.push(data)
  },
  updateStatusCommit (state, data) {
    const taskIndex = state.taskList.findIndex(task => task.id === data.id)
    if (data.task_status) {
      data.task_status = false
    } else {
      data.task_status = true
    }
    state.taskList[taskIndex] = data
  }
}
