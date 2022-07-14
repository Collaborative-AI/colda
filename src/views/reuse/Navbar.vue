<template>
    <div class="header">
      <div class="container">
        <div class="row">
          <div class="col-xl-12">
            <div class="navigation">
              <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <router-link class="navbar-brand" to="/">
                  <img src="../../assets/images/logo1.png" height="58px" alt=""/>
                  <h2 style="color:black; font-family: Helvetica; margin:20px">Synspot</h2>
                </router-link>
                <b-navbar-toggle target="navbarNavDropdown"> </b-navbar-toggle>
                <b-collapse is-nav id="navbarNavDropdown">
                  <b-navbar-nav tag="ul" class="navbar-nav">
                    <li class="nav-item">
                        <router-link  to="/" class="nav-link">
                            <p>Home</p> 
                        </router-link>
                    </li>
                    <li class="nav-item">
                      <router-link  to="/products" class="nav-link">
                            <p>Products</p> 
                      </router-link>
                    </li>
                    <li class="nav-item dropdown">
                      
                        <a href="#" class="nav-link" ><p>Resources</p></a>
                        <div class="dropdown-content">
                            <a target="_blank" href="html/index.html" >Documentation</a>
                            <a target="_blank" href="notebook/User_Guide.html">Tutorials</a>
                            <router-link  to="/usecases">
                                Use Cases
                            </router-link>
                        </div>
                      
                    </li>
                    <li class="nav-item">
                      <router-link  to="/about" class="nav-link">
                            <p>About</p> 
                      </router-link>
                    </li>
                    <li class="nav-item">
                      <router-link  to="/contact" class="nav-link">
                            <p>Contact</p> 
                      </router-link>
                    </li>
                    <li class="nav-item">
                      <router-link  to="/dashboard" class="nav-link">
                            <p>Dashboard</p> 
                      </router-link>
                    </li>


                  </b-navbar-nav>
                </b-collapse>

                <div class="signin-btn" style="margin-top: -10px">
                  <router-link class="btn btn-primary text-white" :to="dark ? '/signin-dark': '/signin'"
                    >Sign in</router-link
                  >
                </div>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </div>

</template>

<script>
// 标准模板
export default {
  name: 'Navbar',
  data () {
    return {
      msg: 'this is profile page'
    }
  },
  components: {
    
  },
  methods: {

  }

}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.dropbtn {
  /* background-color: #04AA6D; */
  color: rgb(1, 1, 1);
  padding: 16px;
  font-size: 16px;
  border: none;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #ddd;}

.dropdown:hover .dropdown-content {display: block;}

/* .dropdown:hover .dropbtn {background-color: #3e8e41;} */


</style>