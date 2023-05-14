<template>
  <div class="container g-pt-20">
    <div class="row">
      
      <!-- End 左边菜单栏 -->

      <!-- 右边子路由匹配后，显示对应的组件 -->
      <div class="col-lg-12">

        <!-- 居中关键 center keypoint -->

        <router-view></router-view>

      </div>
      <!-- End 嵌套路由 -->
    </div>
  </div>
</template>

<script>
import store from '../../store'
import $ from 'jquery'
import { add_prefix } from '../../utils'

// const store = require('../../store').default
// const $ = require('jquery')

export default {
  name: 'Notifications',  // this is the name of the component
  data () {
    return {
      sharedState: store.state,
      user: '',
      notifications: {  
        unread_messages_count: 0,
      }
    }
  },
  methods: {
    getUser (id) {
      // const path = `/users/${id}`
      let vm = this
      this.$axios.get(add_prefix(`/users/${vm.sharedState.user_id}`, `/user`))
        .then((response) => {
          // handle success
          this.user = response.data
        })
        .catch((error) => {
          // handle error
          console.error(error)
        })
    },
    getUserNotifications (id) {
      let since = 0
      let vm = this
      // const path = `/users/${id}/notifications/?since=${since}`
      // console.log("notification shua xin",since)
      this.$axios.get(add_prefix(`/users/${vm.sharedState.user_id}/`, `/user`))
        .then((response) => {
          // handle success
          const len = response.data.length
          for(var i = 0; i < len; i++) {
            switch (response.data[i].name) {
                       
              case 'unread_messages_count':
                this.notifications.unread_messages_count = response.data[i].payload
                break
              
            }
            since = response.data[i].timestamp
            // console.log("notification shua xin",since)
          }
        })
        .catch((error) => {
          // handle error
          console.error(error)
        })
    }
  },
  created () {
    const user_id = this.sharedState.user_id
    this.getUser(user_id)
    this.getUserNotifications(user_id)
    // tooltip
    $(document).ready(function(){
      $('[data-toggle="tooltip"]').tooltip(); 
    })

  },
  // 当路由变化后(比如变更查询参数 page 和 per_page)重新加载数据
  beforeRouteUpdate (to, from, next) {
    next()
    this.getUserNotifications(this.sharedState.user_id)
  }
}
</script>