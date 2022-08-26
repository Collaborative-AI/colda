<template>
  <b-modal id="add_task" centered title="Add Task">
    <b-form>
      <b-form-group
        class="form-group"
        label="Task Title"
        label-for="task_tile"
      >
        <b-form-input name="task_title" v-model="task.task_title" id="task_tile" placeholder=""></b-form-input>
      </b-form-group>
      <b-form-group
        class="form-group"
        label="Assigned By"
        label-for="user_id"
      >
        <v-select v-model="task.user_id" name="user_id" id="user_id" :options="userList" />
      </b-form-group>
      <b-form-group
        class="form-group"
        label="Category"
        label-for="category_id"
      >
        <v-select v-model="task.category_id" name="user_id" id="category_id" :options="categoryList" />
      </b-form-group>
      <b-form-group
        class="form-group"
        label="Priority"
        label-for="priority"
      >
        <b-form-radio inline v-model="task.status" name="priority" :value="item" v-for="(item,index) in status" :key="index">{{ item }}</b-form-radio>
      </b-form-group>
    </b-form>
    <template v-slot:modal-footer>
      <b-button variant="none" class="iq-bg-primary"  @click="$bvModal.hide('add_task')">Cancel</b-button>
      <b-button variant="primary" @click="saveTask(task)">Save</b-button>
    </template>
  </b-modal>
</template>
<script>
import { Users } from '../../../../FackApi/api/chat'
export default {
  name: 'TaskForm',
  props: ['newId', 'category'],
  data () {
    return {
      userList: [],
      categoryList: [],
      status: ['Expiring', 'Ending', 'Urgent'],
      task: this.default()
    }
  },
  mounted () {
    Users.map(item => {
      this.userList.push({
        label: item.name,
        code: item.id
      })
    })
    this.category.map(item => {
      if (!item.isHidden) {
        this.categoryList.push({
          label: item.name,
          code: item.id
        })
      }
    })
  },
  computed: {
  },
  methods: {
    default () {
      return {
        id: this.newId,
        task_title: '',
        project_id: 1,
        category_id: 0,
        user_id: 0,
        status: 'Urgent',
        task_status: false
      }
    },
    saveTask (item) {
      item.id = this.$store.getters['Todo/selectedProjectState'].id
      item.project_id = this.$store.getters['Todo/selectedProjectState'].id
      item.category_id = item.category_id.code
      item.user_id = item.user_id.code
      this.$store.dispatch('Todo/addTaskAction', item)
      this.$bvModal.hide('add_task')
      this.task = this.default()
    }
  }
}
</script>
