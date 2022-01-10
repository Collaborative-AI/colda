import store from '../../../src/store'

function logout_function(){
    test('logout', () => {

        store.logoutAction()
        
    })
}

let logout_helper = {}
// train_helper_functions.login = {}

logout_helper.logout = logout_function


export { logout_helper }