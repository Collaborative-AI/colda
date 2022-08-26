<template>
  <section class=" iq-section-space pt-0 iq-section-pb-70">
    <div class="container">
      <div class="row">
        <div v-for="(list,index) in lists" :key="index" class="col-lg-4 col-md-4 col-sm-12">
          <div class="servicebox-datascience wow fadeInUp text-left">
            <div class="service-box-detail">
              <h2 class="data-title">{{ list.title }}</h2>
              <p>{{ list.subtitle }}</p>
              <a class="link-btn" :href="list.href">
              <span class="btn-effect"> Readmore<i class="fas fa-angle-right ml-2"></i></span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Specializing2',
  data() {
    return {
      lists: [
        {
          title: 'IOT Python Programming',
          subtitle: 'Many variations of passages fact that a reader will be distracted content of a page when looking at its layout.',
          href: '#'
        },
        {
          title: 'Fundamentals of Marketing',
          subtitle: 'Contrary to popular established fact that a reader will be content of a page when looking.',
          href: '#'
        },
        {
          title: 'UI/UX Basics and Principles',
          subtitle: 'Many variations of passages fact that a reader will be distracted content of a page when looking at its layout.',
          href: '#'
        }
      ]
    }
  }
}
</script>
