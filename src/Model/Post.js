import { is } from 'ramda'

export default class Post {
  constructor (post = {}) {
    this.id = is(String, post.id) ? post.id : ''
    this.images = is(Array, post.images) ? post.images : []
    this.description = is(String, post.description) ? post.description : ''
    this.likes = is(Number, post.likes) ? post.likes : 0
    this.time = is(Date, post.time) ? post.time : new Date()
    this.is_follow = is(Boolean, post.is_follow) ? post.is_follow : false
    this.is_liked = is(Boolean, post.is_liked) ? post.is_liked : false
    this.user = is(Object, post.user) ? post.user : { profile: require('../assets/images/page-img/g1.jpg'), name: 'Nik Jon' }
    this.comments = is(Array, post.comments) ? post.comments : []
  }
}
