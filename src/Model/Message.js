import { is } from 'ramda'

export default class Message {
  constructor (message = {}) {
    this.id = is(Number, message.id) ? message.id : 0
    this.text = is(String, message.text) ? message.text : ''
    this.time = is(String, message.time) ? message.time : ''
    this.userId = is(Number, message.userId) ? message.userId : ''
    this.me = is(Boolean, message.me) ? message.me : false
    this.created_at = is(Boolean, message.created_at) ? message.created_at : false
  }
}
