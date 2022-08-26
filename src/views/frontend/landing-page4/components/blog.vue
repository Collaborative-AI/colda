<template>
  <section class="iq-section-pb-55 iq-section-space res-pt overflow-hidden position-relative">
    <div class="container">
      <TitleSection title="You can know more about us by our latest blogs" subclass="pr-lg-6">
        <template v-slot:underline>
          <p class="iq-line six" />
        </template>
        <template v-slot:rightside>
          <div class="col-lg-6 col-md-6">
            <div class="btn-container">
              <a class="iq-button d-inline-block" href="#"><span>Click Here</span><em /></a>
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
            data-dots="false"
            data-items="3"
            data-items-laptop="3"
            data-items-tab="2"
            data-items-mobile="1"
            data-items-mobile-sm="1"
            data-margin="30"
          >
            <div v-for="(item,index) in items" :key="index" class="item">
              <CardStyle3 text="Read More" :src="item.src" :title="item.title" :date="item.date" :description="item.description" style="width: 350px; margin-right: 30px;"/>
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
          title: 'Fully dedicated to finding',
          date: '1 Feb 2020',
          description: 'It is a long established fact that a reader will be distracted by the readable.',
          src: require('@/assets/images/landing-page/landing-4/blog-1.jpg')
        },
        {
          title: 'Analytics for your website',
          date: '1 Feb 2020',
          description:
            'It is a long established fact that a reader will be distracted by the readable.',
          src: require('@/assets/images/landing-page/landing-4/blog-2.jpg')
        },
        {
          title: 'Beautiful Presentations for Site',
          date: '1 Feb 2020',
          description:
            'It is a long established fact that a reader will be distracted by the readable.',
          src: require('@/assets/images/landing-page/landing-4/blog-3.jpg')
        },
        {
          title: 'Marketing Agencies Strategies',
          date: '1 Feb 2020',
          description:
            'It is a long established fact that a reader will be distracted by the readable.',
          src: require('@/assets/images/landing-page/landing-4/blog-4.jpg')
        },
        {
          title: 'Tools for Digital Growth',
          date: '1 Feb 2020',
          description:
            'It is a long established fact that a reader will be distracted by the readable.',
          src: require('@/assets/images/landing-page/landing-4/blog-5.jpg')
        },
        {
          title: 'Analytics for your website',
          date: '1 Feb 2020',
          description:
            'It is a long established fact that a reader will be distracted by the readable.',
          src: require('@/assets/images/landing-page/landing-4/blog-6.jpg')
        }
      ]
    }
  }
}
</script>
