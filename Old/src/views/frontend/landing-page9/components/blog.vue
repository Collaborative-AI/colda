<template>
  <section class="pt-lg-0 pt-5">
    <div class="container">
      <TitleSection title="You can know more about us by our latest blogs " subclass="pr-lg-7">
        <template v-slot:rightside>
          <div class="col-lg-5 col-md-6 ">
            <div class="btn-container">
              <a class="iq-button iq-gradient-btn" href="#"><span>Click Here</span><em /></a>
            </div>
          </div>
        </template>
      </TitleSection>
      <div class="row justify-content-sm-center">
        <div class="col-sm-12">
          <div
            class="owl-carousel"
            data-autoplay="true"
            data-loop="true"
            data-nav="false"
            data-dots="true"
            data-items="3"
            data-items-laptop="3"
            data-items-tab="2"
            data-items-mobile="1"
            data-items-mobile-sm="1"
            data-margin="30"
          >
            <div v-for="(item,index) in items" :key="index" class="item">
              <CardStyle5 :title="item.title" :date="item.date" :description="item.description" :src="item.src" text="Read More" style="width: 350px; margin-right: 30px;"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Blog',
  data () {
    return {
      items: [
        {
          title: 'Fully dedicated to finding.',
          date: '1 Feb 2020',
          description:
            ' It is a long established fact that a reader will be distracted.',
          src: require('@/assets/images/landing-page/landing-9/blog-d2-1.jpg')
        },
        {
          title: 'Analytics for your website',
          date: '1 Feb 2020',
          description:
            ' It is a long established fact that a reader will be distracted.',
          src: require('@/assets/images/landing-page/landing-9/blog-d2-2.jpg')
        },
        {
          title: 'Marketing Agencies Strategies',
          date: '1 Feb 2020',
          description:
            ' It is a long established fact that a reader will be distracted.',
          src: require('@/assets/images/landing-page/landing-9/blog-d2-3.jpg')
        }
      ]
    }
  }
}
</script>
