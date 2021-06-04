import Vue from 'vue';
import VueRouter from 'vue-router';
// 导入 vue-scrollto，跳转到锚点时支持平滑过渡
import VueScrollTo from 'vue-scrollto'

// route level code-splitting
// this generates a separate chunk (about.[hash].js) for this route
// which is lazy-loaded when the route is visited.

// Authentication
const Register = () => import('@/views/Auth/Register.vue')
const Login = () => import('@/views/Auth/Login.vue')

const Home = () => import('../views/Home.vue')
const Shiyan = () => import('../views/Shiyan.vue')

// User Resources
const Resource = () => import('../views/Resources/Resource.vue')
const MessagesIndexResource = () => import('../views/Resources/Messages/Index.vue')
const SentMessagesResource = () => import('../views/Resources/Messages/List.vue')
const MessagesHistoryResource = () => import('../views/Resources/Messages/History.vue')

// User Notifications
const Notifications = () => import('../views/Notifications/Notifications.vue')
// const RecivedComments = () => import('../views/Notifications/RecivedComments.vue')
const MessagesIndex = () => import('../views/Notifications/Messages/Index.vue')
const RecivedMessages = () => import('../views/Notifications/Messages/List.vue')
const MessagesHistory = () => import('../views/Notifications/Messages/History.vue')

// User Personal Settings
const Settings = () => import('../views/Settings/Settings.vue')
const Profile = () => import('../views/Settings/Profile.vue')

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
    // Modify personal information
    path: '/settings',
    component: Settings,
    children: [
        { 
            path: '', 
            component: Profile 
        },
        {   path: 'profile', 
            name: 'SettingProfile', 
            component: Profile 
        },
    ],
    meta: {
      requiresAuth: true
    }
  },
  {
    // User Resources
    path: '/resource',
    component: Resource,
    children: [
        { 
            path: '', 
            component: MessagesIndexResource 
        },
        { 
            path: 'messages', 
            component: MessagesIndexResource,
              children: [
                  // 默认匹配，你给哪些人发送过私信
                  { 
                      path: '', 
                      name: 'MessagesIndexResource', 
                      component: SentMessagesResource 
                  },
                  // 与某个用户之间的全部历史对话记录
                  { 
                      path: 'history', 
                      name: 'MessagesHistoryResource', 
                      component: MessagesHistoryResource 
                  }
              ]
          }
        ],
    meta: {
      requiresAuth: true
    }
  },
  {
    // 用户通知
    path: '/notifications',
    component: Notifications,
    children: [
        { 
            path: '', 
            component: MessagesIndex 
        },
        // {   path: 'comments', 
        //     name: 'RecivedComments', 
        //     component: RecivedComments 
        // },
        { 
            path: 'messages', 
            component: MessagesIndex,
            children: [
                // 默认匹配，哪些人给你发送过私信
                { 
                    path: '', 
                    name: 'MessagesIndex', 
                    component: RecivedMessages
                },
                // 与某个用户之间的全部历史对话记录
                { 
                    path: 'history', 
                    name: 'MessagesHistory', 
                    component: MessagesHistory
                }
            ]
        },
    ],
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
