
const os = ('os');
const node_path = window.node_path;
import store from './store'
import db from './db'

export default {
    // check 
    checkAuthority(authority_list){
        if (store.state.authority in authority_list){
            console.log("checkAuthority_true", store.state.authority)
            return true
        }
        console.log("checkAuthority_false", store.state.authority)
        return true
    },
    // includeAuthority(){

    // }
}