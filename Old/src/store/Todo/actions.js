export default {
  addProjectAction (context, payload) {
    return new Promise((resolve, ) => {
      context.commit('addProjectCommit', payload)
      resolve()
    })
  },
  addTaskAction (context, payload) {
    return new Promise((resolve, ) => {
      context.commit('addTaskCommit', payload)
      resolve()
    })
  },
  selectedAction (context, payload) {
    return new Promise((resolve, ) => {
      context.commit('selectedCommit', payload)
      resolve()
    })
  },
  updateStatusAction (context, payload) {
    return new Promise((resolve, ) => {
      context.commit('updateStatusCommit', payload)
      resolve()
    })
  }
}
