import User from '../../Model/User'
import Message from '../../Model/Message'

export const Users = [
  new User({ id: 1, name: 'Anna Sthesia', role: 'Developer', image: require('../../assets/images/user/01.jpg'), isActive: true }),
  new User({ id: 2, name: 'Paul Molive', role: 'Web Designer', image: require('../../assets/images/user/05.jpg'), isActive: false }),
  new User({ id: 3, name: 'Bob Frapples', role: 'App Developer', image: require('../../assets/images/user/03.jpg'), isActive: true }),
  new User({ id: 4, name: 'Barb Ackue', role: 'Ios Developer', image: require('../../assets/images/user/04.jpg'), isActive: true }),
  new User({ id: 5, name: 'Greta Life', role: 'Game Developer', image: require('../../assets/images/user/05.jpg'), isActive: false }),
  new User({ id: 6, name: 'Ira Membrit', role: 'Software Developer', image: require('../../assets/images/user/06.jpg'), isActive: true }),
  new User({ id: 7, name: 'Pete Sariya', role: 'Backend Developer', image: require('../../assets/images/user/07.jpg'), isActive: false }),
  new User({ id: 8, name: 'Anna Sthesia', role: 'Web Developer', image: require('../../assets/images/user/08.jpg'), isActive: true }),
  new User({ id: 9, name: 'Paul Molive', role: 'App Developer', image: require('../../assets/images/user/09.jpg'), isActive: false }),
  new User({ id: 10, name: 'Bob Frapples', role: 'Ios Developer', image: require('../../assets/images/user/10.jpg'), isActive: true }),
  new User({ id: 11, name: 'Anna Sthesia', role: 'Web Designer', image: require('../../assets/images/user/01.jpg'), isActive: true }),
  new User({ id: 12, name: 'Paul Molive', role: 'Game Developer', image: require('../../assets/images/user/05.jpg'), isActive: false }),
  new User({ id: 13, name: 'Bob Frapples', role: 'Web Developer', image: require('../../assets/images/user/03.jpg'), isActive: false }),
  new User({ id: 14, name: 'Barb Ackue', role: 'Ios Developer', image: require('../../assets/images/user/04.jpg'), isActive: true }),
  new User({ id: 15, name: 'Greta Life', role: 'App Developer', image: require('../../assets/images/user/08.jpg'), isActive: true })
]

export const MessagesUser1 = [
  new Message({ text: 'How can we help? We\'re here for you! 😄', userId: 5, me: true, time: '6:45' }),
  new Message({ text: 'Hey John, I am looking for the best admin template. Could you please help me to find it out?🤔', userId: 15, me: false, time: '6:48' }),
  new Message({ text: 'Absolutely!\n' + 'Sofbox Dashboard is the responsive bootstrap 4 admin template.', userId: 5, me: true, time: '6:50' }),
  new Message({ text: 'Looks clean and fresh UI.', userId: 15, me: false, time: '6:55' }),
  new Message({ text: 'Thanks, from ThemeForest.', userId: 5, me: true, time: '6:59' }),
  new Message({ text: 'I will purchase it for sure.', userId: 15, me: false, time: '7:05' }),
  new Message({ text: 'Okay Thanks...', userId: 5, me: true, time: '7:07' }),
  new Message({ text: 'Hey John, I am looking for the best admin template. Could you please help me to find it out?', userId: 15, me: false, time: '7:08' }),
  new Message({ text: 'Absolutely!\n' + 'Sofbox Dashboard is the responsive bootstrap 4 admin template.', userId: 5, me: true, time: '7:10' }),
  new Message({ text: 'Looks clean and fresh UI.', userId: 15, me: false, time: '7:12' }),
  new Message({ text: 'Okay Thanks...', userId: 5, me: true, time: '7:20' })
]

export const MessagesUser2 = [
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message()
]

export const MessagesUser3 = [
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message()
]
export const MessagesUser4 = [
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message(),
  new Message()
]
