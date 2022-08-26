import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    appName: 'ProX',
    logo: require('../assets/images/logo.png'),
    darklogo:require('../assets/images/logo-white.png'),
    dark: '',
    namespaced: true,
    user:{
      name:'Barry Tech',
      image:require('../assets/images/user/1.jpg'),
      image2:require('../assets/images/layouts/layout-3/user-1.jpg'),
      image3:require('../assets/images/user/02.jpg')
    }
  },
  mutations: {
  },
  actions: {
  },
  getters: {
    appName: state => { return state.appName },
    logo: state => { return state.logo },
    darklogo: state => { return state.darklogo },
    image1: state => { return state.user.image },
    name: state => { return state.user.name },
    image2:state => { return state.user.image2},
    image3:state => { return state.user.image3}
  },
  modules: {
  }
})
