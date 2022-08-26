<template>
  <card>
    <template v-slot:body>
      <div class="iq-todo-page">
        <b-form class="position-relative">
          <b-form-group class="mb-0" label-for="search">
            <b-form-input class="todo-search" placeholder="Search" v-model="search" />
            <b-link href="#" class="search-link"><i class="ri-search-line" /></b-link>
          </b-form-group>
        </b-form>
        <div class="add-new-project mt-3 mb-3">
          <b-link href="#" class="d-block new-project" v-b-modal.add_project size="lg"><i class="ri-add-line mr-2"/>Add Project</b-link>
          <b-modal id="add_project" centered title="Add Project">
            <p class="my-2">
              <b-form-input name="project_name" v-model="project.project_name" placeholder="Project Name" />
            </p>
            <template v-slot:modal-footer>
              <b-button variant="none" class="iq-bg-primary"  @click="$bvModal.hide('add_project')">Cancel</b-button>
              <b-button variant="primary" @click="saveProject(project)">Save</b-button>
            </template>
          </b-modal>
        </div>
        <ul class="todo-task-list p-0 m-0">
          <li v-for="(item,index) in filteredList" :key="index" @click="selectProject(item)" :class="`${item.id === selectedProject ? 'active' : ''}`">
            <b-link href="#"><i class="ri-stack-fill mr-2"></i>{{ item.project_name }}</b-link>
            <ul :id="'todo-task'+index" class="sub-task mt-2 p-0" :class="`${item.id === selectedProject.id ? 'show' : ''}`">
              <li v-for="(category, index1) in categoryList" :key="index1" @click="selectCategory(category)" :class="`${category.id === selectedCategory.id ? 'active' : ''}`">
                <b-link :href="category.href"><i class="ri-checkbox-blank-circle-fill" :class="'text-'+category.color" /> {{ category.name }}</b-link>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </template>
  </card>
</template>
<script>
export default {
  name: 'ProjectList',
  props: [
    'selectedProject',
    'selectedCategory',
    'projectList',
    'categoryList'
  ],
  data () {
    return {
      search: '',
      project: {
        id: 0,
        project_name: ''
      }
    }
  },
  methods: {
    saveProject () {
      this.$store.dispatch('Todo/addProjectAction', this.project)
      this.$bvModal.hide('add_project')
    },
    selectProject (project) {
      this.$store.dispatch('Todo/selectedAction', { data: project, type: 'project' })
      this.search = ''
    },
    selectCategory (category) {
      this.$store.dispatch('Todo/selectedAction', { data: category, type: 'category' })
      this.search = ''
    }
  },
  computed: {
    filteredList () {
      return this.projectList.filter(item => {
        return item.project_name.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  mounted () {
  }
}
</script>
