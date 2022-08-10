<template>
     <div id="iq-home" class="iq-banner-06 iq-bg-over iq-over-blue-85  postion-relative overflow-hidden"
            :style= "`background: url(${require('@/assets/images/landing-page/landing-1/01.jpg')});background-repeat: no-repeat;`">
            <div class="container">
                <div class="banner-text text-center">
                    <div class="row">
                        <div class="col-md-12">
                            <h1 class="text-white">Software SaaS Platform</h1>
                            <p class="text-white pt-2 mb-2">Lorem Ipsum is simply dummy text of the printing. Lorem Ipsum has
                                been the industry's standard dummy text <br>ever since the 1500s, when an unknown printer took a
                                galley,</p>
                        </div>
                        <div class="col-md-12">
                            <img class="banner-img img-fluid center-block"
                                src="@/assets/images/landing-page/landing-1/09.png" alt="">
                        </div>
        
                    </div>
                </div>
            </div>
            <div class="banner-objects">
                <span class="banner-objects-02 iq-fadebounce">
                    <span class="iq-round"></span>
                </span>
                <span class="banner-objects-03 iq-fadebounce">
                    <span class="iq-round"></span>
                </span>
            </div>
        </div>
</template>
<script>
export default {
    name:'home'
}
</script>