<template>
    <div id="tab-bar">
        <h1>{{user}}</h1>
        <h1>{{sharedState.user_id}}</h1>
    </div> 
</template>

<script>
import {add_prefix} from '../../utils.js'

export default {
  name: 'Dashboard',
  data () {
    return {
      msg: 'this is profile page',
      sharedState: this.$store.state,
      user: ''
    }
  },
  components: {
    
  },
  methods: {
    getUser () {
      // const path = `/users/${id}`
      let vm = this
      this.$axios.get(add_prefix(`/users/${vm.sharedState.user_id}`, `/user`))
        .then((response) => {
          // handle success
          vm.user = response.data.user
          console.log('user is', vm.user)
        })
        .catch((error) => {
          // handle error
          console.error(error)
        })
    },

  },
  created() {
    const user_id = this.sharedState.user_id
    this.getUser(user_id)
  }

}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
