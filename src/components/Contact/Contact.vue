<template>
    <div class="contact-section pb-100">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="contact-text">
                        <h3>Have Any Questions About Us?</h3>
                        <p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed eiusmod tempor incididunt ut labore </p>
                    </div>

                    <div class="contact-form">
                        <form id="contactForm">
                            <div class="form-group">
                                <label>Name</label>
                                <input type="text" name="name" id="name" class="form-control" required placeholder="Name">
                            </div>
                            
                            <div class="form-group">
                                <label>Email</label>
                                <input type="email" name="email" id="email" class="form-control" required placeholder="Your Email">
                            </div>
                            
                            <div class="form-group">
                                <label>Subject</label>
                                <input type="text" name="msg_subject" id="msg_subject" class="form-control" required placeholder="Your Subject">
                            </div>
                            
                            <div class="form-group">
                                <label>Message</label>
                                <textarea name="message" class="form-control" id="message" cols="30" rows="6" required placeholder="Your Message"></textarea>
                            </div>

                            <div class="send-btn">
                                <button type="submit" class="default-btn">
                                    Send Message
                                </button>
                            </div>
                        </form>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="contact-image">
                        <img src="../../assets/images/contact.png" alt="image">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Contact'
    }
</script>