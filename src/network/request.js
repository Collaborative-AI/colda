import axios from 'axios'

const request = axios.create({
    baseURL: 'http://synspot-environment.eba-gug8tkzj.us-east-2.elasticbeanstalk.com',
    timeout: 5000
})

export {request}

// function request(config, success, failure) {
//     const instance = axios.create({
//         baseURL: 'http://synspot-environment.eba-gug8tkzj.us-east-2.elasticbeanstalk.com',
//         timeout: 5000
//     })
//     instance(config)
//         .then(res => {
//             // console.log('result is', res);
//             success(res)
//         })
//         .catch(err => {
//             // console.log('err is', err);
//             failure(err)
//         })
// }

// export {request}