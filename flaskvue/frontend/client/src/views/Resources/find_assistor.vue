<template>
  <div class="container g-pt-20">
    <div class="row">
      <!-- 左边菜单栏 -->
      <div class="col-lg-3 g-mb-50">
        <aside class="g-brd-around g-brd-gray-light-v4 rounded g-px-20 g-py-30">
          <!-- 用户头像 -->
          <div v-if="user" class="text-center g-pos-rel g-mb-30">
            <div class="g-width-100 g-height-100 mx-auto mb-3">
              <!-- v-bind:src="user._links.avatar" -->
              <img class="img-fluid rounded-circle g-brd-around g-brd-gray-light-v4 g-pa-2" v-bind:src="user._links.avatar"  v-bind:alt="user.name || user.username">
            </div>

            <span class="d-block g-font-weight-500">{{ user.name || user.username }}</span>

            <router-link v-bind:to="{ path: `/user/${sharedState.user_id}` }">
              <span class="u-icon-v3 u-icon-size--xs g-color-white--hover g-bg-primary--hover rounded-circle g-pos-abs g-top-0 g-right-15 g-cursor-pointer" title="Go To Your Profile"
                    data-toggle="tooltip"
                    data-placement="top">
                <i class="icon-finance-067 u-line-icon-pro"></i>
              </span>
            </router-link>
          </div>
          <!-- End 用户头像 -->

          <hr class="g-brd-gray-light-v4 g-my-30">

          <!-- 菜单列表 -->
          <ul class="list-unstyled mb-0">
            <!-- <li class="g-pb-3">
              <router-link v-bind:to="{ name: 'PostsResource' }" v-bind:active-class="'active g-color-primary--active g-bg-gray-light-v5--active'" class="d-block align-middle u-link-v5 g-color-text g-color-primary--hover g-bg-gray-light-v5--hover rounded g-pa-3">
                <span class="u-icon-v1 g-color-gray-dark-v5 mr-2"><i class="icon-education-008 u-line-icon-pro"></i></span>
                Posts
              </router-link>
            </li> -->
            <li class="g-py-3">
              <router-link v-bind:to="{ name: 'MessagesIndexResource' }" v-bind:active-class="'active g-color-primary--active g-bg-gray-light-v5--active'" class="d-block align-middle u-link-v5 g-color-text g-color-primary--hover g-bg-gray-light-v5--hover rounded g-pa-3">
                <span class="u-icon-v1 g-color-gray-dark-v5 mr-2"><i class="icon-communication-154 u-line-icon-pro"></i></span>
                History
              </router-link>
            </li>
          </ul>
          <!-- End 菜单列表 -->
        </aside>
      </div>
      <!-- End 左边菜单栏 -->

      <!-- 右边子路由匹配后，显示对应的组件 -->
      <div class="col-lg-9 g-mb-50">

        <router-view></router-view>

      </div>
      <!-- End 嵌套路由 -->
    </div>
  </div>
</template>

<script>
import store from '../../store'
import $ from 'jquery'

export default {
  name: 'Find_Assistor',  // this is the name of the component
  data () {
    return {
      sharedState: store.state,
      user: ''
    }
  },
  methods: {
    getUser (id) {
      const path = `/users/${id}`
      this.$axios.get(path)
        .then((response) => {
          // handle success
          this.user = response.data
        })
        .catch((error) => {
          // handle error
          console.error(error)
        })
    },

    submit() {
      try{
        let stdout = ex.execSync('python3 ../../../algorithm/make_dataset.py --num_users 2', {encoding: 'utf8'})
        console.log(stdout.split("\n"))
      }catch{
        console.log("wrong")
      }

      // const sponsor_data_folder = 'Sponsor_Data/'
      // fs.mkdirSync(sponsor_data_folder, { recursive: true})

      // const filename = 'shiyan.csv'
      // const data = fs.readFileSync(sponsor_data_folder + filename,
      //   {encoding:'utf8', flag:'r'});
      
      // let data_array = data.split("\n")

      const payload = {
        assistor_id_list: [5],
        id_file: data_array
      }
      
      this.$axios.post('/find_assistor/', payload)
        .then((response) => {
          const Log_address = 'Local_Data/' + this.sharedState.user_id + '/' + response.data.task_id + '/' + 'train/' + 'Log.txt'
          // handle success
          console.log("1.1 Sponsor calls for help", response)
          this.$toasted.success(`1.1 Sponsor calls for help`, { icon: 'fingerprint' })

          console.log("1.2 Sponsor sends id file")
          this.$toasted.success(`1.2 Sponsor sends id file`, { icon: 'fingerprint' })

          // Create 'Local_Data/id/task_id/' folder
          // const new_address = 'Local_Data/' + this.sharedState.user_id + '/' + response.data.task_id + '/'
          // fs.mkdirSync(new_address, { recursive: true})
          

          try {
            fs.appendFileSync(Log_address, "---------------------- Train Stage Starts\n")
            fs.appendFileSync(Log_address, "---------------------- 1. Find assistor\n")
            fs.appendFileSync(Log_address, "1.1 Sponsor calls for help\n")
            fs.appendFileSync(Log_address, "1.2 Sponsor sends id file\n")
          } catch (err) {
            console.error(err)
          }

          // console.log("1.3 Sponsor creates " + new_address)
          // this.$toasted.success("1.3 Sponsor creates " + new_address, { icon: 'fingerprint' })

          try {
            // fs.appendFileSync(Log_address, "1.3 Sponsor creates " + new_address + "\n")
            fs.appendFileSync(Log_address, "---------------------- 1. Find assistor Done\n")
          } catch (err) {
            console.error(err)
          }

        })
        .catch((error) => {
          // handle error
          console.log(error)
          // console.log(error.response.data)
          // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })

    }
  },
  created () {
    const user_id = this.sharedState.user_id
    this.getUser(user_id)
    // tooltip
    $(document).ready(function(){
      $('[data-toggle="tooltip"]').tooltip(); 
    })
  }
}
</script>