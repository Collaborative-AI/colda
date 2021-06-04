import Vue from 'vue';
import VueRouter from 'vue-router';
// 导入 vue-scrollto，跳转到锚点时支持平滑过渡
import VueScrollTo from 'vue-scrollto'

// route level code-splitting
// this generates a separate chunk (about.[hash].js) for this route
// which is lazy-loaded when the route is visited.

// Authentication
const Register = () => import(/* webpackChunkName: "about" */ '@/views/Auth/Register.vue')
const Login = () => import(/* webpackChunkName: "about" */ '@/views/Auth/Login.vue')

const Home = () => import(/* webpackChunkName: "about" */ '../views/Home.vue')
const Profile = () => import(/* webpackChunkName: "about" */ '../views/Profile.vue')
const Chat = () => import(/* webpackChunkName: "about" */ '../views/Chat.vue')
const Notification = () => import(/* webpackChunkName: "about" */ '../views/Notification.vue')
const Askhelp = () => import(/* webpackChunkName: "about" */ '../views/Askhelp.vue')
const Shiyan = () => import(/* webpackChunkName: "about" */ '../views/Shiyan.vue')
const RecivedComments = () => import(/* webpackChunkName: "about" */ '../views/ReceivedRequest.vue')

Vue.use(VueRouter);

// scrollBehavior:
// - only available in html5 history mode
// - defaults to no scroll behavior
// - return false to prevent scroll
const scrollBehavior = (to, from, savedPosition) => {
  if (savedPosition) {
    // savedPosition is only available for popstate navigations.
    return savedPosition
  } else {
    const position = {}
    // new navigation.
    // scroll to anchor by returning the selector
    if (to.hash) {
      // 重要: 延迟1秒等待 DOM 生成，不然跳转到对应的锚点时会提示找不到 DOM
      setTimeout(() => {
        VueScrollTo.scrollTo(to.hash, 200)
      }, 1000)
      position.selector = to.hash
    }
    // check if any matched route config has meta that requires scrolling to top
    if (to.matched.some(m => m.meta.scrollToTop)) {
      // cords will be used if no selector is provided,
      // or if the selector didn't match any element.
      position.x = 0
      position.y = 0
    }
    // if the returned position is falsy or an empty object,
    // will retain current scroll position.
    return position
  }
}

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },  
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {
        requiresAuth: true
    }
  },
  {
    path: '/chat',
    name: 'Chat',
    component: Chat,
    meta: {
        requiresAuth: true
    }
  },
  {
    path: '/notification',
    name: 'Notification',
    component: Notification,
    children: [
        { 
            path: '', 
            redirect: 'comments' 
        },
        {   path: 'comments', 
            component: RecivedComments 
        }
    ],
    meta: {
        requiresAuth: true
    }
  },
  {
    path: '/askhelp',
    name: 'Askhelp',
    component: Askhelp,
    meta: {
        requiresAuth: true
    }
  },
  {
    path: '/shiyan',
    name: 'Shiyan',
    component: Shiyan,
  },
];

const router = new VueRouter({
  scrollBehavior,
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

// router.beforeEach((to, from, next) => {
//     const token = window.localStorage.getItem('token')
//     if (to.matched.some(record => record.meta.requiresAuth) && (!token || token === null)) {
//       next({
//         path: '/login',
//         query: { redirect: to.fullPath }
//       })
//     } else if (token && to.name == 'Login') {
//       // cant go back to login page when after logining in
//       next({
//         path: from.fullPath
//       })
//     } else {
//       next() // stay in the same page
//     }
//   })
export default router;
