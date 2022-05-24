<template>
    <div class="main-banner-area-eight">
        <div class="d-table">
            <div class="d-table-cell">
                <div class="container">
                    <div class="row align-items-center">
                        <div class="col-lg-6">
                            <div class="main-banner-content">
                                <span>Welcome To App Showcase</span>
                                <h1>Awesome App For Your Modern Lifestyle</h1>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing incididunt ut laboredolore magna aliqua elsed  tempomet, consectetur adipiscing.</p>
                                <div class="banner-btn">
                                    <a href="#" class="default-btn">Get Started</a>
                                </div>
                            </div>
                        </div>

                        <div class="col-lg-6">
                            <div class="banner-form">
                                <form id="contactForm">
                                    <div class="form-group">
                                        <input type="text" name="name" id="name" class="form-control" required placeholder="Name">
                                    </div>
                                    
                                    <div class="form-group">
                                        <input type="email" name="email" id="email" class="form-control" required placeholder="Your Email">
                                    </div>
                                    
                                    <div class="form-group">
                                        <input type="text" name="msg_subject" id="msg_subject" class="form-control" required placeholder="Your Subject">
                                    </div>
                                    
                                    <div class="form-group">
                                        <textarea name="message" class="form-control" id="message" cols="30" rows="6" required placeholder="Your Message"></textarea>
                                    </div>
        
                                    <button type="submit" class="default-btn">
                                        Send Message
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="default-shape">
            <div class="shape-1">
                <img src="../../assets/images/shapes/shape-4.png" alt="image">
            </div>

            <div class="shape-2 rotateme">
                <img src="../../assets/images/shapes/shape-5.svg" alt="image">
            </div>

            <div class="shape-3">
                <img src="../../assets/images/shapes/shape-6.svg" alt="image">
            </div>

            <div class="shape-4">
                <img src="../../assets/images/shapes/shape-7.png" alt="image">
            </div>

            <div class="shape-5">
                <img src="../../assets/images/shapes/shape-8.png" alt="image">
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Banner'
    }
</script>