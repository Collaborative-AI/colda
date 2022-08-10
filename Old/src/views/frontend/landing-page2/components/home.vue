<template>
    <section id="iq-home" class="iq-banner-02 overview-block-pt  iq-over-blue-90 " :style= "`background: url(${require('@/assets/images/landing-page/landing-2/hr-back.jpg')})`">
        <div class="container">
            <div class="banner-text">
                <div class="row">
                    <div class="col-md-6">
                        <h1 class=" text-white iq-tw-8">Best HR Management Software</h1>
                        <p class="text-white pt-3 mb-4 iq-mlr-100 iq-plr-50">Lorem Ipsum is simply dummy text of the
                            printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever
                            since the 1500s, when an unknown printer took a galley,</p>
                        <a href="javascript:void(0)" class="landing-button banner-btn mt-2 mb-5">Download</a>
                    </div>
                    <div class="col-md-6">
                        <img class="banner-img img-fluid center-block "
                            src="@/assets/images/landing-page/landing-2/01.png" alt="">
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
    </section>
</template>
<script>
export default {
    name:"home"
}
</script>