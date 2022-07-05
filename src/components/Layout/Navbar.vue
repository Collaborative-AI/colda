<template>
    <div>
        <div :class="['navbar-area', {'is-sticky': isSticky}]">
            <div class="valzo-nav">
                <div class="container">
                    <nav class="navbar navbar-expand-lg navbar-light">
                        <router-link class="navbar-brand" to="/">
                            <!-- <img src="../../assets/images/logo.png" alt="logo"> -->
                            <div class="row">
                            <!-- <div class="row" style="border-left:0; border:1px solid black;"> -->
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

                        <div class="collapse navbar-collapse zuiwai" :class="{ show: active }" is-nav>
                        <!-- <div class="collapse navbar-collapse" :class="{ show: active }" is-nav style="border-left:0; border:1px solid black; padding: 0px">  -->
                            <div class="zuobian"></div>

                            <ul class="navbar-nav px-0">
                            <!-- <ul class="navbar-nav px-0" style="border:1px solid red;"> -->
                                <li class="nav-item">
                                    <router-link  to="/" class="nav-link">
                                       <p>Home</p> 
                                    </router-link>
                                    <!-- <a href="home" class="nav-link">
                                        <p>Home</p>
                                        <i class='bx bx-chevron-down'></i>
                                    </a> -->
                                    <!-- <ul class="dropdown-menu">
                                        <li class="nav-item">
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
                                        </li>

                                        <li class="nav-item">
                                            <router-link  to="/home-seven" class="nav-link">
                                                Home Seven
                                            </router-link>
                                        </li>

                                        <li class="nav-item">
                                            <router-link  to="/home-eight" class="nav-link">
                                                Home Eight
                                            </router-link>
                                        </li>

                                        <li class="nav-item">
                                            <router-link  to="/home-nine" class="nav-link">
                                                Home Nine
                                            </router-link>
                                        </li>
                                    </ul> -->
                                </li>

                                <li class="nav-item">
                                    <router-link  to="/products" class="nav-link">
                                       <p>Products</p> 
                                    </router-link>
                                </li>

                                <li class="nav-item">
                                    <a href="#" class="nav-link" style="width: 105px">
                                        <p>Resources</p>&nbsp;
                                        <i class='bx bx-chevron-down'></i>
                                    </a>
                                    <ul class="dropdown-menu">
                                        <li class="nav-item">
                                            <a target="_blank" href="html/index.html" class="nav-link"
                                            >Documentation</a>
                                            
                                        </li>

                                        <li class="nav-item">
                                            <a target="_blank" href="notebook/User_Guide.html" class="nav-link"
                                            >Tutorials</a>
                                        </li>

                                        <li class="nav-item">
                                            <router-link  to="/use-cases" class="nav-link">
                                            Use&nbsp;Cases
                                            </router-link>
                                        </li>

                                        
                                    </ul>
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

                                <!-- <li class="nav-item">
                                    <router-link  to="/about" class="nav-link">
                                        About
                                    </router-link>
                                </li> -->

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

                                <!-- <li class="nav-item">
                                    <a href="#" class="nav-link">
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

                                <!-- <li class="nav-item">
                                    <router-link  to="/contact" class="nav-link">
                                        Contact
                                    </router-link>
                                </li> -->
                                <li>
                                    <div class="sign-up">
                                        <router-link to="/sign-in" class="default-btn">Sign&nbsp;In</router-link>
                                    </div>
                                </li>
                        
                            </ul>
                        </div>

                        <!-- <div class="others-options">
                            <div 
                                class="burger-menu"
                                v-on:click="isPopupMethod(isPopup)"
                            >
                                <span></span>
                                <span></span>
                                <span></span>
                            </div>
                        </div> -->
                        <!-- <div class="others-options">
                            <router-link to="/sign-up" class="default-btn">Sign In</router-link>
                        </div> -->

                        
                    </nav>
                </div>
            </div>
        </div>

        <div 
            class="sidebar-modal"
            v-if="isPopup"
        >
            <div class="sidebar-modal-inner">
                <div class="sidebar-about">
                    <div class="title">
                        <h2>About Us</h2>
                        <p>We believe brand interaction is key to communication. Real innovations and positive customer experience are the heart of successful communication. No fake products and services. The customer is king, their lives and needs are the inspiration.</p>
                    </div>
                    <div 
                        class="close-btn"
                        v-on:click="isPopupMethod(isPopup)"
                    >
                        <i class='bx bx-x'></i>
                    </div>
                </div>

                <div class="sidebar-contact-feed">
                    <h2>Contact</h2>
                    <div class="contact-form">
                        <form>
                            <div class="row">
                                <div class="col-lg-12 col-md-12">
                                    <div class="form-group">
                                        <input type="text" name="name" id="name" class="form-control" required placeholder="Your Name">
                                    </div>
                                </div>

                                <div class="col-lg-12 col-md-12">
                                    <div class="form-group">
                                        <input type="email" name="email" id="email" class="form-control" required placeholder="Your Email">
                                    </div>
                                </div>

                                <div class="col-lg-12 col-md-12">
                                    <div class="form-group">
                                        <input type="text" name="phone_number" id="phone_number" required class="form-control" placeholder="Your Phone">
                                    </div>
                                </div>

                                <div class="col-lg-12 col-md-12">
                                    <div class="form-group">
                                        <input type="text" name="msg_subject" id="msg_subject" class="form-control" required placeholder="Your Subject">
                                    </div>
                                </div>

                                <div class="col-lg-12 col-md-12">
                                    <div class="form-group">
                                        <textarea name="message" class="form-control" id="message" cols="30" rows="6" required placeholder="Your Message"></textarea>
                                    </div>
                                </div>

                                <div class="col-lg-12 col-md-12">
                                    <div class="send-btn">
                                        <button type="submit" class="send-btn-one">
                                            Send Message
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>

                <div class="sidebar-contact-area">
                    <div class="contact-info">
                        <div class="contact-info-content">
                            <h2>
                                <a href="tel:+0881306298615">
                                    +088 130 629 8615
                                </a>
                                <span>OR</span>
                                <a href="mailto:valzo@gmail.com">
                                    valzo@gmail.com
                                </a>
                            </h2>

                            <ul class="social">
                                <li>
                                    <a href="#" target="_blank">
                                        <i class="flaticon-facebook"></i>
                                    </a>
                                </li>
                                <li>
                                    <a href="#" target="_blank">
                                        <i class="flaticon-twitter"></i>
                                    </a>
                                </li>
                                <li>
                                    <a href="#" target="_blank">
                                        <i class="flaticon-instagram"></i>
                                    </a>
                                </li>
                                <li>
                                    <a href="#" target="_blank">
                                        <i class="flaticon-pinterest"></i>
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Navbar',
    data(){
        return {
            isSticky: false,
            isPopup: false,
            active: false,
            button_active_state: false
        }
    },
    methods: {
        isPopupMethod(isPopup){
            return this.isPopup = !isPopup
        },
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

<style scoped>
ul {
    margin:0 auto;
    width: 75%;
    display: flex;
    justify-content: space-between;
    /* border:1px solid red; */
}
.nav-item p{
    /* width: 20%; */
    /* margin-left: 5%;
    margin-right: 5% */
    /* margin: auto;
    padding: auto; */
    font-size: 120%;
    color: black;
    display: inline
}
.sign-up {
    margin-top: 15px;
    /* border:1px solid red; */
}
/* .zuiwai {
    border:1px solid blue;
} */
.zuobian {
    /* border:1px solid green; */
    width: 5%
}
/* i {
    display:inline-block;
    white-space:nowrap
} */
.router-link-active p{
  color:#086AD8
}


</style>