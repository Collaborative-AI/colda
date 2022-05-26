<template>
    <div :class="['navbar-area navbar-two', {'is-sticky': isSticky}]">
        <div class="valzo-nav">
            <div class="container" style="margin-left:5em; margin-right:5em">
                <nav class="navbar navbar-expand-lg navbar-light">
                    <router-link class="navbar-brand" to="/">
                        <!-- <div class="container"> -->
                            <div class="row" style="border-left:0;">
                                <div class="col-4">
                                    <img src="../../assets/images/logo1.png" width="50" height="50" alt="logo">
                                     <!-- <h1>Synspot</h1> -->
                                </div>
                                <div class="col-6">
                                    <!-- <div style="margin-top:10%; color:green"> -->
                                        <h2 style="color:black; font-family: Helvetica">Synspot</h2>
                                    <!-- </div> -->
                                    
                                </div>
                            </div>
                        <!-- </div> -->
                        
                    </router-link>
                    

                    <div 
                        class="navbar-toggler"
                        @click="active = !active" :aria-pressed="active ? 'true' : 'false'"
                        v-bind:class="{ 'active': button_active_state }"
                        v-on:click="button_active_state = !button_active_state"
                    >
                        <span class="icon-bar top-bar"></span>
                        <span class="icon-bar middle-bar"></span>
                        <span class="icon-bar bottom-bar"></span>
                    </div>

                    <div class="collapse navbar-collapse" id="navbarSupportedContent" is-nav>
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <a href="home-seven" class="nav-link">
                                    Home 
                                    <i class='bx bx-chevron-down'></i>
                                </a>
                                <ul class="dropdown-menu">
                                    <!-- <li class="nav-item">
                                        <router-link  to="/" class="nav-link">
                                            Home One
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/home-two" class="nav-link">
                                            Home Two
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/home-three" class="nav-link">
                                            Home Three
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/home-four" class="nav-link">
                                            Home Four
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/home-five" class="nav-link">
                                            Home Five
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/home-six" class="nav-link">
                                            Home Six
                                        </router-link>
                                    </li> -->

                                    <li class="nav-item">
                                        <router-link  to="/home-seven" class="nav-link">
                                            Home Seven
                                        </router-link>
                                    </li>

                                    <!-- <li class="nav-item">
                                        <router-link  to="/home-eight" class="nav-link">
                                            Home Eight
                                        </router-link>
                                    </li> -->

                                    <li class="nav-item">
                                        <router-link  to="/home-nine" class="nav-link">
                                            Home Nine
                                        </router-link>
                                    </li>
                                </ul>
                            </li>

                            

                            <!-- <li class="nav-item">
                                <a href="#" class="nav-link">
                                    Services 
                                    <i class='bx bx-chevron-down'></i>
                                </a>
                                <ul class="dropdown-menu">
                                    <li class="nav-item">
                                        <router-link  to="/services-one" class="nav-link">
                                            Services
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/services-two" class="nav-link">
                                            Services Two
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/single-services" class="nav-link">
                                            Services Details
                                        </router-link>
                                    </li>
                                </ul>
                            </li> -->

                            <!-- <li class="nav-item">
                                <a href="#" class="nav-link">
                                    Projects 
                                    <i class='bx bx-chevron-down'></i>
                                </a>

                                <ul class="dropdown-menu">
                                    <li class="nav-item">
                                        <router-link  to="/projects-one" class="nav-link">
                                            Projects One
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/projects-two" class="nav-link">
                                            Projects Two
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/single-projects" class="nav-link">
                                            Projects details
                                        </router-link>
                                    </li>
                                </ul>
                            </li> -->

                            <!-- <li class="nav-item">
                                <a href="#" class="nav-link">
                                    Pages 
                                    <i class='bx bx-chevron-down'></i>
                                </a>

                                <ul class="dropdown-menu">
                                    <li class="nav-item">
                                        <router-link  to="/about" class="nav-link">
                                            About
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/team" class="nav-link">
                                            Team
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/pricing" class="nav-link">
                                            Pricing
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/faq" class="nav-link">
                                            FAQ
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <a href="#" class="nav-link">
                                            User 
                                            <i class='bx bx-chevron-down'></i>
                                        </a>

                                        <ul class="dropdown-menu">
                                            <li class="nav-item">
                                                <router-link  to="/log-in" class="nav-link">
                                                    Log In
                                                </router-link>
                                            </li>

                                            <li class="nav-item">
                                                <router-link  to="/sign-up" class="nav-link">
                                                    Sign Up
                                                </router-link>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/terms-condition" class="nav-link">
                                            Terms & Conditions
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/privacy-policy" class="nav-link">
                                            Privacy Policy
                                        </router-link>
                                    </li>
                                
                                    <li class="nav-item">
                                        <router-link  to="/error-404" class="nav-link">
                                            404 Error
                                        </router-link>
                                    </li>

                                    

                                    <li class="nav-item">
                                        <router-link  to="/contact" class="nav-link">
                                            Contact
                                        </router-link>
                                    </li>
                                </ul>
                            </li> -->

                            <li class="nav-item">
                                <router-link  to="/products" class="nav-link">
                                    Products
                                </router-link>
                            </li>

                            <li class="nav-item">
                                <a href="#" class="nav-link">
                                    Resources 
                                    <i class='bx bx-chevron-down'></i>
                                </a>
                                <ul class="dropdown-menu">
                                    <li class="nav-item">
                                        <a href="html/index.html" class="nav-link"
                                        >Docs</a>
                                        
                                    </li>

                                    <li class="nav-item">
                                        <a href="notebook/Sponsor_User_Guide.html" class="nav-link"
                                        >Tutorials</a>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/use-cases" class="nav-link">
                                            Use Cases
                                        </router-link>
                                    </li>

                                    
                                </ul>
                            </li>

                            

                            <!-- <li class="nav-item">
                                <a href="/blog-one" class="nav-link">
                                    Blog 
                                    <i class='bx bx-chevron-down'></i>
                                </a>
                                <ul class="dropdown-menu">
                                    <li class="nav-item">
                                        <router-link  to="/blog-one" class="nav-link">
                                            Blog Grid
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/blog-two" class="nav-link">
                                            Blog Right Sidebar
                                        </router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link  to="/single-blog" class="nav-link">
                                            Blog Details
                                        </router-link>
                                    </li>
                                </ul>
                            </li> -->

                            <li class="nav-item">
                                <router-link  to="/about" class="nav-link">
                                    About us
                                </router-link>
                            </li>

                            <li class="nav-item">
                                <router-link  to="/contact" class="nav-link">
                                    Contact
                                </router-link>
                            </li>
                        </ul>
                    </div>

                    <div class="others-options">
                        <router-link to="/sign-up" class="default-btn">Sign In</router-link>
                    </div>
                </nav>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'NavbarStyleTwo',
    
    data(){
        return {
            isSticky: false,
            active: false,
            button_active_state: false,
            publicPath: process.env.BASE_URL
        }
    },
    mounted(){
        const that = this
        window.addEventListener('scroll', () => {
            let scrollPos = window.scrollY
            if(scrollPos >= 100){
                that.isSticky = true
            } else {
                that.isSticky = false
            }
        })
    }
}
</script>