<template>
  <b-container fluid>
    <b-row>
      <b-col lg="3">
        <ProjectList
          :project-list="projectList"
          :category-list="categoryList"
          :selected-category="selectedCategory"
          :selected-project="selectedProject"/>
      </b-col>
      <b-col lg="9">
        <TaskList :task-list="taskList" :project="selectedProject" :category="selectedCategory"/>
      </b-col>
      
    </b-row>
  </b-container>
</template>
<script>
import { core } from '../../../config/pluginInit'
import ProjectList from '../App/todo/ProjectList'
import TaskList from '../App/todo/TaskList'
import { mapGetters } from 'vuex'
import Todo from '../../../store/Todo'
export default {
  name: 'TodoListing',
  components: { ProjectList, TaskList },
  beforeMount () {
    this.$store.registerModule('Todo', Todo)
  },
  beforeDestroy () {
    this.$store.unregisterModule('Todo')
  },
  mounted () {
    core.index()
  },
  computed: {
    ...mapGetters({
      taskList: 'Todo/taskState',
      projectList: 'Todo/projectState',
      categoryList: 'Todo/categoryState',
      selectedCategory: 'Todo/selectedCategoryState',
      selectedProject: 'Todo/selectedProjectState'
    })
  }
}
</script>
<style>
</style>
