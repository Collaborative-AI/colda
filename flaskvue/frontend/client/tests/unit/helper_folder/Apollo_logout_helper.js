import store from '../../../src/store'

function logout_function(){
    test('logout_function', () => {
      window.localStorage.removeItem('Apollo-token')
      store.state.is_authenticated = false
      store.state.user_id = 0
    })
}

let logout_helper = {}
// train_helper_functions.login = {}

logout_helper.logout = logout_function


export { logout_helper }